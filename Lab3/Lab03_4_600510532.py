#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 03
# Problem 4
# 204111 SEC 001


import math
def main():
    number = int(input())         
    k = int(input())           
    output = kth_digit(number, k)  #call kth_digit
    print('{:d}' .format(output))      

def kth_digit(number, k):
    # |x|/10^k%10
    k = (int((math.fabs(number)//(10**k))%10))
    return k

if __name__ == '__main__':
    main()