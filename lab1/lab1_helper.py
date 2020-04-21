"""DO NOT CHANGE THIS FILE"""

import numpy as np
import time

def pure_tone_tests(your_pure_tone_gen):
    test1_yours, test1_staff = your_pure_tone_gen("A#", 44100, .0001), np.array([0., 0.04878004, 0.09744394, 0.14587583])
    test2_yours, test2_staff = your_pure_tone_gen("C", 20, 3, 2), np.array([ 0.00000000e+00,  1.79862426e+00, -1.57310311e+00, -4.22765247e-01, 1.94285979e+00, -1.27648837e+00, -8.26424372e-01,  1.99929122e+00, -9.22185003e-01, -1.19273472e+00,  1.96536825e+00, -5.26205128e-01, -1.50514154e+00,  1.84262396e+00, -1.06444350e-01, -1.74952617e+00, 1.63660555e+00,  3.18126992e-01, -1.91484408e+00,  1.35662367e+00, 7.28321151e-01, -1.99362401e+00,  1.01533160e+00,  1.10560013e+00, -1.98230566e+00,  6.28153424e-01,  1.43291348e+00, -1.88140053e+00, 2.12586971e-01,  1.69546886e+00, -1.69546886e+00, -2.12586971e-01, 1.88140053e+00, -1.43291348e+00, -6.28153424e-01,  1.98230566e+00, -1.10560013e+00, -1.01533160e+00,  1.99362401e+00, -7.28321151e-01, -1.35662367e+00,  1.91484408e+00, -3.18126992e-01, -1.63660555e+00, 1.74952617e+00,  1.06444350e-01, -1.84262396e+00,  1.50514154e+00, 5.26205128e-01, -1.96536825e+00,  1.19273472e+00,  9.22185003e-01, -1.99929122e+00,  8.26424372e-01,  1.27648837e+00, -1.94285979e+00, 4.22765247e-01,  1.57310311e+00, -1.79862426e+00, -2.42920406e-13])
    test3_yours, test3_staff = your_pure_tone_gen("F", 4800, .01, octave_offset=-1), np.array([ 0.,  0.23116988,  0.44981655,  0.64409522,  0.8034812, 0.91934002,  0.98539525,  0.99806848,  0.95667314,  0.86345175, 0.72345442,  0.54426526,  0.3355915 ,  0.10873768, -0.12400682, -0.35003346, -0.55709767, -0.73398212, -0.87110441, -0.96103619, -0.99890556, -0.98266103, -0.9131826 , -0.79423415, -0.63225949, -0.43603332, -0.21618583,  0.01537315,  0.2460993 ,  0.46349348, 0.65577872,  0.81253834,  0.92528016,  0.98789659,  0.9969955, 0.95208397,  0.85559502,  0.71275574,  0.5313042,  0.32107022, 0.09344283, -0.13924665, -0.36439269, -0.56979842, -0.74433635, -0.87855119, -0.96517211, -0.99950656])
    test4_yours, test4_staff = your_pure_tone_gen("D", 44100, .001, octave_offset=9), np.array([ 0., -0.00409137,  0.00818266, -0.01227382,  0.01636478, -0.02045546,  0.02454579, -0.02863572,  0.03272517, -0.03681407, 0.04090235, -0.04498995,  0.0490768 , -0.05316282,  0.05724795, -0.06133213,  0.06541528, -0.06949733,  0.07357823, -0.07765788, 0.08173624, -0.08581324,  0.08988879, -0.09396284,  0.09803532, -0.10210615,  0.10617528, -0.11024263,  0.11430813, -0.11837173, 0.12243333, -0.12649289,  0.13055034, -0.13460559,  0.1386586, -0.14270928,  0.14675758, -0.15080341,  0.15484673, -0.15888745, 0.16292551, -0.16696084,  0.17099338, -0.17502306])
    test1_passed = np.allclose(test1_yours, test1_staff)
    test2_passed = np.allclose(test2_yours, test2_staff)
    test3_passed = np.allclose(test3_yours, test3_staff)
    test4_passed = np.allclose(test4_yours, test4_staff)
    print("Test 1 Passed: {}".format(test1_passed))
    print("Test 2 Passed: {}".format(test2_passed))
    print("Test 3 Passed: {}".format(test3_passed))
    print("Test 4 Passed: {}".format(test4_passed))
    print("\n{0} out of {1} tests passed".format(sum(np.array([test1_passed,test2_passed,test3_passed,test4_passed])), 4))

def run_tests(your_decaying_expo):    
    num_passed = 0
    
    ### Index tests, non-negative n_start ###
    test1_yours, _ = your_decaying_expo(.95, 0, 20)
    test1_staff = np.arange(0, 21)
    test1_passed = np.allclose(test1_yours, test1_staff)
    
    test2_yours, _ = your_decaying_expo(.8, 3, 20)
    test2_staff = np.arange(3, 21)
    test2_passed = np.allclose(test2_yours, test2_staff)
    
    print("Testing indices are correct when n_start >= 0")
    print("Test 1 Passed: {}".format(test1_passed))
    print("Test 2 Passed: {}".format(test2_passed))
    
    ### Signal tests, non-negative n_start ###
    _, test3_yours = your_decaying_expo(.95, 0, 20)
    test3_staff = np.array([1.0,0.38674102345450123,0.14956861922263506,0.057844320874838484,0.0223707718561656,0.008651695203120634,0.003345965457471275,0.001294022105465849,0.0005004514334406108,0.00019354509955809418,7.48518298877006e-05,2.894827329821157e-05,1.119548484259096e-05,4.329753266092978e-06,1.674493209434269e-06,6.475952175842209e-07,2.504516372327622e-07,9.685992250925397e-08,3.7459705562952584e-08,1.4487204867720514e-08,5.602796437537268e-09])
    test3_passed = np.allclose(test3_staff, test3_yours)
    
    _, test4_yours = your_decaying_expo(.8, 0, 20)
    test4_staff = np.array([1.0,0.44932896411722156,0.20189651799465538,0.09071795328941247,0.04076220397836621,0.01831563888873418,0.008229747049020023,0.003697863716482929,0.001661557273173934,0.0007465858083766792,0.00033546262790251185,0.0001507330750954765,6.772873649085378e-05,3.0432483008403625e-05,1.3674196065680938e-05,6.14421235332821e-06,2.7607725720371986e-06,1.2404950799567113e-06,5.573903692694596e-07,2.504516372327617e-07,1.1253517471925912e-07])
    test4_passed = np.allclose(test4_staff, test4_yours)
    
    _, test5_yours = your_decaying_expo(.3, 0, 20)
    test5_staff = np.array([1.0,0.7408182206817179,0.5488116360940265,0.40656965974059917,0.30119421191220214,0.22313016014842982,0.16529888822158656,0.1224564282529819,0.09071795328941251,0.06720551273974978,0.049787068367863944,0.036883167401240015,0.02732372244729257,0.02024191144580439,0.014995576820477703,0.011108996538242306,0.00822974704902003,0.006096746565515638,0.00451658094261267,0.003345965457471272,0.0024787521766663585]) 
    test5_passed = np.allclose(test4_staff, test4_yours)
    
    print("\nTesting signal values are correct when n_start >= 0")
    print("Test 3 Passed: {}".format(test3_passed))
    print("Test 4 Passed: {}".format(test4_passed))
    print("Test 5 Passed: {}".format(test5_passed))
    
    ### Index tests, negative n_start ###
    test6_yours, _ = your_decaying_expo(5, -4, 217)
    test6_staff = np.arange(-4, 218)
    test6_passed = np.allclose(test6_yours, test6_staff)
    
    test7_yours, _ = your_decaying_expo(np.pi, -1998, 2019)
    test7_staff = np.arange(-1998, 2020)
    test7_passed = np.allclose(test7_yours, test7_staff)
    
    print("\nTesting indices are correct when n_start < 0")
    print("Test 6 Passed: {}".format(test6_passed))
    print("Test 7 Passed: {}".format(test7_passed))
    
    ### Signal tests, negative n_start ###
    _, test8_yours = your_decaying_expo(1, -4, 14)
    test8_staff = np.array([0.0,0.0,0.0,0.0,1.0,0.36787944117144233,0.1353352832366127,0.049787068367863944,0.01831563888873418,0.006737946999085467,0.0024787521766663585,0.0009118819655545162,0.00033546262790251185,0.00012340980408667956,4.5399929762484854e-05,1.670170079024566e-05,6.14421235332821e-06,2.2603294069810542e-06,8.315287191035679e-07])
    test8_passed = np.allclose(test8_staff, test8_yours)
    
    _, test9_yours = your_decaying_expo(.5, -5, 15)
    test9_staff = np.array([0.0,0.0,0.0,0.0,0.0,1.0,0.6065306597126334,0.36787944117144233,0.22313016014842982,0.1353352832366127,0.0820849986238988,0.049787068367863944,0.0301973834223185,0.01831563888873418,0.011108996538242306,0.006737946999085467,0.004086771438464067,0.0024787521766663585,0.0015034391929775724,0.0009118819655545162,0.0005530843701478336])
    test9_passed = np.allclose(test9_staff, test9_yours)
    
    _, test10_yours = your_decaying_expo(4, -6, 16)
    test10_staff = np.array([0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.01831563888873418,0.00033546262790251185,6.14421235332821e-06,1.1253517471925912e-07,2.061153622438558e-09,3.775134544279098e-11,6.914400106940203e-13,1.2664165549094176e-14,2.3195228302435696e-16,4.248354255291589e-18,7.781132241133797e-20,1.4251640827409352e-21,2.6102790696677047e-23,4.780892883885469e-25,8.75651076269652e-27,1.603810890548638e-28])
    test10_passed = np.allclose(test10_staff, test10_yours)
    
    print("\nTesting signal values are correct when n_start < 0")
    print("Test 8 Passed: {}".format(test8_passed))
    print("Test 9 Passed: {}".format(test9_passed))
    print("Test 10 Passed: {}".format(test10_passed))
    
    test_results = np.array([test1_passed, test2_passed, test3_passed, test4_passed, test5_passed, \
                            test6_passed, test7_passed, test8_passed, test9_passed, test10_passed])
    
    print("\n{0} out of {1} tests passed".format(sum(test_results), 10))

def check_passed(true, actual):
    if not len(true) == len(actual) or not np.allclose(true, actual):
        print("correct output: {}".format(true))
        print("your output:    {}".format(actual))
        raise ValueError("Test case failed")

def conv_tests(test_fctn):
    ## Convolving a signal with itself
    sig = [1]
    true, actual = np.convolve(sig, sig, "full"), test_fctn(sig, sig)
    check_passed(true, actual)
    
    sig = [1, 2, 7]
    true, actual = np.convolve(sig, sig, "full"), test_fctn(sig, sig)
    check_passed(true, actual)
    
    sig = [1, -1, 1, -1, 1]
    true, actual = np.convolve(sig, sig, "full"), test_fctn(sig, sig)
    check_passed(true, actual)
   
    sig = np.random.randn(100)
    true, actual = np.convolve(sig, sig, "full"), test_fctn(sig, sig)
    check_passed(true, actual)
    
    ## Convolving two different signals
    sig1 = [1]
    sig2 = [2]
    true, actual = np.convolve(sig1, sig2, "full"), test_fctn(sig1, sig2)
    check_passed(true, actual)
    
    sig1 = [1, 2, 7]
    sig2 = [-3, -4, 0, 0]
    true, actual = np.convolve(sig1, sig2, "full"), test_fctn(sig1, sig2)
    check_passed(true, actual)
    
    sig1 = [1, -1, 1, -1, 1, -1, 1, -1]
    sig2 = [1/2, 1/2]
    true, actual = np.convolve(sig1, sig2, "full"), test_fctn(sig1, sig2)
    check_passed(true, actual)
   
    sig1 = np.random.randn(512)
    sig2 = np.random.randn(256)
    true, actual = np.convolve(sig1, sig2, "full"), test_fctn(sig1, sig2)
    check_passed(true, actual)
    
    print("All tests passed")

def get_speedup(f, g, num_trials=10):
    """
    Report the average speedup time over NUM_TRIALS attempts for convolving 
    two randomly generated length 500 signals using "f", a Python function
    to perform convolution, versus a naive numpyless implementation.
    """
    signal1 = np.random.randn(500)
    signal2 = np.random.randn(500)
    
    your_avg_time, default_avg_time = 0, 0
    for trial in range(num_trials):
        # Time your numpy-based convolution function
        t_start = time.time()
        f(signal1, signal2)
        t_end = time.time()
        your_avg_time += t_end - t_start

        # Time numpy-free convolution
        t_start = time.time()
        g(signal1, signal2)
        t_end = time.time()
        default_avg_time += t_end - t_start
    
    your_avg_time, default_avg_time = your_avg_time / num_trials, default_avg_time / num_trials
    print("Without NumPy: {} sec".format(round(default_avg_time, 4)))
    print("With NumPy:    {} sec".format(round(your_avg_time, 4)))
    print("NumPy gives a {}x speedup".format(round(default_avg_time / your_avg_time, 4)))