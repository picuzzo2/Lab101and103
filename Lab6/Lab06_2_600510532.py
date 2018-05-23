#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 06
# Problem 2
# 204111 SEC 001  

def main():
    x = float(input())
    result = float_to_bin(x)
    print('%.6f' %result) 
    
def float_to_bin(x):
    int_x=abs(x)//1                 #|
    int_result = 0                  #|--- int
    int_i = 0                       #|
    while int_x//1 != 0:
        int_mod = int_x%2
        int_result = int_result+(int_mod*(10**int_i))
        int_x=int_x//2      
        int_i = int_i+1

    float_result= 0                 #|
    float_i=-1                      #|--- float
    float_x=abs(x)%1                #|
    for a in range(6):
        float_x = float_x*2
        float_result = float_result+((float_x//1)*(10**float_i))
        float_x = float_x%1
        float_i = float_i-1
    final_result = int_result+float_result
    if x>=0:
        return final_result
    elif x<0:
        return -(final_result)     #return minus


if __name__ == '__main__':
    main()