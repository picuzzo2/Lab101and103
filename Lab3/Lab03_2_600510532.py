#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 03
# Problem 2
# 204111 SEC 001

def main():
    x = int(input())
    reverse = reverse_digits(x)
    print('%d' %reverse)

def reverse_digits(x):
    #1234 % 10 = 4
    #1234 % 100 // 10 = 3
    #1234 % 1000// 100 = 2
    #1234 // 1000 = 1
    digit_1 = x%10
    digit_2 = x%100//10
    digit_3 = x%1000//100
    digit_4 = x//1000
    reverse = int((digit_1*1000)+ (digit_2*100)+ (digit_3*10)+ digit_4)
    return reverse


if __name__ == '__main__':
    main()