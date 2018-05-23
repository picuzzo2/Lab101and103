#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 11
# Problem 4
# 204111 SEC 001

def main():
    list_a = [1, 2, [[2, [[145], 34]], [48, 22]]]
    print(sum_nested_list(list_a))

def sum_nested_list(list_a):
    list_b = []
    for number in list_a:
        list_b.append(number)

    j=0
    while j != len(list_b):
        if type(list_b[j]) == int:
            j+=1
        else:
            list_b.extend(list_b.pop(j))
    return sum(list_b)


if __name__ == '__main__':
    main()
