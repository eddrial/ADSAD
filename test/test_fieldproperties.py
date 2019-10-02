'''
Created on 11 Aug 2016

@author: gdy32713
'''
import unittest
import numpy as np
from id_analyses import loadbfield as lb
from id_analyses import fieldmanipulation as fm
from id_analyses import fieldproperties as fp


class Test(unittest.TestCase):

    testfile = lb.loadBFieldFromHDF5('CPMUplota1ideal.h5')
    B_Array = fm.makeDataNumpyArray(testfile)
    long_B_Array = fm.insertNPeriods(B_Array, 98)

    def testDefaultMachineProperties(self):
        machineProperties = fp.defineMachineProperties()
        self.assertEqual(machineProperties[0:4], (3.0, 0.0001, 2.9911124e8, 0.511e-3))
        
    def testPhaseErrorIsFloat(self, bfield = long_B_Array):
        (a,b) = fp.fieldPhaseError(bfield)
        self.assertLess(a,100.0)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()