
def main():
    list_x = ['11/1/2100','5/12/2100','19/1/2100','11/9/2100'] # 3,4,7,9
    sort_date(list_x,True)
    print('---')
    print(list_x)

def sort_date(list_x , show_step = False):
    for i in range(len(list_x)):
        list_x[i] = list_x[i].split('/')
    i = 0

    while i+1 < len(list_x):   
        # First swap
        date1,date2 = list_x[i],list_x[i+1]
        if less_than(date1,date2):
            list_x[i],list_x[i+1] = list_x[i+1],list_x[i]
            i+=1
        else:
            i+=1

        # Back swap
        if i-2 >= 0:
            tempo_i = i
            while i > 1:
                i-=1
                date2,date1 = list_x[i],list_x[i-1]
                if less_than(date1,date2):
                    list_x[i],list_x[i-1] = list_x[i-1],list_x[i]
            i = tempo_i


        if show_step == True:
                print('%d: ['%i,end='')
                for k in range(len(list_x)):
                    print("'",end='') 
                    print('/'.join(list_x[k]),end='')
                    print("'",end='')
                    if k+1 < len(list_x):
                        print(', ',end='')

                print(']')
    for i in range(len(list_x)):
        list_x[i] = '/'.join(list_x[i])

def less_than(date1,date2):
    if int(date1[2]) != int(date2[2]):
        i = 2
    elif int(date1[1]) != int(date2[1]):
        i = 1
    else:
        i = 0

    if int(date1[i])>int(date2[i]):
        return True
    else:
        return False
      



        

if __name__ == '__main__':
    main()


  #if list_x[i][j] > list_x[i+1][j]:
   #         list_x[i],list_x[i+1] = list_x[i+1],list_x[i]    #swap i0 and i1
    #        i+=1                                                           #set new i
   #         if i-1 >0:
   #             while list_x[i-1][j] < list_x[i-2][j]:                     #LOOP WHILE #compare i-1 and i-2
    #                list_x[i-1],list_x[i-2] = list_x[i-2],list_x[i-1]
  #      else:
   #         i+=1
        