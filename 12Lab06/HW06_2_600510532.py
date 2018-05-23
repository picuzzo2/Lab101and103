def main():
    list_x = [3, 7, 4, 9, 5, 2, 6, 1]
    merge_sort(list_x, True)
    print('--------')
    print(list_x)

def merge_sort(list_x,show_step = False):
    
    if len(list_x)>1:
        mid = len(list_x)//2
        lefthalf = list_x[:mid]
        righthalf = list_x[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                list_x[k]=lefthalf[i]
                i=i+1
            else:
                list_x[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            list_x[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            list_x[k]=righthalf[j]
            j=j+1
            k=k+1
    



if __name__ == '__main__':
    main()