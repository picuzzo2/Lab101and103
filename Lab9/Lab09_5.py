
def main():
    decode("aceiklmr-",'''
3
5 3 4 2
3 1 2 8 1 7 2 0    86 -1 -2
''')

def decode(code_table,text):
    x=0
    text = text.strip()
    column = text.split('\n')
    while x< len(column):
        
        y = column[x].split(' ')
        for i in range(len(y)):
            if y[i].isdigit()==True or "-" in y[i]:
                if 0 <= int(y[i]) < len(code_table):
                    print(code_table[int(y[i])],end='')
                else:
                    print('_',end='') 
        

        print('')
        i=0

        x=x+1

if __name__ == '__main__':
    main()

