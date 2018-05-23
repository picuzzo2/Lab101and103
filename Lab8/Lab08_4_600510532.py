#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 08
# Problem 4
# 204111 SEC 001

def main():
    n = int(input())
    print(series(n))

def series(n):
    if n==2:
        return 3
    elif n==1:
        return 1
    elif n==0:
        return 0
    else:
        return 2*(series(n-2))+series(n-1)

if __name__ == '__main__':
    main()


