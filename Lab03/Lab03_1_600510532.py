def main():
    information_gain('Country of origin')

def information_gain(feature):
    ### SPLIT DATA FROM TXT FILE ###
    ################################
    list_data=[]
    data = open('eiei.txt','r')
    j=0
    for i in data:
        list_data.append(i.split(','))
        list_data[j][4] = list_data[j][4].split()
        j+=1
    print(list_data)


    #return (1-P(USA)) * (E(USA)-P(Europe)) * (E(Europe)-P(Rest of world))*E((Rest of world))

if __name__ == '__main__':
    main()