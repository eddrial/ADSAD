'''
Created on 2 Oct 2019

@author: oqb
'''
import unittest
import requests
from ArchiverTool import archiverdefn as ad

class Test(unittest.TestCase):


    def test_ArchiveDefaultName(self):
        testarchive = ad.archiver()
        self.assertEqual(testarchive.archiver_name, 'BESSY')
        
    def test_ArchiveChosenName(self):
        testarchive = ad.archiver("My_Archiver2")
        self.assertEqual(testarchive.archiver_name, 'My_Archiver2')
        
    def test_ArchiveExists(self):
        testarchive = ad.archiver()
        self.assertIsInstance(testarchive, ad.archiver)

    def test_ArchiveOptionsBESSY(self):
        testarchive = ad.archiver()
        self.assertDictContainsSubset({'BESSY':'http://www.bessy.de/archiver/retrieval/'}, testarchive.all_archivers,"Archiver is not in class default list")
        
    
    def test_ArchiveAddressBESSY(self):
        testarchive = ad.archiver()
        self.assertEqual(testarchive.archiver_address, "http://www.bessy.de/archiver/retrieval/", "Archiver address is Wrong")
        
    def test_ArchiveAddressBESSYisLive(self):
        testarchive = ad.archiver()
        r = requests.get(testarchive.archiver_address[:-10],timeout=3)
        self.assertEqual(r.status_code, 200, "BESSY Archiver Appliance Address is Not Working")
        
    
        
            
        
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()