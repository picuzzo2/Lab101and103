from operator import itemgetter

def main():
    list_x = ["11/1/2100", "15/12/1999", "5/12/2001", "11/9/2001"]
    sort_date(list_x)
    print('---')
    print(list_x)

def sort_date(list_x):
    for i in range(len(list_x)):
        list_x[i] = list_x[i].split('/')
    
    list_x.sort(key = itemgetter(2,1,0))
    
    #for i in range(3):
    #    list_x.sort(key = lambda list_x:list_x[i][0])
    #    print('---')
    #    print(list_x)
    #seen = []
    











    for i in range(len(list_x)):
        list_x[i] = '/'.join(list_x[i])
    #list_x = 0
    #list_x[0],list_x[1] = list_x[1], list_x[0]




if __name__ == '__main__':
    main()