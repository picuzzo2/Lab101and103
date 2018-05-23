import datetime

def main():
    qrand_dice()


def qrand_dice():
    a = datetime.datetime.now().microsecond
    b = datetime.datetime.now().second
    c = datetime.datetime.now().minute

    a1 = a % c
    b1 = b % c

    a2 = a%b
    b2 = a

    Comp1_x0 = ((a*b)%6)+1
    Comp2_x0 = ((a*c)%6)+1

    c1 = rand(Comp1_x0,a1,b1,c)
    c2 = rand(Comp2_x0,a2,b2,c)

    comp1Result = c1+rand(a*Comp1_x0,a*a1,a*b1,a*c)
    comp2Result = c2+rand(b*Comp2_x0,b*a1,b*b1,b*c)

    print('Computor 1 diced %d and %d result is %d'%(c1,rand(a*Comp1_x0,a*a1,a*b1,a*c),comp1Result))
    print('Computor 2 diced %d and %d result is %d'%(c2,rand(b*Comp2_x0,b*a1,b*b1,b*c),comp2Result))
    #print(comp1Result,comp2Result)

    print('----------------')
    if abs(comp1Result-8) > abs(comp2Result-8):
        print('Computor 2 win')
    elif abs(comp1Result-8) == abs(comp2Result-8):
        print('Draw')
    else:
        print('Computor 1 win')

def rand(x0,a,b,c):
    return (((a*(x0**2))+(b*(x0))+c)%6)+1

if __name__ == '__main__':
    main()