#600510532 SEC1

def main():
    message = input()
    pattern = input()
    patterned_message(message,pattern)

def patterned_message(message,pattern):
    x=0
    message=message.replace(' ','') 
    for i in pattern:
        if i =='*':

            if x == len(message):
                x=0
            if message[x]==' ':
                #x=x+1
                print(i.replace(i,message[x]),end='')
            else:
                print(i.replace('*',message[x]),end='')
            x=x+1
            
            
        elif i == '\n':
            print('')
        else:
            print(' ',end='')



if __name__ == '__main__':
    main()

#patterned_message("Three Diamonds!",'''
#    *     *     *
#   ***   ***   ***
#  ***** ***** *****
#   ***   ***   ***
#    *     *     *
#''')