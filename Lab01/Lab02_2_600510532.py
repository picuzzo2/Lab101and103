def main():
    x = input()
    print(two_complement(x))

def two_complement(x):
    mod = 10
    floor = 1
    x1 = int(x)
    z = 0
    for i in range(len(x)):
        y = (x1%mod)//floor
        if y ==1 :
            z+=1*10**i
            x1+=1*10**(i+1)
        if y ==2:
            x1+=1*10**(i+1)
        mod*=10
        floor*=10

    x1 = (len(x)-len(str(z))) * '0' + str(z)
    simbol = x1[0]
    rest = x1[1:] 
    count = len(x1)-2
    result = -int(simbol)*(2**(count+1))  
    for i in rest:
        result += int(i)*2**count
        count-=1
    return(x1,result)




if __name__ == '__main__':
    main()