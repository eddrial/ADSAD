'''
Created on 2 Oct 2019

@author: oqb
'''
import unittest
from ArchiverTool import archiverdefn as ad

class Test(unittest.TestCase):


    def testconstructor(self):
        testarchive = ad.archiver_ed()
        self.assertEqual(testarchive.myname, 'My_Archiver')
        
    def testconstructor2(self):
        testarchive = ad.archiver_ed("My_Archiver2")
        self.assertEqual(testarchive.myname, 'My_Archiver2')
        
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()