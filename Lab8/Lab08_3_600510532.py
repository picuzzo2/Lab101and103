#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 08
# Problem 3
# 204111 SEC 001

def main():
    n = int(input())
    print(is_prime(n))

def is_prime(n):
    i = 2
    help_is_prime(n,i)
    return help_is_prime(n,i)

def help_is_prime(n,i):
    if n%i==0:
        return False
    elif n**(1/2)<i:
        return True

    else:
        return help_is_prime(n,i+1)
if __name__ == '__main__':
    main()