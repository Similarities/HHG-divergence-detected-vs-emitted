# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 13:33:12 2019

@author: sweedy
"""

# full beam calculation

import matplotlib.pyplot as plt
import math

Nmax = 42+1
beam_radius_fundamental = 60 #mm
beam_divergence_half_angle = (60/1500)
distance_source_grating= 1416 #mm
capture_radius_at_grating_V = 3.66*0.5
capture_radius_at_grating_H = 25*0.5
beam_radius_at_grating = beam_divergence_half_angle*distance_source_grating
print(beam_radius_at_grating, 'beamradius at grating')

switch = 0

captured_height = 3.63 # height collected from grating


a = [i for i in range (Nmax)]
b = [i for i in range (Nmax)]

print(a)

def beamradius_at_grating_def():

    for i in range(1,Nmax):

        Theta = math.atan(beam_divergence_half_angle)
        radius_fundamental_grating = distance_source_grating*math.tan(Theta)
        #print(radius_fundamental_grating, "Theta laser = half angle laser")
        #print(beam_radius_at_grating, "alternative Rechenmethode")
        radius_N_at_grating = beam_radius_at_grating/i
        #print(radius_N_at_grating, i, "radius HHG with N")


        if radius_N_at_grating > capture_radius_at_grating_V:
            #print(radius_N_at_grating, "radius HHG with N is bigger than capturing angle in V for N: ", i)
            switch = 0

        else:
            #print("now capturing angle is bigger than HHG beam divergence, for N :", i)
            switch = i
            print(switch, "from here the capturing angle is bigger as HHG radius")
            return switch


beamradius_at_grating_def()


def calculate_relative_area_detected(switch):

    for x in range(1,switch):



        captured_area = 3.142 *capture_radius_at_grating_V*beam_radius_at_grating/x
        print(captured_area, "captured Area for N :", x)

        theoretical_Area = 3.142*(beam_radius_at_grating/x)**2

        print(theoretical_Area, "theorectial area at grating for N: ", x)

        relative_factor = captured_area/theoretical_Area

        print('relative captured Area for N: ', relative_factor)

        a[x] = x

        b[x] = relative_factor


    for x in range(switch, Nmax):

        relative_factor = 1

        a[x] = x
        b[x] = relative_factor

switch = beamradius_at_grating_def()
calculate_relative_area_detected(switch)




    
plt.figure(1)
plt.plot(a,b)
plt.xlabel('N')
plt.ylabel('correction to account for full beam diameter')
plt.show()


    
