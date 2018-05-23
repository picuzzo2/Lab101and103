#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 07
# Problem 2
# 204111 SEC 001

def main():
    test_digit_count()

def digit_count(x,base=10):
    count = 0
    x = abs(x)
    while x>0:
        x = x// base
        count += 1
    return count

def test_digit_count():
    print(digit_count(258)   )         #258 base 10 without input base 
    print(digit_count(258,10))         #258 base 10 with input base = 10  
    print(digit_count(258,2) )         #258 base 2 with input base = 2
    print(digit_count(258,4) )         #258 base 4 with input base = 4
    print(digit_count(258,5) )         #258 base 5 with input base = 5
    print(digit_count(-258,2))         #-258 base 2 with input base = 2
    print(digit_count(-258)  )         #-258 base 10 without input base
if __name__ == '__main__':
    main()