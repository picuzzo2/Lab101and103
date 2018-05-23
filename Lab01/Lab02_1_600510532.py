def main():
    x = input()
    print(string_to_signed_int(x))

def string_to_signed_int(x):
    simbol = x[0]
    rest = x[1:] 
    count = len(x)-2
    result = -int(simbol)*(2**(count+1))  
    for i in rest:
        result += int(i)*2**count
        count-=1
    return(result)

if __name__ == '__main__':
    main()