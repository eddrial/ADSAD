'''
Created on 15 Oct 2019

@author: oqb
'''
import unittest
from ArchiverTool import multifetcher as mf


class Test(unittest.TestCase):


    def testName(self):
        pass

    def testMultifetcherInits(self):
        multifetcher = mf.MultiJsonFetcher()
        self.assertIsInstance(multifetcher, mf.MultiJsonFetcher())

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()