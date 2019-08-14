#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 16:54:54 2019

@author: similarities
"""

import matplotlib.pyplot as plt
import numpy as np


class Open_and_Plot_Picture:
        def __init__(self, filename,  xlabel, ylabel,xmin, xmax, z):
            self.filename = filename
            self.filedescription="01"+self.filename[26:34]+"_"+self.filename[-6:-4]
            print(self.filedescription, "description")
            self.xlabel = xlabel
            self.ylabel = ylabel
            self.ymin = 0
            self.xmin = xmin
            self.ymax = 2048
            self.xmax = xmax
            self.picture = np.empty([])
            self.integrated= np.empty([])
            self.x_backsubstracted=np.empty([2048, 2048])
            self.x_axis_in_nm =np.empty([2048,1])
            self.z = z
            self.filedescription="20190123_"+self.filename[-6:-4]+ str(z)
            print(self.filedescription, "description")


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
            back_mean=np.mean(self.picture[:, 1700:2000], axis = 1)
            i=1
            N=len(self.picture)-1
            
            while i<= N:
                
                self.x_backsubstracted[::,i] = self.picture[::,i]- (back_mean[i]) #-1500+i*1.6

                i = i+1
                
                
            plt.figure(3)
            
            plt.imshow(self.x_backsubstracted)
            self.integrated= np.sum(self.x_backsubstracted[:,self.xmin:self.xmax], axis = 1)

            #print(len(self.integrated), 'length of ROI')
           #np.savetxt(self.filedescription + '_backsubbed_integrated', self.integrated, delimiter='', fmt='%1.4e')   # use exponential notation
            return self.integrated
        
        def grating_function(self):
            N = len(self.integrated)
            i = 0
            #print (N)
            while i <= N-1:
                #self.x_axis_in_nm[i] =  8.303e-07 x - 0.01564 x + 56.25 #-1.771e-09 x + 9.376e-06 x - 0.02669 x + 59.48
                self.x_axis_in_nm[i] =1.15696112e-06*i**2 -1.63040125e-02*i+  5.20764280e+01
                i = i+1
            

            #print(self.x_axis_in_nm) 
            
            plt.figure(6) #handles=[plot]
            plt.ylabel(self.ylabel)
            plt.xlabel(self.xlabel)
            plt.plot(self.x_axis_in_nm,self.integrated,label=self.filedescription,linewidth=2)
            plt.xlim(38, 50)
            plt.ylim((0,6225500))
            plt.legend()

            
           # self.integrated[i,0] = f(x)*self.integrated[i,0]
           # create new x array: make 2D array
           
        def plot_HHG_800nm (self):
            i = 15
            N = 32
            while i<=N:
                #print(800./i)
                plt.figure(6)
                plt.vlines(798./i, ymin = 9, ymax = 40000000, color ="b", linewidth =0.2)

                i = i+1
            plt.label="800nm"   
            plt.legend()
            plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
            plt.savefig("20190123_" + str(self.z) + ".png",  bbox_inches="tight", dpi = 1000)
                
                
        def plot_HHG_8xxnm (self):
            i = 15
            N = 32
            while i<=N:
                #print(800./i)
                lambda2 =778.
                print(lambda2)
                plt.figure(6)
                plt.vlines(lambda2/i, ymin = 9, ymax = 40000000, color ="g", linewidth =1)
                i = i+1
            plt.legend()



Picture1=Open_and_Plot_Picture('spectro1__Wed Jan 23 2019_14.51.31_17.tif', 'nm', 'counts',700, 800, "z2000um GVD 900")
Picture1.open_file()
#Picture2.integrate_and_plot()
Picture1.background()
Picture1.grating_function()

Picture1=Open_and_Plot_Picture('spectro1__Wed Jan 23 2019_15.11.38_20.tif', 'nm', 'counts',800, 900, "z2000um GVD 600")
Picture1.open_file()
#Picture2.integrate_and_plot()
Picture1.background()
Picture1.grating_function()

Picture1=Open_and_Plot_Picture('spectro1__Wed Jan 23 2019_15.17.26_24.tif', 'nm', 'counts', 700, 800, "z2000um GVD 0")
Picture1.open_file()
#Picture2.integrate_and_plot()
Picture1.background()
Picture1.grating_function()



Picture1.plot_HHG_800nm()




