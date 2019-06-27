# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 13:33:12 2019

@author: similarity
"""



class full_HHG_beamsize:

    def __init__(self, Nmax, beam_diameter, focal_lenght, distance, capturing_r_V, capturing_r_H):

        self.Nmax = Nmax

        self.beam_diameter = beam_diameter

        self.focal_length = focal_lenght

        self.distance = distance

        self.capturing_r_V = capturing_r_V

        self.capturing_r_H = capturing_r_H

        self.beam_radius_at_grating = (self.beam_diameter/self.focal_length)*self.distance_source_grating

        self.switch = 0

        self.a = [i for i in range (Nmax)]

        self.b = [i for i in range (Nmax)]

        self.c = [i for i in range (Nmax)]




    def theoretical_HHG_beam_radius_at_distance(self):

            for i in range(1,self.Nmax):

                self.c[i] = self.beam_radius_at_grating/i

            return self.c



    def test_switch(self):


        for i in range(1,self.Nmax):

            if self.radius_N_at_grating > self.capturing_r_V:
                #print(radius_N_at_grating, "radius HHG with N is bigger than capturing angle in V for N: ", i)
                self.switch = 0

            else:
            #print("now capturing angle is bigger than HHG beam divergence, for N :", i)
                self.switch = i

        print(self.switch, "from here the capturing angle is bigger as HHG radius")

        return self.switch




    def calculate_relative_area_detected(self):

        self.test_switch()


        for x in range(1,self.switch):

            captured_area = 3.142 *self.capturing_r_V*self.beam_radius_at_grating/x
            #print(captured_area, "captured Area for N :", x)

            theoretical_Area = 3.142*(self.beam_radius_at_grating/x)**2

            #print(theoretical_Area, "theorectial area at grating for N: ", x)

            relative_factor = captured_area/theoretical_Area

            #print('relative captured Area for N: ', relative_factor)

            self.a[x] = x

            self.b[x] = relative_factor



        for x in range(self.switch, self.Nmax):

            relative_factor = 1

            self.a[x] = x

            self.b[x] = relative_factor




        return self.a, self.b












    


    
