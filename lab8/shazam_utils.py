import hashlib
import csv

from scipy.io import wavfile

def generate_hash(f1, f2, t1, t2, hash_length = 20):
    td = t2 - t1
    h = hashlib.sha1(("%s|%s|%s" % (str(f1), str(f2), str(td))).encode("utf-8"))
    return h.hexdigest()[0:hash_length], t1

