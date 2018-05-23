#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 08
# Problem 2
# 204111 SEC 001

def main():
    n = int(input())
    num = int(input())
    print(n_base_to_10(n,num))

def n_base_to_10(n,num):
    b=0
    base(n,num,b)
    return base(n,num,b)

def base(n,num,b):
    if num == 0 :
        return 0 
    else:
        return base(n,num//10,b+1)+((num%10)*(n**b))

if __name__ == '__main__':
    main()