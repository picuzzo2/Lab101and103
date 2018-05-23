#600510532 SEC1

def main():
    x = int(input())
    b = int(input())
    print(is_palindrome(x,b))

def is_palindrome(x,b):
    result = 0
    result1 = 0
    i = 0
    while x != 0:
        mod = x%b
        result += mod*(10**i)
        x = x//b
        i +=1

    x1 = result
    y = len(str(result)) - 1
    while x1 != 0:
        mod1 = x1%10
        result1 += mod1*(10**y)
        x1 = x1//10
        y -= 1
    #print(result,result1)
    if result1 == result:
        return True
    else:
        return False
 

if __name__ == '__main__':
    main()