
def main():
    m1 = [[1,2,3],[4,5,6]]
    m2 = [[7,8],[9,10],[11,12]]
    matrix_mult(m1,m2)

def matrix_mult(m1,m2):
    m3=[]
    m4=[]
    m5=[]
    for i in range(2):  #m1 do 2round
        for k in range(len(m2[0])):  ##do 2 sets
            result = 0
            for j in range(len(m2)):  ###do 3round per set
                result = m1[i][j]*m2[j][k]
                m3.append(result)
            m3= sum(m3)
            m4.append(m3)
            m3=[]
        m5.append(m4)
        
    return m4

if __name__ == '__main__':
    main()

