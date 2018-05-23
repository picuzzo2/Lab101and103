def main():
    a = multiply_polynomials([1,0,5],[1,-19,9])
    print(a)

def multiply_polynomials(p1,p2):
    max = len(p1)-1 + len(p2)-1 +1
    p3 = [[] for i in range(max)]
    poly = lambda x,i: len(x) - (i+1)
    for i in range(len(p1)):
        for j in range(len(p2)):
            p3[poly(p3,poly(p1,i) + poly(p2,j))].        append(p1[i]*p2[j])
    return [sum(p3[i]) for i in range(len(p3))]  

if __name__ == '__main__':
    main()