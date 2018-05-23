#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 07
# Problem 1
# 204111 SEC 001

def main():
    x = int(input())
    y = int(input())
    print(sum_prime_in_range(x,y))

def sum_prime_in_range(x,y):
    i = 2
    a = x
    result = 0
    #LOOP y
    for k in range(y-x+1):
        a = x
        #CHECK prime
        while i<=(a**(1/2)):             # i will not be lower than sqrt.a  
            if a%i==0:                   # if i can / a
                a = a//i                 # a = a/i
            else:
                i +=1                    # if not i+1
        #IF a = x is prime
        if a == x:
            if a != 1:
                result += a
                #print('a is %d'%a)
            x += 1
            #IF not = skip
        else:
            x += 1
        i = 2
    return result


if __name__ == '__main__':
    main()

