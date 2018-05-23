#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 06
# Problem 3
# 204111 SEC 001

def main():
    x = int(input())
    factorize(x)
    #factorize(17)
    #factorize(360)
         
def factorize(x):
    i = 2
    a = x
    print('%d is'%x,end =' ')          
    while i<=(a**(1/2)):            # i < root a
        if a%i==0:
            a = a//i 
            print(i, end=' * ')
        else:
            i +=1
    if x==a:
        print('prime')
    else:
        print(a)


        

if __name__ == '__main__':
    main()