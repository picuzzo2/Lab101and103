#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 03
# Problem 1
# 204111 SEC 001


import math

def main():
    surface = float(input("input surface area: "))
    radius = find_r_from_surface_area(surface)
    volume = sphere_volume(radius)
    print("volume = {0:.02f}" .format(volume))

def find_r_from_surface_area(surface):
    #surface area = 4* PI *R^2
    #r = sqrt(surface/(4PI))
    r = math.sqrt(surface/(4*math.pi))
    return r

def sphere_volume(radius):
    #volume = 4/3*PI*R^3
    v = ((4/3)*math.pi*(math.pow(radius, 3)))
    return v

if __name__ == '__main__':
    main()

