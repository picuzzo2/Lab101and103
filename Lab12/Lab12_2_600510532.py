#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 12
# Problem 2
# 204111 SEC 001



def main():
    set_a = {'a','b','c'}
    print(power_set(set_a))

def power_set(set_a):
    list_a = list(set_a)
    result = [[]]
    set_b = []
    for member in list_a:
        for subset in result:
            #print('subset =%s'%subset)
            result = result + [subset + [member]]
    for i in result:
        set_b.append(set(i))
    return set_b

            
   
    




if __name__ == '__main__':
    main()

