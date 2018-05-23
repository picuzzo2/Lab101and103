#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 04
# Problem 1
# 204111 SEC 001

import math
def main():
    x = float(input())
    print(nearest_odd(x))

def nearest_odd(x):
    x = math.floor(x)
    if x%2 == 0:
        x = x+1
    return x


if __name__ == '__main__':
    main()
    
