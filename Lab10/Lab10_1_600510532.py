#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 10
# Problem 1
# 204111 SEC 001


def main():
    str1 = 'Anagram____'
    str2 = 'Nag a ram123'
    print(is_anagram(str1,str2))

def is_anagram(str1,str2):
    
    i1=0
    str1=str1.lower()
    while str1.isalpha() != True:
        if str1[i1].isalpha()==True:
            i1 = i1+1
        else:
            str1=str1.replace(str1[i1],'')
    

    i2=0
    str2=str2.lower()
    while str2.isalpha() != True:
        if str2[i2].isalpha()==True:
            i2 = i2+1
        else:
            str2=str2.replace(str2[i2],'')


    list1=sorted(str1)
    list2=sorted(str2)
    if list1==list2:
        return True
    else:
        return False


    #str2
    #str2 = str2.replace(' ','')
    #str2 = str2.lower()
    #list2 = sorted(list(str2))
    #print(list2)

    #if list1 == list2:
        #return True
    
    #else:
        #return False

if __name__ == '__main__':
    main()