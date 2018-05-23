#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 07
# Problem 4
# 204111 SEC 001


def main():
    n = int(input())
    print(life_path(n))

def life_path(n):
    result = n
    main = n
    if n > 9:              #n is not digit
        while result >9 :   #result is not digit
            main = result
            result = 0

            while main != 0:    
                mod = main % 10
                result += mod
                main //= 10

            if result <=9:
                return result
    else:
        return n
if __name__ == '__main__':
    main()


    

