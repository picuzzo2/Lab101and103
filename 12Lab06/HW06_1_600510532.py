def main():
    list_x = [1014, 68, 264, 603, 938, 1565, 798, 11, 834, 1129]
    radix_int(list_x,True)
    print('--------')
    print(list_x)


def radix_int(list_x,show_step = False):
    radix = [[],[],[],[],[],[],[],[],[],[]]
    div = 1
    mod = 10
    while len(radix[0]) != len(list_x):
        radix = [[],[],[],[],[],[],[],[],[],[]]
        for i in list_x:
            target = (i%mod)//div
            radix[target].append(i)
            
        del list_x[0:len(list_x)]
        for i in radix:
            if len(i) > 0:
                for j in i:
                    list_x.append(j)        
        div*=10
        mod*=10

        if show_step == True:
            if radix[0] != list_x:
                print(list_x)

if __name__ == '__main__':
    main()