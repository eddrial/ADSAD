'''
Created on 15 Oct 2019

Class for fetching data over multiple timespans and multiple PVs from the Archiver Appliance using the js fetcher

@author: Ed Rial
'''

from aa import data, fetcher, js

class MultiJsonFetcher(object):
    '''
    classdocs
    '''


    def __init__(self, pvs = None, times = None, bin_length = None):
        '''
        Constructor
        '''
        if pvs is None:
            self.pvs = []
        elif pvs is not list:
            self.pvs = [pvs]
        else:
            self.pvs = pvs
        
        if times is None:
            self.times = []
        else: 
            self.times = times
        self.bin_length = bin_length