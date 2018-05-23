#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 05
# Problem 5
# 204111 SEC 001 

def main():
    year = int(input())
    print(zodiac_element(year))

def zodiac_element(year):
    def zodiac():              #define zodiac
        if year%12==4:
            return 'Rat'
        if year%12==5:
            return 'Ox'
        if year%12==6:
            return 'Tiger'
        if year%12==7:
            return 'Rabbit'
        if year%12==8:
            return 'Dragon'
        if year%12==9:
            return 'Snake'
        if year%12==10:
            return 'Horse'
        if year%12==11:
            return 'Goat'
        if year%12==0:
            return 'Monkey'
        if year%12==1:
            return 'Rooster'
        if year%12==2:
            return 'Dog'
        if year%12==3:
            return 'Pig'
 
    def element():            #define element
        if year%10==0 or year%10==1:
            return 'Metal'
        if year%10==2 or year%10==3:
            return 'Water'
        if year%10==4 or year%10==5:
            return 'Wood'
        if year%10==6 or year%10==7:
            return 'Fire'
        if year%10==8 or year%10==9:
            return 'Earth'

    return(element()+" "+zodiac())     
    

if __name__ == '__main__':
    main()