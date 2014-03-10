#!/usr/bin/env python
import derivative as drvt
import convolver as dcnv
import numpy as np
import matplotlib.pyplot as plt


def main():
    steps = 1000.0
    dx = 2 * np.pi / steps
    x_0 = 0.0 
    x_max = 4 * np.pi # to avoid indexing issues in the derivatibve function. 
    f = np.sin
    derivatives = []

    first_derivatives = {}
    second_derivatives = {}
    plt_styles = { 
            "h^2" : 'ko',
            "h^4" : 'ro',
            "h^6" : 'go'
            }


    # First Derivatives
    cf=[[-1,1],[-1,1]]
    lcf=[[1,-4,3],[-2,-1,0]]
    rcf=[[-3,4,-1],[0,1,2]]
    h = [dx, 2, 1]
    first_derivatives['h^2'] = [cf, lcf, rcf, h]
    
    cf=[[1,-8,8,-1],[-2,-1,1,2]]
    lcf=[[3,-16,36,-48,25],[-4,-3,-2,-1,0]]
    rcf=[[-25,48,-36,16,-3],[0,1,2,3,4]]
    h = [dx, 12, 1]
    first_derivatives['h^4'] = [cf, lcf, rcf, h]
    
    cf=[[-1,9,-45,45,-9,1],[-3,-2,-1,1,2,3]]
    lcf=[[10,-72,225,-400,450,-360,147],[-6,-5,-4,-3,-2,-1,0]]
    rcf=[[-147,360,-450,400,-225,72,-10],[0,1,2,3,4,5,6]]
    h = [dx, 60, 1]
    first_derivatives['h^6'] = [cf, lcf, rcf, h]
    
    # Second Derivatives 
    cf=[[1,-2,1],[-1,0,1]]
    lcf=[[-1,4,-5,2],[-3,-2,-1,0]]
    rcf=[[2,-5,4,-1],[0,1,2,3]]
    h = [dx, 1, 2]
    second_derivatives['h^2'] = [cf, lcf, rcf, h]
    
    cf=[[-1,16,-30,16,-1],[-2,-1,0,1,2]]
    lcf=[[-10,61,-156,214,-154,45],[-5,-4,-3,-2,-1,0]]
    rcf=[[45,-154,214,-156,61,-10],[0,1,2,3,4,5]]
    h = [dx, 12, 2]
    second_derivatives['h^4'] = [cf, lcf, rcf, h]
    
    cf=[[2,-27,270,-490,270,-27,2],[-3,-2,-1,0,1,2,3]]
    lcf=[[-126,1019,-3618,7380,-9490,7911,-4014,938],[-7,-6,-5,-4,-3,-2,-1,0]]
    rcf=[[938,-4014,7911,-9490,7380,-3618,1019,-126],[0,1,2,3,4,5,6,7]]
    h = [dx, 180, 2]
    second_derivatives['h^6'] = [cf, lcf, rcf, h]
        
    print "First derivative of sin(x)"
    r = 1.155
    func = "sin'(x)"
    rss_vals = {}
    dx_vals = []
    dydx_f = np.cos
    for k in range(0, 50):
        dx = 1.0 / (r**k)
        dx_vals.append(dx)
        y_golden = drvt.arrayify(dydx_f, x_0, x_max, dx)
        print "dx = %f" % dx
        for key, val in first_derivatives.iteritems():
            #print key
            val[3][0] = dx
            derivative = drvt.Derivative(dcnv.derive_dot, val)
            y = derivative.derive(f, x_0, x_max) 
            rss = drvt.rss(y, y_golden)

            if key in rss_vals:
                rss_vals[key].append(rss)
            else:
                rss_vals[key] = [rss]
    
    lgnds = []
    lgndslbs = []
    for key, val in first_derivatives.iteritems():
        lgnd, = plt.plot(dx_vals, rss_vals[key], plt_styles[key])
        lgnds.append(lgnd)
        lgndslbs.append(key)
    plt.xscale('log')
    plt.yscale('log')
    plt.title("Squared Errors in First Derivative Evaluations sin(x)")
    plt.xlabel("h")
    plt.ylabel("Squared Error")
    plt.legend(lgnds, lgndslbs)
    plt.savefig("first_derivative_sine.png", bbox_inches="tight", dpi=240)
    
    
    print "Second Derivative of sin(x)"
    r = 1.155
    func = "sin''(x)"
    rss_vals = {}
    dx_vals = []
    dydx_f = dydx_cos
    for k in range(0, 50):
        dx = 1.0 / (r**k)
        dx_vals.append(dx)
        y_golden = drvt.arrayify(dydx_f, x_0, x_max, dx)
        print "dx = %f" % dx
        for key, val in second_derivatives.iteritems():
            #print key
            val[3][0] = dx
            derivative = drvt.Derivative(dcnv.derive_dot, val)
            y = derivative.derive(f, x_0, x_max) 
            rss = drvt.rss(y, y_golden)
            if key in rss_vals:
                rss_vals[key].append(rss)
            else:
                rss_vals[key] = [rss]

    lgnds = []
    lgndslbs = []
    for key, val in second_derivatives.iteritems():
        lgnd, = plt.plot(dx_vals, rss_vals[key], plt_styles[key])
        lgnds.append(lgnd)
        lgndslbs.append(key)
    plt.xscale('log')
    plt.yscale('log')
    plt.title("Squared Errors in Second Derivative Evaluations sin(x)")
    plt.xlabel("h")
    plt.ylabel("Squared Error")
    plt.legend(lgnds, lgndslbs)
    plt.savefig("second_derivative_sine.png", bbox_inches="tight", dpi=240)

     
    return 0.0

def dydx_cos(theta):
    return -1.0 * np.sin(theta)


if __name__ == '__main__':
    main()

