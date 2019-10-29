'''
Created on 29 Oct 2019

@author: oqb
'''
import numpy as np
import matplotlib.pyplot as plt
from aa import data, fetcher, js
from tzlocal import get_localzone
from datetime import datetime


if __name__ == '__main__':
    #Set up archive
    tz = get_localzone()
    ArchiverBessy = 'archiver.bessy.de'
    
    jfetcher_Bessy = js.JsonFetcher(ArchiverBessy,80)
    # gather data on move to create time window
    UE112Gap = 'UE112ID7R:BasePmGap.A'
    UE112Phase = 'UE112ID7R:SBasePmGap.B'
    
    phasestart = tz.localize(datetime(2019, 10, 27, 8 , 25))
    phaseend = tz.localize(datetime(2019, 10, 27, 8, 33))
    
    phasemove = jfetcher_Bessy.get_values(UE112Phase, phasestart, phaseend)
    
    #Have a quick look
    plt.plot(phasemove._timestamps, phasemove._values)
    plt.show()
    
    # set window
    
    #find _values array point wwhere the move starts and stops
    np.
    #set corresponding _timestamps as start and stop
    # gather more data (tune, Box0)
    
    # fit curves
    
    # create fixed x scale
    
    # create tables
    
    # compare tables
    
    #point to stop for debug
    print (phasemove)