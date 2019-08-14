#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 16:54:54 2019

@author: similarities
"""

import matplotlib.pyplot as plt
import numpy as np


class Open_and_Plot_Picture:
        def __init__(self, filename, filedescription, xlabel, ylabel,xmin, xmax,color, ymin = 0, ymax=2048 ):
            self.filename = filename
            self.filedescription= filedescription
            self.xlabel = xlabel
            self.ylabel = ylabel
            self.ymin = ymin
            self.xmin = xmin
            self.ymax = ymax
            self.xmax = xmax
            self.picture = np.empty([])
            self.integrated= np.empty([])
            self.x_backsubstracted=np.empty([2048, 2048])
            self.x_axis_in_nm =np.empty([2048,1])
            self.color = color

        def open_file(self):
            self.picture = plt.imread(self.filename)
            #plt.figure(10)
            #plt.imshow (self.picture, label=self.filedescription)
            #plt.title(self.filedescription, fontdict=None, loc='center', pad=None)
            #plt.legend() #handles=[plot]
            #plt.ylabel(self.ylabel)
            #plt.xlabel(self.xlabel)
            return self.picture
            
        def integrate_and_plot(self):
            self.integrated = np.sum(self.picture[:,self.xmin:self.xmax], axis = 1)          
            #plt.figure(1)
            #plt.plot(self.integrated,label=self.filedescription,linewidth=0.5)
            #plt.legend()
            return self.integrated
        
        def background(self):
            back_mean=np.mean(self.picture[:, 1650:1900], axis = 1)
            i=1
            N=len(self.picture)-1
            
            while i<= N:
                
                self.x_backsubstracted[::,i] = self.picture[::,i]- back_mean[i]

                i = i+1
                
                
            plt.figure(3)
            
            plt.imshow(self.x_backsubstracted)
            self.integrated= np.sum(self.x_backsubstracted[:,self.xmin:self.xmax], axis = 1)

            plt.figure(4)
            plt.plot(self.integrated,label=self.filedescription + "backsubbed",linewidth=1, color =self.color, alpha = 0.5)

            plt.legend()
            print(len(self.integrated), 'length of ROI')
            np.savetxt(self.filedescription + '_backsubbed_integrated', self.integrated, delimiter='', fmt='%1.4e')   # use exponential notation
            return self.integrated
        
        def grating_function(self):
            N = len(self.integrated)
            i = 0
            print (N)
            while i <= N-1:
                #self.x_axis_in_nm[i] =  8.303e-07 x - 0.01564 x + 56.25 #-1.771e-09 x + 9.376e-06 x - 0.02669 x + 59.48
                self.x_axis_in_nm[i] =1.22447518e-06*i**2 -1.73729829e-02*i+  5.82820234e+01
                i = i+1
            

            print(self.x_axis_in_nm) 
            
            plt.figure(6) #handles=[plot]
            plt.ylabel(self.ylabel)
            plt.xlabel(self.xlabel)
            plt.plot(self.x_axis_in_nm,self.integrated,label=self.filedescription,linewidth=2, color = self.color, alpha = 0.5)
            plt.xlim([38,50])
            plt.ylim([0, 4000000])
            plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
            
            
           # self.integrated[i,0] = f(x)*self.integrated[i,0]
           # create new x array: make 2D array
           
        def plot_HHG_800nm (self):
            i = 13
            N = 33
            while i<=N:
                print(800./i)
                plt.figure(6)
                plt.vlines(800./i, ymin = 9, ymax = 60000000, color ="b", linewidth =0.2)
                i = i+1
                
            plt.vlines(800./20, ymin = 9, ymax =60000000, color ="r", linewidth =0.2, label ="CWE cutoff")
            plt.savefig('0118_40_z2400_partial_lineout.png',  bbox_inches="tight", dpi = 1000)









Picture1=Open_and_Plot_Picture('20190118/rotated/spectro1__Fri Jan 18 2019_14.03.31_40.tif', ' + 5.0 RL GVD 0', 'energy [nm]', 'integrated counts',700,800,'r')
Picture1.open_file()
#Picture2.integrate_and_plot()
Picture1.background()
Picture1.grating_function()

Picture1=Open_and_Plot_Picture('20190118/rotated/spectro1__Fri Jan 18 2019_14.17.36_49.tif', ' + 5.0 RL GVD +300', 'energy [nm]', 'integrated counts',600,700,'b')
Picture1.open_file()
#Picture2.integrate_and_plot()
Picture1.background()
Picture1.grating_function()


Picture1=Open_and_Plot_Picture('20190118/rotated/spectro1__Fri Jan 18 2019_14.09.51_45.tif', ' + 5.0 RL GVD -300', 'energy [nm]', 'integrated counts',100,200,'c')
Picture1.open_file()
#Picture2.integrate_and_plot()
Picture1.background()
Picture1.grating_function()
Picture1.plot_HHG_800nm()

