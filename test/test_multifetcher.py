'''
Created on 15 Oct 2019

@author: oqb
'''
import unittest
from ArchiverTool import multifetcher as mf
from builtins import list


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
        if multifetcher.times is list:
            for time in multifetcher.times:
                self.assertIsInstance(multifetcher.times[time], tuple, "Time " + multifetcher.times[time] + " is not a tuple")
            
    def testBinLengthSuitable(self):
        multifetcher = mf.MultiJsonFetcher()
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()