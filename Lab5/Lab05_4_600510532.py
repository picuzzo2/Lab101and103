#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 05
# Problem 4
# 204111 SEC 001

def main():
    l1,t1,w1,h1 = map(int,input().split())
    l2,t2,w2,h2 = map(int,input().split())
    overlap = is_overlapped(l1,t1,w1,h1,l2,t2,w2,h2)
    print(overlap)

def is_overlapped(l1,t1,w1,h1,l2,t2,w2,h2):

    if  (l1 > l2+w2) or (l2 > l1+w1) or (t1 > t2+h2) or (t2 > t1+h1):  #not overlap each sideB
        return False
    else:
        return True

if __name__ == '__main__':
    main()
