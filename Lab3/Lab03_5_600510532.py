#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 03
# Problem 5
# 204111 SEC 001


import math 

def kth_digit(number, k):     #lab4 funtion
    k = (int((math.fabs(number)//(10**k))%10))
    return k

def main(): 
    number = int(input())       
    k = int(input())                   
    value = int(input())           
    output = set_kth_digit(number, k, value)  #call set kth digit
    print('{:d}' .format(output))             

def set_kth_digit(number, k, value):
    kth = kth_digit(number, k)     #call lab4 function
    # kth-k+value
    set = (number-((10**k)*kth)+((10**k)*value))
    return set

if __name__ == '__main__':
    main()