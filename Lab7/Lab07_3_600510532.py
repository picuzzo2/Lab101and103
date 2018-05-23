#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 07
# Problem 3
# 204111 SEC 001

def main():
    n = int(input())
    triangle(n)

def triangle(n):
    for i in range(n-1):            #print(*)
        print('*',end='')
        delta = i-1

        for j in range(i+delta):          #print(. * i)
            print('.',end='')


        if i != 0:                #print(last *)
            print('*')
        else:
            print(' ')

    for h in range(n):
        print('*',end=' ')
if __name__ == '__main__':
    main()


