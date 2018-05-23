#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 08
# Problem 1
# 204111 SEC 001

def main():
    x = int(input())
    y = int(input())
    print(gcd(x,y))

def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)

if __name__ == '__main__':
    main()