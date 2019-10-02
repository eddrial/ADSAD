'''
Created on 16 Jun 2016

@author: gdy32713
'''

import h5py
import numpy as np
#import matplotlib.pyplot as plt

def makeDataNumpyArray(testfile):
    combined = np.vstack((np.array(testfile['s'][:]),np.array(testfile['Bx'][:]),np.array(testfile['Bz'][:]),np.array(testfile['Bs'][:])))
    transposed = np.transpose(combined)
    return transposed

def maxOfData(data):
    return max(data)

def findPeakIndices(data):
    return [i for i, x in enumerate(data) if x > 0.97*maxOfData(data)]

def findPeakPeriodicity(data):
    peakIndices = findPeakIndices(data)
    return peakIndices[1]-peakIndices[0]

def copyOnePeriod(data):
    periodicity = findPeakPeriodicity(data[:,2])
    duplicatesection = data[(len(data)-1)/2:((len(data)-1)/2+periodicity)]
    return duplicatesection

def insertOnePeriod(data):
    duplicated_data = copyOnePeriod(data)
    extended_data = np.insert(data,(len(data)-1)/2,duplicated_data, 0)
    sstep = data[1,0]-data[0,0]
    extended_data[0,0] = data[0,0]-(len(duplicated_data)*sstep)/2
    news00 = data[0,0]-(sstep*len(duplicated_data)/2)
    news = np.arange(news00, -news00, sstep)
    extended_data[:,0] = news[:]
    return extended_data

def insertNPeriods(data,n):
    duplicated_data = copyOnePeriod(data)
    nduplicated_data = np.tile(duplicated_data,(n,1))

    
    
    extended_data = np.insert(data,(len(data)-1)/2,nduplicated_data, 0)
    sstep = data[1,0]-data[0,0]
    extended_data[0,0] = data[0,0]-(len(nduplicated_data)*sstep)/2
    news00 = data[0,0]-(sstep*len(nduplicated_data)/2)
    news = np.arange(news00, -news00, sstep)
    extended_data[:,0] = news[:]
    return extended_data
    
    #extended_data = data
    #for n in np.arange(n):
   #     extended_data = insertOnePeriod(extended_data)
   # return extended_data
        
    