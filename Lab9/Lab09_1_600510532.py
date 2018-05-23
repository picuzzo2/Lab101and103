#600510532 SEC1

def main():
    n = int(input())
    square_frame(n,sep = ' ')

def square_frame(n, sep=' '):
    start = 1
    stop = (n*n) - (n-2)*(n-2)
    for i in range(n-1):
        print('%02d'%start,end='')
        print(sep,end='')
        start += 1
    print('%02d'%start)
    start+=1
    
    for i in range(n-2):
        print('%02d'%stop,end='')
        for i in range((3*n)-5):
            print(sep,end='')
        print('%02d'%start)
        start += 1
        stop -= 1

    for i in range(n-1):
        print('%02d'%stop,end='')
        print(sep,end='')
        stop -= 1
    print('%02d'%stop)



if __name__ == '__main__':
    main()