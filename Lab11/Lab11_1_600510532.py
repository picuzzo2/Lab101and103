#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 11
# Problem 1
# 204111 SEC 001

def main():
    m1 = [[5,3],[1,3],[9,3],[1,-1000]]
    m2 = [[1,3,3],[2,4,3]]
    print(matrix_mult(m1,m2))

def matrix_mult(m1,m2):
    m3=[]
    m4=[]
    for i in range(len(m1)):
        tempo_m1=m1[i] 
        for j in range(len(tempo_m1)):
            tempo_m2=m2[j]
            for k in range(len(tempo_m2)):
                if len(m3) < k+1:
                    m3.append(tempo_m1[j]*tempo_m2[k])
                else:
                    m3[k]=m3[k]+(tempo_m1[j]*tempo_m2[k])
        m4.append(m3)
        m3=[]
    if len(m1[0]) != len(m2):
        return None
    else:
        return m4
                
if __name__ == '__main__':
    main()
