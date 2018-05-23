#Keattisak wongsathan 
#600510532 SEC002

import math
def main():
    factor_list()

def factor_list():
    new_data = []
    ### SPLIT DATA FROM TXT FILE ###
    ################################
    list_data=[]
    data = open('eiei.txt','r')
    j=0
    for i in data:
        list_data.append(i.split(','))
        list_data[j][4] = list_data[j][4].split()
        j+=1

    ### FACTOR LIST ###
    ###################
    headData =['Country of origin','Big Star','Genre']
    sortList =[]
    decision = {information_gain(headData[0],list_data):headData[0],information_gain(headData[1],list_data):headData[1],information_gain(headData[2],list_data):headData[2]}
    for i in decision:
        sortList.append(i)
    sortList.sort(reverse=True)
    feature = decision[sortList[0]]
    print('First factor is',feature)
    headData.remove(feature)
    
    ### Check feature ###
    #####################
    j=0
    seen=[]
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

    ### FACTOR LIST 2 ###
    #####################
    tempoSetSort = {}
    tempoSort = []
    #print(seen)
    for i in seen:
        
        for k in list_data:
            if i in k:
                new_data.append(k)
        #print(i)
        for l in headData:
            decision = information_gain(l,new_data,E(i,list_data))
            tempoSetSort[decision] = l
            #print(l)
            #print(tempoSetSort)
        for item in tempoSetSort:
            tempoSort.append(item)
        tempoSort.sort(reverse=True)
        if tempoSort[0] != 0 :
            print('The next factor of %s is'%i,tempoSetSort[tempoSort[0]])
        else:
            pass
        #print(tempoSort[0])
        #print(tempoSort)
        tempoSort = []
        new_data=[]
        #seen[i]
        tempoSetSort = {}
    



def information_gain(feature,list_data=None,informationGain = 1):   
    
    ### Check feature ###
    #####################
    j=0
    seen=[]
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
    #print(seen)

    ### CALCULATE INFORMATION GAIN ###
    ##################################

    for i in seen:
        informationGain -= P(i,list_data)*E(i,list_data)
    return informationGain
    
def E(S,list_data):
    p = []
    prob1 = 0
    prob0 = 0

    for k in list_data:
        if S in k:
            if k[4][0] == 'true':
                prob1+=1
            elif k[4][0] == 'false':
                prob0+=1
   
    p.append((prob1/(prob1+prob0)))
    p.append((prob0/(prob1+prob0)))
    
    try:
        result = -p[0]*math.log2(p[0]) - p[1]*math.log2(p[1])
    except:
        result = 0
    return result
    
def P(S,list_data):
    seen = 0
    for i in list_data:
        if S in i:
            seen+=1
    result = seen/len(list_data)
    return result
    
if __name__ == '__main__':
    main()