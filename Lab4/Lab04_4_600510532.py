#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 04
# Problem 1
# 204111 SEC 001

import math

def main():
    x = float(input())
    print(round_to_int(x))

def round_to_int(x):
    y = abs(x)%1
    if y>=0.5:
        if x>=0:
            return math.ceil(abs(x))

        if x<0:
            return math.ceil(abs(x))*-1
 
    if y<0.5:
        if x>=0:
            return math.floor(abs(x))
  
        if x<0:
            return math.floor(abs(x))*-1





if __name__ == '__main__':
    main()