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


    def __init__(self, params):
        '''
        Constructor
        '''
        