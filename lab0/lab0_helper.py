"""DO NOT CHANGE THIS FILE"""

import numpy as np

def run_tests(decaying_expo):
    num_passed = 0
    
    ### Index tests, non-negative n_start ###
    test1_yours, _ = decaying_expo(.95, 0, 20)
    test1_staff = np.arange(0, 21)
    test1_passed = np.allclose(test1_yours, test1_staff)
    
    test2_yours, _ = decaying_expo(.8, 3, 20)
    test2_staff = np.arange(3, 21)
    test2_passed = np.allclose(test2_yours, test2_staff)
    
    print("Testing indices are correct when n_start >= 0")
    print("Test 1 Passed: {}".format(test1_passed))
    print("Test 2 Passed: {}".format(test2_passed))
    
    ### Signal tests, non-negative n_start ###
    _, test3_yours = decaying_expo(.95, 0, 20)
    test3_staff = np.array([1.0,0.38674102345450123,0.14956861922263506,0.057844320874838484,0.0223707718561656,0.008651695203120634,0.003345965457471275,0.001294022105465849,0.0005004514334406108,0.00019354509955809418,7.48518298877006e-05,2.894827329821157e-05,1.119548484259096e-05,4.329753266092978e-06,1.674493209434269e-06,6.475952175842209e-07,2.504516372327622e-07,9.685992250925397e-08,3.7459705562952584e-08,1.4487204867720514e-08,5.602796437537268e-09])
    test3_passed = np.allclose(test3_staff, test3_yours)
    
    _, test4_yours = decaying_expo(.8, 0, 20)
    test4_staff = np.array([1.0,0.44932896411722156,0.20189651799465538,0.09071795328941247,0.04076220397836621,0.01831563888873418,0.008229747049020023,0.003697863716482929,0.001661557273173934,0.0007465858083766792,0.00033546262790251185,0.0001507330750954765,6.772873649085378e-05,3.0432483008403625e-05,1.3674196065680938e-05,6.14421235332821e-06,2.7607725720371986e-06,1.2404950799567113e-06,5.573903692694596e-07,2.504516372327617e-07,1.1253517471925912e-07])
    test4_passed = np.allclose(test4_staff, test4_yours)
    
    _, test5_yours = decaying_expo(.3, 0, 20)
    test5_staff = np.array([1.0,0.7408182206817179,0.5488116360940265,0.40656965974059917,0.30119421191220214,0.22313016014842982,0.16529888822158656,0.1224564282529819,0.09071795328941251,0.06720551273974978,0.049787068367863944,0.036883167401240015,0.02732372244729257,0.02024191144580439,0.014995576820477703,0.011108996538242306,0.00822974704902003,0.006096746565515638,0.00451658094261267,0.003345965457471272,0.0024787521766663585]) 
    test5_passed = np.allclose(test4_staff, test4_yours)
    
    print("\nTesting signal values are correct when n_start >= 0")
    print("Test 3 Passed: {}".format(test3_passed))
    print("Test 4 Passed: {}".format(test4_passed))
    print("Test 5 Passed: {}".format(test5_passed))
    
    ### Index tests, negative n_start ###
    test6_yours, _ = decaying_expo(5, -4, 217)
    test6_staff = np.arange(-4, 218)
    test6_passed = np.allclose(test6_yours, test6_staff)
    
    test7_yours, _ = decaying_expo(np.pi, -1998, 2019)
    test7_staff = np.arange(-1998, 2020)
    test7_passed = np.allclose(test7_yours, test7_staff)
    
    print("\nTesting indices are correct when n_start < 0")
    print("Test 6 Passed: {}".format(test6_passed))
    print("Test 7 Passed: {}".format(test7_passed))
    
    ### Signal tests, negative n_start ###
    _, test8_yours = decaying_expo(1, -4, 14)
    test8_staff = np.array([0.0,0.0,0.0,0.0,1.0,0.36787944117144233,0.1353352832366127,0.049787068367863944,0.01831563888873418,0.006737946999085467,0.0024787521766663585,0.0009118819655545162,0.00033546262790251185,0.00012340980408667956,4.5399929762484854e-05,1.670170079024566e-05,6.14421235332821e-06,2.2603294069810542e-06,8.315287191035679e-07])
    test8_passed = np.allclose(test8_staff, test8_yours)
    
    _, test9_yours = decaying_expo(.5, -5, 15)
    test9_staff = np.array([0.0,0.0,0.0,0.0,0.0,1.0,0.6065306597126334,0.36787944117144233,0.22313016014842982,0.1353352832366127,0.0820849986238988,0.049787068367863944,0.0301973834223185,0.01831563888873418,0.011108996538242306,0.006737946999085467,0.004086771438464067,0.0024787521766663585,0.0015034391929775724,0.0009118819655545162,0.0005530843701478336])
    test9_passed = np.allclose(test9_staff, test9_yours)
    
    _, test10_yours = decaying_expo(4, -6, 16)
    test10_staff = np.array([0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.01831563888873418,0.00033546262790251185,6.14421235332821e-06,1.1253517471925912e-07,2.061153622438558e-09,3.775134544279098e-11,6.914400106940203e-13,1.2664165549094176e-14,2.3195228302435696e-16,4.248354255291589e-18,7.781132241133797e-20,1.4251640827409352e-21,2.6102790696677047e-23,4.780892883885469e-25,8.75651076269652e-27,1.603810890548638e-28])
    test10_passed = np.allclose(test10_staff, test10_yours)
    
    print("\nTesting signal values are correct when n_start < 0")
    print("Test 8 Passed: {}".format(test8_passed))
    print("Test 9 Passed: {}".format(test9_passed))
    print("Test 10 Passed: {}".format(test10_passed))
    
    test_results = np.array([test1_passed, test2_passed, test3_passed, test4_passed, test5_passed, \
                            test6_passed, test7_passed, test8_passed, test9_passed, test10_passed])
    
    print("\n{0} out of {1} tests passed".format(sum(test_results), 10))