'''
Created on 2 Oct 2019

@author: oqb
'''
import unittest
from ArchiverTool import archiverdefn as ad

class Test(unittest.TestCase):


    def test_ArchiveDefaultName(self):
        testarchive = ad.archiver()
        self.assertEqual(testarchive.archivername, 'BESSY')
        
    def test_ArchiveChosenName(self):
        testarchive = ad.archiver("My_Archiver2")
        self.assertEqual(testarchive.archivername, 'My_Archiver2')
        
    def test_ArchiveExists(self):
        testarchive = ad.archiver()
        self.assertIsInstance(testarchive, ad.archiver)

    def test_ArchiveOptions(self):
        testarchive = ad.archiver()
        self.assertDictContainsSubset({'BESSY':'http://www.bessy.de/archiver/'}, testarchive.all_archivers,"Archiver is not in class default list")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()