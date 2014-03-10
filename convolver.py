import numpy as np
import pylab as py
import matplotlib.pyplot as plt
import math as m
import scipy.signal as sig

    #[[coeffs],[index offset]]
###############################################################
    #first derivative h^2(2h)
##    cf12=[[-1,1],[-1,1]]
##    lcf12=[[1,-4,3],[-2,-1,0]]
##    rcf12=[[-3,4,-1],[0,1,2]]
##    #first derivative h^4(12h)
##    cf14=[[1,-8,8,-1],[-2,-1,1,2]]
##    lcf14=[[3,-16,36,-48,25],[-4,-3,-2,-1,0]]
##    rcf14=[[-25,48,-36,16,-3],[0,1,2,3,4]]
##    #first derivative h^6(60h)
##    cf16=[[-1,9,-45,45,-9,1],[-3,-2,-1,1,2,3]]
##    lcf16=[[10,-72,225,-400,450,-360,147],[-6,-5,-4,-3,-2,-1,0]]
##    rcf16=[[-147,360,-450,400,-225,72,-10],[0,1,2,3,4,5,6]]
####################################################################
##    #Second Derivative h^2(h^2)
##    cf22=[[1,-2,1],[-1,0,1]]
##    lcf22=[[-1,4,-5,2],[-3,-2,-1,0]]
##    rcf22=[[2,-5,4,-1],[0,1,2,3]]
##    #second derivative h^4 (12h^2)
##    cf24=[[-1,16,-30,16,-1],[-2,-1,0,1,2]]
##    lcf24=[[-10,61,-156,214,-154,45],[-5,-4,-3,-2,-1,0]]
##    rcf24=[[45,-154,214,-156,61,-10],[0,1,2,3,4,5]]
##    #second derivative h^6 (180h^2)
##    cf26=[[2,-27,270,-490,270,-27,2],[-3,-2,-1,0,1,2,3]]
##    lcf26=[[-126,1019,-3618,7380,-9490,7911,-4014,938],[-7,-6,-5,-4,-3,-2,-1,0]]
##    rcf26=[[938,-4014,7911,-9490,7380,-3618,1019,-126],[0,1,2,3,4,5,6,7]]
################################################################################
def derive(y,cf,lcf,rcf,h):
    cf=np.array(cf).astype(float)
    lcf=np.array(lcf).astype(float)
    rcf=np.array(rcf).astype(float)
    h=np.array(h).astype(float)
    
    starti=int(cf[1][0])
    stopi=int(cf[1][-1])

 
    out=[]
    for i in range(0, np.abs(starti)):
        #print i
        indexes = np.array(rcf[1]).astype(int) + i
        y_s = np.array(y[indexes])
        dydx=1/(h[1]*(h[0]**h[2]))*np.dot(y_s,rcf[0])
        out.append(dydx)

    # Center differential
    for i in range(abs(starti),len(y)-stopi,1):
        indexes = np.array(cf[1]).astype(int) + i
        y_s = np.array(y[indexes])
        dydx=1/(h[1]*(h[0]**h[2]))*np.dot(y_s,cf[0])
        out.append(dydx)
    
    # Left differential
    #print len(y)
    for i in range(len(y) - stopi, len(y)):
        #print i
        indexes = np.array(lcf[1]).astype(int) + i
        y_s = y[indexes]
        dydx=1/(h[1]*(h[0]**h[2]))*np.dot(y_s,lcf[0])
        out.append(dydx)
    
    return out

def derive2(y,cf,lcf,rcf,h):
    cf=np.array(cf).astype(float)
    lcf=np.array(lcf).astype(float)
    rcf=np.array(rcf).astype(float)
    h=np.array(h).astype(float)
    
    out=[]

    # Right-hand differential
    indexes = np.array(rcf[1]).astype(int)
    y_s = np.array(y[indexes])
    conv=np.array(sig.convolve(y_s,rcf[0],'valid'))
    dydx=(1/(h[1]*(h[0]**h[2])))*conv
    out.append(-1*np.sum(dydx))
    
    # Center differential
    starti=int(cf[1][0])
    stopi=int(cf[1][-1])
    for i in range(abs(starti),len(y)-stopi,1):
        indexes = np.array(cf[1]).astype(int) + i
        y_s = np.array(y[indexes])
        conv=np.array(sig.convolve(y_s,cf[0],'valid'))
        dydx=(1/(h[1]*(h[0]**h[2])))*conv
        out.append(-1*np.sum(dydx))
    
    # Left-hand differential 
    indexes = np.array(lcf[1]).astype(int)+(len(y)-1)
    y_s = y[indexes]
    conv=sig.convolve(y_s,lcf[0],'valid')
    dydx=(1/(h[1]*(h[0]**h[2])))*conv
    out.append(-1*np.sum(dydx))
    
    return out

