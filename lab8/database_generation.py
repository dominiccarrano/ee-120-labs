import argparse
import scipy.signal as signal
import numpy as np
import pandas as pd
import csv
import os

from scipy.io import wavfile
from shazam_utils import generate_hash
from scipy.ndimage import maximum_filter

def fingerprint(audio, fs, min_distance=25, amp_thresh=40, hashes_per_peak=15):
    NEIGHBORHOOD_SIZE = 2 * min_distance + 1
    AMP_THRESH = amp_thresh
    HASHES_PER_PEAK = hashes_per_peak
    
    audio = np.mean(audio, axis=1)
    f1, t1, spect = signal.spectrogram(audio, fs, nperseg=4096)

    max_spect = maximum_filter(spect, size = NEIGHBORHOOD_SIZE, mode='constant')
    mask = max_spect == spect
    mask &= spect > AMP_THRESH
    freq_idx, time_idx = np.nonzero(mask)
    
    times, freqs = t1[time_idx], f1[freq_idx]
    sorted_peaks = sorted(zip(freqs, times), key=lambda x: x[1])
    hashes = []
    for i in range(len(sorted_peaks)):
        for j in range(1, HASHES_PER_PEAK):
            if i + j >= len(sorted_peaks):
                break
            f1, t1 = sorted_peaks[i]
            f2, t2 = sorted_peaks[i + j]
            hashes.append(generate_hash(f1, f2, t1, t2))
            
    return hashes

def detect(audio, fs):
    db = pd.read_csv("database.csv", header=None, names=["Hash", "Offset", "Song"])

    hashes = fingerprint(audio, fs)
    db_matches = db[db.Hash.isin(map(lambda x: x[0], hashes))]
    if len(db_matches) == 0:
        print("No Matches")
        return

    counts = db_matches.groupby("Song").size()
    counts = counts / counts.sum()
    return counts.idxmax(), counts.max()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="File to Shazam")
    parser.add_argument("--mode", dest="mode", required=True, default="fingerprint", type=str)
    parser.add_argument("--start", dest="start", type=float)
    parser.add_argument("--end", dest="end", type=float)

    args = parser.parse_args()

    if args.mode == "fingerprint":
        fs, audio = wavfile.read(args.file)
        hashes = fingerprint(audio, fs)
        
        with open('database.csv', mode='a') as db_file:
            db_writer = csv.writer(db_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            for hash_pair in hashes:
                db_writer.writerow([hash_pair[0], hash_pair[1], args.file[:-4]])

    else:
        fs, audio = wavfile.read(args.file)
        audio = audio[int(args.start * fs) : int(args.end * fs)]
        print("Predicting: {}, Confidence: {:.6f}".format(*detect(audio, fs)))