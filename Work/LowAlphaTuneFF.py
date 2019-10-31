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
    
    tuneH = 'TUNEZR:rdH'
    tuneV =  'TUNEZR:rdV'
    THzbox0 = 'THZH11FD6L:BOX0'
    
    
    toistart = tz.localize(datetime(2019, 10, 27, 8 , 25))
    toiend = tz.localize(datetime(2019, 10, 27, 8, 33))
    
    phasemove = jfetcher_Bessy.get_values(UE112Phase, toistart, toiend)
    
    #Have a quick look
    plt.plot(phasemove._timestamps, phasemove._values)
    plt.show()
    
    # set window
    
    #find _values array point wwhere the move starts and stops #can be wrapped up
    #find the stepsize of value array
    tmpphasediff = np.diff(phasemove._values[:,0])
    #create a True/False array of 'real steps' i.e. above 0.1 micron. Find the first true
    datastartindex = np.argmax(tmpphasediff>1e-4)+1
    #find the first false after the first true
    datastopindex = np.argmin(tmpphasediff[datastartindex:]>1e-4)+1
    #Local Timestamps for TuneH, Tune V and Box0
    phasemovestart = tz.localize(datetime.fromtimestamp((phasemove._timestamps[datastartindex])))
    phasemoveend = tz.localize(datetime.fromtimestamp((phasemove._timestamps[datastopindex])))
    # gather more data (tune, Box0)
    tuneHdata =  jfetcher_Bessy.get_values(tuneH, phasemovestart, phasemoveend)
    tuneVdata = jfetcher_Bessy.get_values(tuneV, phasemovestart, phasemoveend)
    THzbox0data = jfetcher_Bessy.get_values(THzbox0, phasemovestart, phasemoveend)
    
    plt.figure()
    plt.plot(tuneHdata._timestamps, tuneHdata._values-np.mean(tuneHdata._values))
    plt.plot(tuneVdata._timestamps, tuneVdata._values-np.mean(tuneVdata._values))
    plt.plot(THzbox0data._timestamps, 500*(THzbox0data._values-np.mean(THzbox0data._values)))
    
    
    plt.show()
    
    # fit curves
    #(VTune determine main oscillation frequency and strip it out?) Worth looking at? Or comes out in the fit wash?
    #THz tune number remove linear fit from first to final point CAN ONLY BE DONE AFTER BOTH WAYS LOOKED AT OR LINEAR FIT FROM PREVIOUS MOTION FREE TIMES USED
    
    
    plt.figure()
    
    
    # create fixed x scale
    
    # create tables
    
    # compare tables
    
    #point to stop for debug
    print (phasemove)
    print (phasemovestart)
    print (phasemoveend)
    print (tuneHdata)
    print (tuneVdata)
    print (THzbox0data)