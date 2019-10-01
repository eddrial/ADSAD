'''
Created on 30 Sep 2019

@author: oqb
'''
import unittest
import archive1.archive1a as ac

class Test(unittest.TestCase):


    def testconstructor(self):
        testarchive = ac.archiver_ed()
        self.assertEqual(testarchive.myname, 'My_Archiver')
        
    def testconstructor2(self):
        testarchive = ac.archiver_ed()
        self.assertEqual(testarchive.myname, 'My_Archiver2')
        
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()