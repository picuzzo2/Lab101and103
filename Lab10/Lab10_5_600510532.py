#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 10
# Problem 5
# 204111 SEC 001

def main():
    num = 42641323862
    #eiei = three_digits_to_word(n)
    #print(eiei)
    print(num_to_word(num))

def three_digits_to_word(n):
    #111 = one hundred eleven
    hun = n//100
    middle = (n%100)//10
    rest = (n%100)%10

    def hund(hun,middle,rest):
        list_hun=['','one hundred','two hundred','three hundred','four hundred','five hundred','six hundred','seven hundred','eight hundred','nine hundred']
        hundred = list_hun[hun]
        if middle ==0 and rest ==0:
            return hundred
        if hun==0:
            return hundred
        else:
            return hundred + ' '

    def mid(middle,rest):
        if middle ==1:
            list_middle_1=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
            first = list_middle_1[rest]
        else:
            list_middle = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
            first = list_middle[middle]
        if middle==0 or middle==1 or rest==0:
            return first
        else:
            return first+'-'

    def digit(hun,middle,rest):
        if middle!=1 :
            list_digit=['','one','two','three','four','five','six','seven','eight','nine']
            last = list_digit[rest]
        else:
            last = ''
        return last


    return hund(hun,middle,rest) + mid(middle,rest) + digit(hun,middle,rest)
        
def num_to_word(num):  
    if num ==0:
        result = 'zero'
    else:

        n = num//1000000000000
        num = num%1000000000000

        #def trillion():
        if n!=0:
            trillion = three_digits_to_word(n) + 'trillion' +' '
        else:
            trillion = ''

        #def billion():
        n = num//1000000000
        num = num%1000000000
        if n!=0:
            billion = three_digits_to_word(n) +' ' + 'billion'+' '
        else:
            billion = ''

        #def million():
        n = num//1000000
        num = num%1000000
        if n!= 0:
            million =  three_digits_to_word(n) +' '+ 'million'+' '
        else:
            million = ''

        #def thousand():
        n = num//1000
        num = num%1000
        if n!=0:
            thousand =  three_digits_to_word(n) +' ' + 'thousand'+' '
        else:
            thousand = ''

        #def digit():
        n=num
        if num!=0:
            digit = three_digits_to_word(n)
        else:
            digit = ''

        result = trillion+billion+million+thousand+digit
    return result

if __name__ == '__main__':
    main()