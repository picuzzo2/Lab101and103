#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 06
# Problem 1
# 204111 SEC 001

def main():
    x = float(input())
    y = int(input())
    xy = int_power(x,y)
    print(xy)

def int_power(x,y):
    x2=1
    for i in range(abs(y)):
        x2=x2*x
    if y>=0:                  #+
        return x2
    else:                    # -
        return 1/x2 
if __name__ == '__main__':
    main()