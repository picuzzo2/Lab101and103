def main():
    code_table = 'aceiklmr-'
    text = '''
3
5 3 4 2
3 1 2 8 1 7 2 0 86
'''
    decode(code_table,text)

def decode(code_table,text):
    x=0
    column = text.strip()
    while x!= len(column):
        #if len(column[x])!=0:
        y = column[x].split(' ')
        for i in range(len(y)):
            if int(y[i]) <= len(code_table):
                print(code_table[int(y[i])],end='')
            else:
                print('_',end='')
        print('')
        i=0

        #else:
        #    print('',end='')
        x=x+1

if __name__ == '__main__':
    main()

