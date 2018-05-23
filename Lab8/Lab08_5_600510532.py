#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 08
# Problem 5 
# 204111 SEC 001

import math
def main():
    num = int(input())
    print(reverse_num(num))

def reverse_num(num):
    i = int(math.log10(num))
    eiei(num,i)
    return eiei(num,i)

def eiei(num,i):
    if num == 0:
        return 0
    else:
        return eiei(num//10,i-1)+((num%10)*(10**i))

if __name__ == '__main__':
    main()