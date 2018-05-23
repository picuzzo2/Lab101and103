#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 07
# Problem Extra
# 204111 SEC 001

def main():
    n = int(input())
    pyramid_stairs(n)

def pyramid_stairs(n):
    count = 0
    for i in range(n-1,-1,-1): #space 0 5 10 15 20
        #print('i=%d'%i)
        for j in range(i):
            print('     ',end='')
        print('  o  ******',end='' )
        for s in range(count):
            print('          ',end='')
        print('******  o')

        for j in range(i):
            print('     ',end='')
        print(' /|\ *     ',end='')
        for s in range(count):
            print('          ',end='')
        print('     * /|\ ')

        for j in range(i):
            print('     ',end='')
        print(' / \ *     ',end='')
        for s in range(count):
            print('          ',end='')
        print('     * / \ ')
        count +=1

    if n != 0:
        for u in range(n-1):
            print('**********',end='')
        print('**********************')
    else:
        print('')

if __name__ == '__main__':
    main()
