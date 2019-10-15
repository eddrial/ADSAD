'''
Created on 15 Oct 2019

@author: oqb
'''
import unittest
from ArchiverTool import multifetcher as mf
from datetime import datetime
from tzlocal import get_localzone
from aa import js


class Test(unittest.TestCase):


    def testName(self):
        pass

    def testMultifetcherInits(self):
        multifetcher = mf.MultiJsonFetcher()
        self.assertIsInstance(multifetcher, mf.MultiJsonFetcher)
        
    def testPVsInMultiFetcherIsList(self):
        multifetcher = mf.MultiJsonFetcher()
        self.assertIsInstance(multifetcher.pvs, list, "PVs are not as list")
        
    def testTimesAreList(self):
        multifetcher = mf.MultiJsonFetcher()
        self.assertIsInstance(multifetcher.times, list, "times are not as list")
        
    def testTimesAreLength2Tuples(self):
        multifetcher = mf.MultiJsonFetcher()
        if isinstance(multifetcher.times, list):
            for time in multifetcher.times:
                self.assertIsInstance(time, tuple, "Time " + str(time) + " is not a tuple")
                
    def testTimesAreLength2TuplesA(self):
        tz = get_localzone()
        startA = tz.localize(datetime(2019, 5, 2,14))
        endA = tz.localize(datetime(2019, 5, 2, 15))
        startB = tz.localize(datetime(2019, 5, 2,16))
        endB = tz.localize(datetime(2019, 5, 2, 17))
        
        multifetcher = mf.MultiJsonFetcher(times=[(startA,endA),(startB,endB)])
        if isinstance(multifetcher.times, list):
            for key in multifetcher.times:
                for time in key:
                    self.assertIsInstance(time, datetime, "Time " + str(time) + " is not a datetime object")
                
    def testTimesAreDatetimes(self):
        pass
        
            
    def testBinLengthSuitable(self):
        multifetcher = mf.MultiJsonFetcher()
        self.assertIsInstance(multifetcher.bin_length, int, "Bin_Length must be an int")
        multifetcher = mf.MultiJsonFetcher(bin_length=1.5)
        self.assertIsInstance(multifetcher.bin_length, int, "Bin_Length must be an int")
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()