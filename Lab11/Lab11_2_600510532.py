#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 11
# Problem 2
# 204111 SEC 001

import copy
def main():
    list_a = [[2,3,4,5],[8,7,6,5],[0,1,2,3],['a','b','c','d']]
    row = int(input())
    col = int(input())
    print(remove_row_col(list_a,row,col))


def remove_row_col(list_a,row,col):
 
    list_b=copy.deepcopy(list_a)
    #remove col
    for i in range(len(list_a)):
        tempolist = list_b[i]
        if abs(col) <= len(tempolist)-1:
            tempolist.pop(col)

    #remove row
    if abs(row) <= len(list_a)-1 and len(list_b) == len(list_a):
        list_b.pop(row)

    return list_b

if __name__ == '__main__':
    main()
