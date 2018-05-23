#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 04
# Problem 1
# 204111 SEC 001



def main():
    first = int(input())
    second = int(input())
    print(love6(first, second))

def love6(first, second):
    if first ==6 or second ==6 or first - second ==6 or first+ second==6 or second - first ==6:
        return True
    else:
        return False
if __name__ == '__main__':
    main()