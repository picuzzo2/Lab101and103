# -*- coding: utf-8 -*-
# @Author: CSB307
# @Date:   2018-02-09 03:56:19
# @Last Modified by:   CSB307
# @Last Modified time: 2018-02-09 04:24:07



### NEW SUMMIT WRONG FILE NAME####

def main():
    print(prime_factorize(180))
    print(prime_factorize(48))
    print(lcmfactor(180,48))
    print(lcm(lcmfactor(180,48)))


###################prime and helper###################

def prime_factorize(x):
    div = 2
    prime = [1]
    return helper(x,div,prime)

def helper(x,div,prime):
    if x == div:
        prime.append(div)
        return prime
    else:
        if x%div == 0:
            prime.append(div)
            return helper(x//div,div,prime)
        else:
            div +=1
            return helper(x,div,prime)

######################################################

########################Lcm Factor####################

def lcmfactor(x,y):
    digit1 = prime_factorize(x)
    digit2 = prime_factorize(y)
    lcm = []
    for i in range(len(digit1)):
        if digit1[i] in digit2:
            lcm.append(digit1[i])
            digit2.remove(digit1[i])
            
    return lcm

#######################################################

#########################Lcm###########################

def lcm(alist):
    result = 1
    for i in alist:
        result *= i
    return result

#######################################################

if __name__ == '__main__':
    main()
