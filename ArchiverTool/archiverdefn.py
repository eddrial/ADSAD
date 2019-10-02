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
        self.archiver_name = name
        
        self.all_archivers = {'BESSY':'http://www.bessy.de/archiver/retrieval/'}
        
        if self.archiver_name == 'BESSY':
            self.archiver_address = self.all_archivers['BESSY']
            
        
    