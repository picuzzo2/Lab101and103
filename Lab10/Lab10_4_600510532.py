#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 10
# Problem 4
# 204111 SEC 001

def main():
    list_a=[1,2,3,4]
    n = int(input())
    dest_rotate_list(list_a,n)
    print(list_a)

def dest_rotate_list(list_a,n):
    n=n%len(list_a)
    for i in range(len(list_a)-n):
        list_a.append(list_a.pop(0))       

if __name__ == '__main__':
    main()