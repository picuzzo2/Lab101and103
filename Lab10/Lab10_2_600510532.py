#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 10
# Problem 2
# 204111 SEC 001

def main():
    list_x=[10, 'hello', 23.5, 4,20,1.55,86.2,'eiei']
    print(classify(list_x))

def classify(list_x):
    #
    list_a=[]
    list_b=[]
    list_c=[]
    for i in range(len(list_x)):
        if type(list_x[i]) == int:
            list_a.append(list_x[i])
        elif type(list_x[i]) == float:
            list_b.append(list_x[i])
        else:
            list_c.append(list_x[i])
    
    return (list_a,list_b,list_c)

if __name__ == '__main__':
    main()