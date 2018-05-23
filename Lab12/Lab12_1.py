
def main():
    list_a = [(2, 7, 1.5), 
(3.2, 2.5, 4.06), 
(-5.5, -4.5, 2.5),
(2, -5.2, 3), 
(7.2, -2.8, 1.2)]

    print(count_segment(list_a))

def count_segment(list_a):
    for i in range(len(list_a)):
        x = list_a[i][0]
        y = list_a[i][1]
        r = list_a[i][2]

    
        p1 = [y+r,x]
        a=p1[0]
        b=p1[1]
        check(a,b)
        p2 = [x+r,y]
        a=p2[0]
        b=p2[1]
        check(a,b)
        p3 = [y-r,x]
        a=p3[0]
        b=p3[1]
        check(a,b)
        p4 = [x-r,y]
        a=p4[0]
        b=p4[1]
        check(a,b)

    
def check(a,b):
    if a>0 and b>0:
        q1=1
    elif a>0 and b<0:
        q2=1
    elif a<0 and b>0:
        q4=1
    elif a<0 and b<0:
        q3=1
    return q1,q2,q3,q4

if __name__ == '__main__':
    main()