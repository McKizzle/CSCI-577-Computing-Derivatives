#!/usr/bin/env python
import derivative as drvt
import Convolver as dcnv
import numpy as np
import matplotlib.pyplot as plt


def main():
    steps = 1000.0
    dt = 2 * np.pi / steps
    t_0 = 0.0
    #first derivative h^4(12h)
    cf=[[-1,1],[-1,1]]
    lcf=[[1,-4,3],[-2,-1,0]]
    rcf=[[-3,4,-1],[0,1,2]]
    h = [dt, 2, 1]
    first_derivative_h2 = drvt.Derivative(dcnv.derive, [cf, lcf, rcf, h])
    #first derivative h^4(12h)
    cf=[[1,-8,8,-1],[-2,-1,1,2]]
    lcf=[[3,-16,36,-48,25],[-4,-3,-2,-1,0]]
    rcf=[[-25,48,-36,16,-3],[0,1,2,3,4]]
    h = [dt, 12, 1]
    first_derivative_h4 = drvt.Derivative(dcnv.derive, [cf, lcf, rcf, h])
    #first derivative h^6(60h)
    cf=[[-1,9,-45,45,-9,1],[-3,-2,-1,1,2,3]]
    lcf=[[10,-72,225,-400,450,-360,147],[-6,-5,-4,-3,-2,-1,0]]
    rcf=[[-147,360,-450,400,-225,72,-10],[0,1,2,3,4,5,6]]
    h = [dt, 60, 1]
    first_derivative_h6 = drvt.Derivative(dcnv.derive, [cf, lcf, rcf, h])
    ##################################################################
    #Second Derivative h^2(h^2)
    cf=[[1,-2,1],[-1,0,1]]
    lcf=[[-1,4,-5,2],[-3,-2,-1,0]]
    rcf=[[2,-5,4,-1],[0,1,2,3]]
    h = [dt, 1, 2]
    second_derivative_h2 = drvt.Derivative(dcnv.derive, [cf, lcf, rcf, h])
    #second derivative h^4 (12h^2)
    cf=[[-1,16,-30,16,-1],[-2,-1,0,1,2]]
    lcf=[[-10,61,-156,214,-154,45],[-5,-4,-3,-2,-1,0]]
    rcf=[[45,-154,214,-156,61,-10],[0,1,2,3,4,5]]
    h = [dt, 12, 2]
    second_derivative_h4 = drvt.Derivative(dcnv.derive, [cf, lcf, rcf, h])
    #second derivative h^6 (180h^2)
    cf=[[2,-27,270,-490,270,-27,2],[-3,-2,-1,0,1,2,3]]
    lcf=[[-126,1019,-3618,7380,-9490,7911,-4014,938],[-7,-6,-5,-4,-3,-2,-1,0]]
    rcf=[[938,-4014,7911,-9490,7380,-3618,1019,-126],[0,1,2,3,4,5,6,7]]
    h = [dt, 180, 2]
    second_derivative_h6 = drvt.Derivative(dcnv.derive, [cf, lcf, rcf, h])
    ###################################################################
    
    out = first_derivative_h2.derive(np.sin, t_0, steps)
    times=np.arange(0, 2 * np.pi, dt)
    print len(times)
    print len(out)
    plt.plot(times, out, 'r')
    plt.show()
    
    return 0

def derive(y, cf, lcf, rcf, h):
    print "------------------------------------------------"
    print y
    print cf
    print lcf
    print rcf
    print h
    return 0

def arrify(f, start_x, h, length):
    return np.array([f(start_x + h * i) for i in range(0, length)])

if __name__ == '__main__':
    main()

