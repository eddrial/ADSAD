'''
Created on 16 Jun 2016

@author: gdy32713
'''
import unittest
import numpy as np
from id_analyses import loadbfield as lb
from id_analyses import fieldmanipulation as fm


class Test(unittest.TestCase):
    
    testfile = lb.loadBFieldFromHDF5('CPMUplota1ideal.h5')
    B_Array = fm.makeDataNumpyArray(testfile)
    
    
    def testHDF5GoesToArray(self, file = testfile):
        B_Array = fm.makeDataNumpyArray(file)
        self.assertEqual(np.shape(B_Array), (801L,4L))
    
    def testBzValuesGreaterThanBxValues(self,data = testfile):
        Bzmax = fm.maxOfData(data['Bz'][:])
        Bxmax = fm.maxOfData(data['Bx'][:])
        self.assertGreater(Bzmax, Bxmax)
        
    def testBzValuesGreaterThanBsValues(self,data = testfile):
        Bzmax = fm.maxOfData(data['Bz'][:])
        Bsmax = fm.maxOfData(data['Bs'][:])
        self.assertGreater(Bzmax, Bsmax)
        
    
    def testMaxValueCorrect(self,data = testfile):
        Bzmax = fm.maxOfData(data['Bz'][:])
        self.assertGreater(Bzmax, 1.23)
        
    def testNumberOfPeaksInTest(self, data = testfile):
        numberOfPeaks = len(fm.findPeakIndices(data['Bz'][:]))
        self.assertEqual(numberOfPeaks, 16)
        
    def testPeakPeriodicity(self, data = testfile):
        peakPeriodicity = fm.findPeakPeriodicity(data['Bz'][:])
        self.assertEqual(peakPeriodicity, 20)
        
    def testCopiedDataIsOnePeriod(self, data = B_Array):
        duplicatePeriod = fm.copyOnePeriod(data)
        self.assertEqual(len(duplicatePeriod), 20)
        
    def testNonIdenticalNeighbouringBzPoints(self, data = B_Array):
        for i in np.arange(len(data)-1):
            self.assertNotEqual(data[i,2], data[i+1,2])
    
    def testArrayLengthIncreaseBy20UponInsertion(self, data = B_Array):
        extended_B_Array = fm.insertOnePeriod(data)
        self.assertEqual(len(extended_B_Array), len(data)+20)
    
    def testMultipleIncreases(self, data = B_Array, n=17):
        extended_B_Array = fm.insertNPeriods(data, n)
        self.assertEqual(len(extended_B_Array), len(data)+n*20)
        
    def testMultipleIncreasesHandlesSCorrectly(self, data = B_Array, n=107):
        extended_B_Array = fm.insertNPeriods(data, n)
        self.assertAlmostEqual(-extended_B_Array[-1,0], extended_B_Array[0,0], delta = 0.00001)
    
    def testSStepIsRegular(self, data = B_Array):
        extended_B_Array = fm.insertOnePeriod(data)
        sstep = data[1,0]-data[0,0]
        for i in np.arange(len(extended_B_Array)-1):
            self.assertAlmostEqual(extended_B_Array[i+1,0], extended_B_Array[i,0]+sstep, delta=0.0001)
            
    def testSStartAfterInsertion(self, data = B_Array):
        extended_B_Array = fm.insertOnePeriod(data)
        self.assertAlmostEqual(-360.8, extended_B_Array[0,0],delta = 0.001)
        
    def testSstartisminusSendAfterInsertion(self, data = B_Array):
        extended_B_Array = fm.insertOnePeriod(data)
        self.assertAlmostEqual(-extended_B_Array[-1,0], extended_B_Array[0,0],delta = 0.001)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()