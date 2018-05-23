#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 10
# Problem 3
# 204111 SEC 001

def main():
    list_a = [0,1,2,3]
    n = int(input())
    print(nondest_rotate_list(list_a, n))

def nondest_rotate_list(list_a,n):
    n=n%len(list_a)
    rotate = len(list_a)-n
    new_list = list_a[rotate:] + list_a[:rotate]
    return new_list

if __name__ == '__main__':
    main()