
def main():
    p2 = [(5,4),(2,6),(1,34),(0,-8)]
    p1 = [(2,-6),(0,2),(1,1)]
    print(polynomial_addition(p1,p2))

def polynomial_addition(p1,p2):
    p1_1 = sorted(p1)
    p2_1 = sorted(p2)
    p3 = {}
    
    for i in p1_1:
        p3[i[0]] = i[1]

    for i in p2_1:
        try:
            p3[i[0]]+=i[1]
        except:
            p3[i[0]] = i[1]

    p4 = [(x,y) for x,y in p3.items()]
    for i in p4:
        if i[1] == 0:
            p4.remove(i)
    p4 = p4[::-1]

    return p4



    #print(p3)
    #print(p1_1,p2_1)

if __name__ == '__main__':
    main()