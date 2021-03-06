#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 16:54:54 2019

@author: similarities
"""

import matplotlib.pyplot as plt
import numpy as np


class Open_and_Plot_Picture:

        def __init__(self, filename,  xlabel, ylabel):


            self.filename = filename

            self.filedescription=self.filename

            #print(self.filedescription, "description")

            self.xlabel = xlabel

            self.ylabel = ylabel

            self.picture = np.empty([])

            self.integrated= np.empty([])

            self.x_backsubstracted=np.empty([2048, 2048])

            self.x_axis_in_nm =np.empty([2048,1])

            self.result_array = np.zeros([2048,2])


        def open_file(self):

            self.picture = plt.imread(self.filename)




            # optional plots raw picture.
            #plt.imshow (self.picture, label=self.filedescription)
            #plt.title(self.filedescription, fontdict=None, loc='center', pad=None)
            #plt.legend() #handles=[plot]
            #plt.ylabel(self.ylabel)
            #plt.xlabel(self.xlabel)

            return self.picture


            
        def integrate_and_plot(self):

            self.integrated = np.sum(self.picture, axis = 1)

            return self.integrated


        
        def background(self):

            back_mean=np.mean(self.picture[:, 1900:1950], axis = 1)

            i=1

            N=len(self.picture)-1

            
            while i<= N:
                
                self.x_backsubstracted[::,i] = self.picture[::,i]- (back_mean[i])

                i = i+1


            self.integrated= np.sum(self.x_backsubstracted[:,:], axis = 1)

            for i in range (0, len(self.integrated)-1):
                self.integrated[i] = self.integrated[i] - i*i*0.17+247000- 110*i

            return self.integrated



        
        def grating_function(self):

            N = len(self.integrated)

            i = 0


            while i <= N-1:


                self.x_axis_in_nm[i] =1.27877896e-06*i**2 -1.37081526e-02*i +  3.46785380e+01
                i = i+1
            


            # optional plots integrated picture
            #print(self.x_axis_in_nm) 
            
            #plt.figure(6) #handles=[plot]
            #plt.ylabel(self.ylabel)
            #plt.xlabel(self.xlabel)
            #plt.plot(self.x_axis_in_nm,self.integrated,label=self.filedescription,linewidth=2)
            #plt.ylim((-200000,11500000))
            #plt.xlim((58., 28.5))
            #plt.legend()


            self.array_of_spectrum()

            return self.result_array



        def array_of_spectrum(self):

            for x in range(0, len(self.x_axis_in_nm)):

                self.result_array[x,0] = self.x_axis_in_nm[x]

                self.result_array[x,1] = self.integrated[x]




           
        def plot_HHG_800nm (self):

            i = 14

            N = 30

            while i<=N:

                #print(800./i)

                plt.figure(6)

                plt.vlines(800./i, ymin = 9, ymax = 40000000, color ="b", linewidth =0.2)

                i = i+1

            plt.label="800nm"

            plt.legend()

            plt.show()
                
                
        def plot_HHG_8xxnm (self):

            i = 14

            N = 30

            while i<=N:

                #print(800./i)

                lambda2 =780.

                print(lambda2)

                plt.figure(6)

                plt.vlines(lambda2/i, ymin = 9, ymax = 40000000, color ="g", linewidth =1)

                i = i+1

            plt.legend()







