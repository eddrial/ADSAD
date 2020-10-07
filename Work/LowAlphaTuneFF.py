'''
Created on 29 Oct 2019

@author: oqb
'''
import numpy as np
import matplotlib.pyplot as plt
from aa import data, fetcher, js
from tzlocal import get_localzone
from datetime import datetime
from scipy.signal import savgol_filter
from scipy import interpolate


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
    
    Vtunetarget = 979.0
    Htunetarget = 882.0
    THztarget = 1
    
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
    datastopindex = np.argmin(tmpphasediff[datastartindex:]>1e-4)+2
    #Local Timestamps for TuneH, Tune V and Box0
    phasemovestart = tz.localize(datetime.fromtimestamp((phasemove._timestamps[datastartindex]))) #start a second before
    phasemoveend = tz.localize(datetime.fromtimestamp((phasemove._timestamps[datastopindex]+1))) #finish a second after
    # gather more data (tune, Box0)
    tuneHdata =  jfetcher_Bessy.get_values(tuneH, phasemovestart, phasemoveend)
    tuneVdata = jfetcher_Bessy.get_values(tuneV, phasemovestart, phasemoveend)
    THzbox0data = jfetcher_Bessy.get_values(THzbox0, phasemovestart, phasemoveend)
    
    
    
    
    
    #gather data for detrending THz signal
    THzdetrendstart = tz.localize(datetime(2019, 10, 27, 8 , 14))
    THzdetrendend = tz.localize(datetime(2019, 10, 27, 8 , 24))
    THztrenddata = jfetcher_Bessy.get_values(THzbox0, THzdetrendstart, THzdetrendend)
    
    #create linear fit
    THztargetfit = np.polyfit(THztrenddata._timestamps, THztrenddata._values[:,0], 1)
    print(THztargetfit)
    THztarget = np.poly1d(THztargetfit)
    
    FMN = THzbox0data._values-THztarget(THzbox0data._timestamps)
    
    plt.figure()
    plt.plot(tuneHdata._timestamps, tuneHdata._values-np.mean(tuneHdata._values))
    plt.plot(tuneVdata._timestamps, tuneVdata._values-np.mean(tuneVdata._values))
    plt.plot(THzbox0data._timestamps, 500*(FMN))
    
    
    plt.show()
    # fit curves
    #fit gap curve also with time
    #(VTune determine main oscillation frequency and strip it out?) Worth looking at? Or comes out in the fit wash?
    #THz tune number remove linear fit from first to final point CAN ONLY BE DONE AFTER BOTH WAYS LOOKED AT OR LINEAR FIT FROM PREVIOUS MOTION FREE TIMES USED
    #HTune Smooth
    smTuneHData = savgol_filter(tuneHdata._values[:,0], 5, 2)
    #VTune Smooth
    smTuneVData = savgol_filter(tuneVdata._values[:,0], 51, 2)
    #THz Smooth
    smTHzData = savgol_filter(THzbox0data._values[:,0], 151, 2)
    tmp2 = savgol_filter(FMN, 151, 2)
    
    ###Here be fits
    xnew = np.linspace(phasemove._timestamps[datastartindex], (phasemove._timestamps[datastopindex]), 51)
    
    #Htune Fit
    #Htune = np.linspace(phasemove._timestamps[datastartindex], phasemove._timestamps[datastopindex], len(smTuneHData))
    tckHtune = interpolate.splrep(np.linspace(phasemove._timestamps[datastartindex], phasemove._timestamps[datastopindex], len(smTuneHData)),smTuneHData, s=0.0)
    Htunefit = interpolate.splev(xnew, tckHtune, der=0)
    
    plt.figure()
    plt.plot(tuneHdata._timestamps, tuneHdata._values,tuneHdata._timestamps, smTuneHData, xnew, Htunefit)
    #plt.plot(tuneHdata._timestamps, smTuneHData)
    
    plt.show()
    
    #Vtune Fit
    tckVtune = interpolate.splrep(np.linspace(phasemove._timestamps[datastartindex], phasemove._timestamps[datastopindex], len(smTuneVData)),smTuneVData, s=0.0)
    Vtunefit = interpolate.splev(xnew, tckVtune, der=0)
    
    plt.figure()
    plt.plot(tuneVdata._timestamps, tuneVdata._values,tuneVdata._timestamps, smTuneVData, xnew, Vtunefit)
    
    plt.show()
    
    
    #THz Fit   
    tckTHz = interpolate.splrep(np.linspace(phasemove._timestamps[datastartindex], phasemove._timestamps[datastopindex], len(smTHzData)),smTHzData, s=0.0)
    THzfit = interpolate.splev(xnew, tckTHz, der=0)    
    
    
    plt.figure()
    plt.plot(THzbox0data._timestamps, THzbox0data._values,THzbox0data._timestamps, smTHzData,xnew, THzfit)
    
    plt.show()
    
    #Gap Fit
    #TODO Needs Improving
    tckGap = interpolate.splrep(np.linspace(phasemove._timestamps[datastartindex], phasemove._timestamps[datastopindex], len(phasemove._values[datastartindex:datastopindex])),phasemove._values[datastartindex:datastopindex], s=0.0)
    Gapfit = interpolate.splev(xnew, tckGap, der=0) 
    
    plt.figure()
    plt.plot(phasemove._timestamps[datastartindex:datastopindex], phasemove._values[datastartindex:datastopindex],xnew, Gapfit)
    
    plt.show()
    
    # create tables
    #Bring fitted lines together
    gapresponse = np.transpose(np.vstack((Gapfit, Htunefit-Htunetarget, Vtunefit-Vtunetarget, THzfit)))
    
    #Create inverse matrix
    responsematrix = np.transpose([[35.75,67.5, 600],[-157.3, -22.5, -22.75], [121,207.5, 190.5]])
    invresponse = np.linalg.inv(responsematrix)
    print (np.asmatrix(responsematrix))
    print(invresponse)
    
    print(np.dot(invresponse,np.transpose(-gapresponse[50,1:])))
    
    
    #create quadrupole array solution.
    quadoffsets = np.zeros(gapresponse.shape)
    quadoffsets[:,0] = gapresponse[:,0]
    quadoffsets[:,1:]=np.transpose(np.dot(invresponse,np.transpose(-gapresponse[:,1:])))
    
    #export tables in expected form..
    
    #make a quadrupole array solution based on existing points and linear interpolation
    # compare tables
    
    #point to stop for debug
    print (quadoffsets)
