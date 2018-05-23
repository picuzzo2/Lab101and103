# -*- coding: utf-8 -*-
# @Author: CSB307
# @Date:   2018-03-30 03:57:19
# @Last Modified by:   CSB307
# @Last Modified time: 2018-03-30 05:42:12
import math

def main():
    factor_list()
    

def information_gain(feature):
    #feature : Country of origin ;Big star; Genre

    ### Split data ###
    list_data=[]
    data = open('eiei.txt','r')
    j=0
    for i in data:
        list_data.append(i.split(','))
        list_data[j][4] = list_data[j][4].split()
        j+=1
    #print(list_data)
    
    ### Check feature ###
    j=0
    seen=[]
    #print(list_data)
    for i in list_data:
        if feature == 'Country of origin':
            target = list_data[j][1]
        elif feature == 'Big Star':
            target = list_data[j][2]
        elif feature == 'Genre':
            target = list_data[j][3]
        j+=1
        #print(target)
        if target not in seen:
            seen.append(target)



    ### Calculate entropy ###
    j=0
    prob = []
    #print(list_data)
    for i in seen:
        prob1 = 0
        prob2 = 0
        for k in list_data:
            if i in k:
                if k[4][0] == 'true':
                    prob1 +=1
                elif k[4][0] == 'false':
                    prob2 +=1
                  
        prob.append([prob1/(prob1+prob2)])
        prob[j].append((prob2/(prob1+prob2)))
        j+=1
    #print(prob)
    ent =[]
    for i in range(len(prob)):
        p1=prob[i][0]
        p0=prob[i][1]
       # print(p1,p0)
        try:
            ent.append(-(p1)*math.log2(p1)-(p0)*math.log2(p0))
        except:
            ent.append(0) 
    #print(ent)

    ### Calculate Prop ###
    finalProb = []
    for i in seen:
        j=0
        tempoProb = 0
        for k in list_data:
            if i in list_data[j]:
                tempoProb +=1
            j+=1
        finalProb.append(tempoProb/len(list_data))
    #print(finalProb)
    
    infor = 1
    for i in range(len(ent)):
        infor -= (finalProb[i] * ent[i])
    
    return infor




def factor_list():
    
    a = 'Country of origin'
    b = 'Big Star'
    c = 'Genre'
    sortList = [information_gain(a),information_gain(b),(information_gain(c))]
    sortList.sort(reverse = True)
    tempoSortedList = []
    dictList=dict([(information_gain(a),a),(information_gain(b),b),(information_gain(c),c)])
    for i in range(len(sortList)):
        tempoSortedList.append(dictList[sortList[i]])
    print(tempoSortedList)
    print('First factor is',tempoSortedList[0])
    print('The next factor of USA is',tempoSortedList[1])
    print('The next factor is Europe is',tempoSortedList[2])
    #print(sort)


if __name__ == '__main__':
    main()