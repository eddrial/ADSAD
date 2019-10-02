'''
Created on 16 Jun 2016

@author: gdy32713
'''
import unittest
from id_analyses import loadbfield as lb

class Test(unittest.TestCase):


    def testIsHDF5File(self):
        f = lb.loadBFieldFromHDF5('CPMUplota1ideal.h5')
        self.assertNotEqual(None, f, "File is not of the correct Type")
        #self.assertEqual('<HDF5 object reference>',f.ref,"File is not of the correct Type")
        
    def testLoadedFileContainsBs(self):
        f = lb.loadBFieldFromHDF5('CPMUplota1ideal.h5')
        self.assertIn('Bs', f.keys())
        
    def testLoadedFileContainsBx(self):
        f = lb.loadBFieldFromHDF5('CPMUplota1ideal.h5')
        self.assertIn('Bx', f.keys())
        
    def testLoadedFileContainsBz(self):
        f = lb.loadBFieldFromHDF5('CPMUplota1ideal.h5')
        self.assertIn('Bz', f.keys())
        
    def testLoadedFileContainss(self):
        f = lb.loadBFieldFromHDF5('CPMUplota1ideal.h5')
        self.assertIn('s', f.keys())
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testIsHDF5File']
    unittest.main()