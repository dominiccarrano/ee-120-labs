# DO NOT EDIT!!!

import numpy as np
import matplotlib.pyplot as plt
import time

# Adapted from the `sg_plot` function in EE 123 Spring 2016 Lab 3A, which can be found at
# https://inst.eecs.berkeley.edu/~ee123/sp16/lab/lab3/lab3-Part_I_Time-Frequency-Spectrogram.html
def specshow(t_range, f_range, Sxx, dr=60):
    """
    Plot the spectrogram of a signal for a specified dynamic range.
    
    t_range - 
    f_range - 
    Sxx     - 2D array representing the magnitude squared of a signal's STFT
    dr      - Dynamic range to use for plotting, in decibels.
    """
    mds = 10.0 ** (-dr / 20.0) # minimum detectable signal
    
    # Compute log-scale power spectrum, normalized so max power is 0 dB
    Sxx_db = 20.0 * np.log10((Sxx / Sxx.max()) * (1-mds) + mds)
    
    # Vertically flip image since we want frequnecy to increase along vertical axis of spectrogram
    Sxx_db = np.flipud(Sxx_db)
    
    fig = plt.figure(figsize=(16,6))
    plt.imshow(Sxx_db, extent=t_range+f_range, cmap=plt.cm.inferno, aspect='auto')
    plt.colorbar(format='%+2.0f dB')
    plt.xlabel('Time (sec)')
    plt.ylabel('Frequency (Hz)')
    plt.title("Log-Scale Spectrogram")
    plt.tight_layout()
    plt.show()

def plot_runtimes_2(input_sizes, avg_times, plot_title, ymax=None):
    plt.figure(figsize=(16, 10))
    plt.title(plot_title)
    plt.plot(input_sizes, avg_times)
    plt.ylabel("Average Runtime (seconds)")
    plt.xlabel("Input Size")
    plt.xlim([1, input_sizes[-1]])
    if ymax:
        plt.ylim([0, ymax])
    plt.show()

def plot_runtimes(input_sizes, dft_avg_times, my_avg_times, plot_title, ymax=None):
    plt.figure(figsize=(16, 4))
    plt.title(plot_title)
    plt.plot(input_sizes, dft_avg_times, label="Naive DFT")
    plt.plot(input_sizes, my_avg_times, label="Our FFT")
    plt.legend()
    plt.ylabel("Average Runtime (seconds)")
    plt.xlim([1, input_sizes[-1]])
    if ymax:
        plt.ylim([0, ymax])
    plt.show()

def get_avg_runtimes(f, input_sizes, num_trials, zero_pad=False):
    """
    Given an FFT function f and an iterable type (list, range, etc.) of input_sizes,
    returns the average (over num_trials) trials runtime of f for randomly generated 
    data of each size within input_sizes.
    """
    runtimes = []
    for n in input_sizes:
        data = random_complex_array(n)
        if zero_pad:
            L = next_power_of(2, len(data)) - len(data)
            data = np.concatenate((data, np.zeros(L)))
        runtimes.append(time_execution(f, data, num_trials))
    return runtimes

def next_power_of(k, n):
    """
    Returns the next power of k after and including the number n.
    Not numerically stable.
    
    >>> next_power_of(2, 5)     # next power of 2 after/including 5
    8
    >>> next_power_of(2, 16)    # next power of 2 after/including 16
    16
    >>> next_power_of(3, 81)    # next power of 3 after/including 81
    81
    >>> next_power_of(3, 28)    # next power of 3 after/including 28
    81
    """
    res = np.ceil(np.log(n) / np.log(k))
    return k ** res.astype('int')

def time_execution(f, arg, num_trials):
    """
    Returns the runtime of a single argument function f when called on arg,
    averaged over num_trials trials.
    """
    times = []
    for _ in range(num_trials):
        t0 = time.time()
        f(arg)
        tf = time.time()
        times.append(tf - t0)
    return sum(times) / len(times)

def random_complex_array(N):
    """
    Generates a length N numpy array of complex numbers whose real and imaginary 
    parts are both chosen uniformly at random from the interval [0, 1).
    """
    re = np.random.rand(N)
    im = np.random.rand(N)
    return re + 1j*im

def run_fft_tests(my_fft):
    """
    Run tests comparing FFT functions f, g, and display information about
    pass/fail and runtime. This is not meant to be used for performance
    profiling, rather just a ballpark for whether or not the function's
    runtimes are reasonable, as the time will also include printing time
    which technically shouldn't be factored in.
    """
    ref_fft = np.fft.fft
    
    # three tests on fixed data
    x1 = np.array([1, 2, 3])
    print("Test 1 passed: {0}".format(np.allclose(my_fft(x1), ref_fft(x1))))

    x2 = np.array([-1, 1j, -1, 1j])
    print("Test 2 passed: {0}".format(np.allclose(my_fft(x2), ref_fft(x2))))

    x3 = np.zeros(2 ** 8)
    print("Test 3 passed: {0}".format(np.allclose(my_fft(x3), ref_fft(x3))))

    # randomized larger datasets to test on
    x4 = np.random.rand(2 ** 8)
    print("Test 4 passed: {0}".format(np.allclose(my_fft(x4), ref_fft(x4))))

    x5 = random_complex_array(2 ** 8)
    print("Test 5 passed: {0}".format(np.allclose(my_fft(x5), ref_fft(x5))))


def run_xcorr_tests(my_xcorr, my_gauss_pulse):
    # Test 1: xcorr([1,2], [1,2])
    test1_correct = np.array([0, .4, 1, .4])
    test1_actual = my_xcorr([1,2], [1,2])

    # Test 2: xcorr([-1, 0, 1], [-1.5, 0.2, 1.5])
    test2_correct = np.array([ 0.00000000e+00, -1.38165169e-17, -4.97792484e-01,  6.63723312e-02,
            9.95584967e-01, -6.63723312e-02, -4.97792484e-01,  1.38165169e-17])
    test2_actual = my_xcorr([-1, 0, 1], [-1.5, 0.2, 1.5])

    # Test 3: xcorr([1,1,1,1,1], [1,2,3,2,1])
    test3_correct = np.array([ 0.00000000e+00, -9.11251831e-17, -4.55625916e-17, -2.27812958e-17,
            1.02597835e-01,  3.07793506e-01,  6.15587011e-01,  8.20782682e-01,
            9.23380517e-01,  8.20782682e-01,  6.15587011e-01,  3.07793506e-01,
            1.02597835e-01, -2.27812958e-17, -4.55625916e-17, -9.11251831e-17])
    test3_actual = my_xcorr([1,1,1,1,1], [1,2,3,2,1])

    # Test 4: xcorr([1, 1], [3, 6, 9])
    test4_correct = np.array([0.56694671, 0.18898224, 0.56694671, 0.94491118])
    test4_actual = my_xcorr([1, 1], [3, 6, 9])

    # Test 5: cross-correlation of two gaussian pulses (should give a Gaussian with a new FWHM)
    sig = my_gauss_pulse(50, 10)
    test5_correct = my_gauss_pulse(128, 14.14213)
    test5_actual = my_xcorr(sig, sig)

    num_tests = 5
    one_passed = np.allclose(test1_correct, test1_actual)
    two_passed = np.allclose(test2_correct, test2_actual)
    three_passed = np.allclose(test3_correct, test3_actual)
    four_passed = np.allclose(test4_correct, test4_actual)
    five_passed = np.allclose(test5_correct, test5_actual)
    num_passed = one_passed + two_passed + three_passed + four_passed + five_passed

    print("Test 1 (same input lengths) passed: {}".format(one_passed))
    print("Test 2 (same input lengths) passed: {}".format(two_passed))
    print("Test 3 (same input lengths) passed: {}".format(three_passed))
    print("Test 4 (diff input lengths) passed: {}".format(four_passed))
    print("Test 5 (same input lengths) passed: {}".format(five_passed))
    print("{0} of {1} tests passed".format(num_passed, num_tests))