import numpy as np
import pylab as py
import matplotlib.pyplot as plt
import math as m
import scipy.signal as sig

def derive_dot(y,cf,lcf,rcf,h):
    """ Calculates the derivative using the dot product.
        :param y: The y values of the of the discretized function with step a size of h.
        :param cf: The center function coefficients and indexes. 
            Expects a 2xN array. Where row one contains the coefficients and row two contains the 
            the relative indexes to access y. 
        :param lcf: The left side function. Just as with cf expects two rows. the first containing the 
            coefficients and the second containing the indexes. 
        :param rcf: The right side function. Just as with cf expects two rows. 
        :param h: The h value as an array. The first index is the h size, the second is the 
            coefficient to multiply h by. The third is the power to raise h. 
            e.x. [h, c, b] => c * h^b
    """
    cf=np.array(cf).astype(float)
    lcf=np.array(lcf).astype(float)
    rcf=np.array(rcf).astype(float)
    h=np.array(h).astype(float)
    
    starti=int(cf[1][0])
    stopi=int(cf[1][-1])

 
    out=[]
    # Right differential 
    for i in range(0, np.abs(starti)):
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
    for i in range(len(y) - stopi, len(y)):
        indexes = np.array(lcf[1]).astype(int) + i
        y_s = y[indexes]
        dydx=1/(h[1]*(h[0]**h[2]))*np.dot(y_s,lcf[0])
        out.append(dydx)
    
    return out

def derive_conv(y,cf,lcf,rcf,h):
    """ Calculates the derivative using the scipy.signal.convolve.
        :param y: The y values of the of the discretized function with step a size of h.
        :param cf: The center function coefficients and indexes. 
            Expects a 2xN array. Where row one contains the coefficients and row two contains the 
            the relative indexes to access y. 
        :param lcf: The left side function. Just as with cf expects two rows. the first containing the 
            coefficients and the second containing the indexes. 
        :param rcf: The right side function. Just as with cf expects two rows. 
        :param h: The h value as an array. The first index is the h size, the second is the 
            coefficient to multiply h by. The third is the power to raise h. 
            e.x. [h, c, b] => c * h^b
    """
    cf=np.array(cf).astype(float)
    lcf=np.array(lcf).astype(float)
    rcf=np.array(rcf).astype(float)
    h=np.array(h).astype(float)

    # Center differential
    starti=int(cf[1][0])
    stopi=int(cf[1][-1])
    
    out=np.array([])

    # Right differential 
    for i in range(0, np.abs(starti)):
        indexes = np.array(rcf[1]).astype(int) + i
        y_s = np.array(y[indexes])
        dydx=1/(h[1]*(h[0]**h[2]))*np.dot(y_s,rcf[0])
        out = np.append(out, dydx)
   
    # Center differential
    conv=np.array(sig.convolve(y,cf[0],'valid'))
    dydx=(1/(h[1]*(h[0]**h[2])))*conv
    out = np.append(out, dydx)
    
    # Left-hand differential 
    for i in range(len(y) - stopi, len(y)):
        indexes = np.array(lcf[1]).astype(int) + i
        y_s = y[indexes]
        dydx=1/(h[1]*(h[0]**h[2]))*np.dot(y_s,lcf[0])
        out = np.append(out, dydx)
    
    return out

