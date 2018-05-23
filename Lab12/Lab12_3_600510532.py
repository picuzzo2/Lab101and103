#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 12
# Problem 3
# 204111 SEC 001

import string
def main():
    text = '''
    He doesn't ###want### to pay $40,000 for a new car,%$^$
                             but his wife doesn't 'seem' to care.
    '''
    print(word_count(text))

def word_count(text):
    text = text.lower()
    text = text.split()
    word = {}
 

    for key in text:
        key = key.strip(string.punctuation)
        if key not in word:        
            word[key] = 1
        else:
            word[key] += 1


    return word


if __name__ == '__main__':
    main()