#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 06
# Problem 5
# 204111 SEC 001

def main():
    n = int(input())
    result = longest_digit_run(n)
    print(result)

def longest_digit_run(n):
    result = 0
    count = 0
    comepare = n%10                #comepare = digit

    while n != 0:              #loop until last digit
        target = n % 10            #target = digit
        if comepare == target:
            count += 1
            if count >= result:
                result = count     #keep 'count'

        else:
            if count >= result:
                result = count     #keep ' count'
            count = 1              #reset count
        comepare = n%10            #newcompare
        n //= 10
    return result

if __name__ == '__main__':
    main()