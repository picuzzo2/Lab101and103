#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 03
# Problem 3
# 204111 SEC 001

def main():
    x = float(input())                              
    octagon = octagon_area(x)  #call octagon_area      
    print('{:6f}' .format(octagon))       

def octagon_area(x):
    #octagon area = square - 4*triangle
    square_area = x*x
    triangle_area = (4)*(1/2)*(x/3)*(x/3)
    octagon_area = square_area - triangle_area
    return octagon_area

if __name__ == '__main__':
    main()