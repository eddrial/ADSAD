'''
Created on 16 Jun 2016

@author: gdy32713
'''
import h5py
import inspect
import os

def loadBFieldFromHDF5(name):
    path = inspect.stack()[0][1]
    filepath =  '/'.join(os.path.split(path)[0].split(os.sep)[:-1] +
                    ['data', name])
    
    f=h5py.File(filepath,'r')
    
    return f
