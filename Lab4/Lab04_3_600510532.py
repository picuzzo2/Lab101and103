#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 04
# Problem 3
# 204111 SEC 001

def main():
    p = int(input())
    c = int(input())
    print(calculate_p2p_evolve_exp(p,c))

def calculate_p2p_evolve_exp(p,c):
    x = p-1
    y = (x+c)//12
    if y > p:
        return p*500
    elif x <0:
        return 0
    else:
        return y*500
    
if __name__ == '__main__':
    main()
        
    


