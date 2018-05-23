#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 05
# Problem 1
# 204111 SEC 001

import math

def main():
    x1,y1,r1 = map(float,input().split())
    x2,y2,r2 = map(float,input().split())
    print(intersects(x1,y1,r1,x2,y2,r2,epsilon=10**-6))


def intersects(x1,y1,r1,x2,y2,r2,epsilon=10**-6):
    distance = math.sqrt(((x1-x2)**2) + ((y1-y2)**2))  #calculate distance of c1 and c2
    zigma_r = r1+r2     
    if zigma_r > distance and math.fabs(zigma_r-distance) > epsilon:     #check zigma r and compare epsilon
        return 1
    elif math.fabs(zigma_r - distance) < epsilon :
        return 0
    else:
        return -1

if __name__ == '__main__':
    main()