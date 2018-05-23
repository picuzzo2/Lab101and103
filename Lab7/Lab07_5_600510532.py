#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 07
# Problem 5
# 204111 SEC 001

import math
def main():
    num = int(input())
    pos = int(input())
    result = rotate(num,pos) 
    print(result)   

def rotate(num,pos):
    count = int(math.log10(num))+1     #all digit numbers count

    new_pos = abs(pos) % (count)  #4
    if pos >= 0:
        repos = num%(10**(new_pos) )       #5
        renum = num//(10**(new_pos))       #1234
        result = (repos * (10**(count-new_pos))) + renum
        #print(count)
    else:
        repos = num%(10**(count-new_pos))
        renum = num//(10**(count-new_pos))
        result = (repos * (10**(new_pos))) + renum
        #print(renum)
    return result
if __name__ == '__main__':
    main()