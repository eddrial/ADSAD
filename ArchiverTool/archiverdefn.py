'''
Created on 30 Sep 2019

@author: oqb
'''

class archiver():
    '''
    classdocs
    '''


    def __init__(self, name = 'BESSY'):
        '''
        Constructor
        '''
        self.archivername = name
        
        self.all_archivers = {'BESSY':'http://www.bessy.de/archiver/'}
    