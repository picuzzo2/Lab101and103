#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 05
# Problem 2
# 204111 SEC 001
#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 05
# Problem 2
# 204111 SEC 001

def main():
    a,b,c = map(int,input().split())
    print(is_p_triple(a,b,c))


def my_max_mid_min(a, b, c):
    if a >= b >= c:  # abc
        return(a, b, c)
    elif a >= c >= b:  # acb
        return(a, c, b)
    elif b >= a >= c:  # bac
        return(b, a, c)
    elif b >= c >= a:  # bca
        return(b, c, a)
    elif c >= a >= b:  # cab
        return(c, a, b)
    elif c >= b >= a:  # cba
        return(c, b, a)

def is_p_triple(a,b,c):
    max,mid,min=my_max_mid_min(a,b,c)            #reorder integer
    c = ((mid**2)+(min**2))**(1/2)            #peta calculate
    if max == c:
        return True
    else:
        return False

if __name__ == '__main__':
    main()
