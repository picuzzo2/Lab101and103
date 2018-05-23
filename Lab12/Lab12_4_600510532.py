#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 12
# Problem 4
# 204111 SEC 001

def main():
    list_x = [[2,3,4],[1,1,1,1,1,1,1],[1],[1],[1]]
    square_matrix(list_x)
    print(list_x)

def square_matrix(list_x):
    check = 0
    for i in range(len(list_x)):
        if len(list_x[i])>check:
            check = len(list_x[i])
    
    if len(list_x) > check:
        check = len(list_x)

    for i in range(len(list_x)):
        while len(list_x[i])<check:
            list_x[i].append(0)

    if len(list_x) < check:
        
        for i in range(len(list_x),check):
            list_x.append([])
            for j in range(check):
                list_x[i].append(0)
           






if __name__ == '__main__':
    main()