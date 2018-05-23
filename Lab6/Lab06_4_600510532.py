#!usr/bin/env python3
# keattisak wongsathan
# 600510532
# Lab 06
# Problem 4
# 204111 SEC 001

def main():
    x = int(input('Total students: '))
    print('Enter score:')
    student(x)

def student(x):
    y = 0
    top = 0
    runner_up = 0
    count = 0
    all_plus = 0
    for i in range(x):  
        y = int(input())            #loop input y
        d = y
        all_plus += d
        count +=1
        if y > top:                #Runneriup
            runner_up = top
        if y >= top:               #MAX
            top = y
        elif runner_up< y < top:
            runner_up = y          #RUNNERUP replace max
    av = all_plus/count #ave
    print('---')
    print('Max score is: %.2f'%top)
    if int(runner_up) == 0:
        runner_up = None
        print('Runner up is: ',end='')
        print(runner_up)
    else:
        print('Runner up is: %.2f'%runner_up)
    print('Average is: %.2f'%av)
        
       

        

if __name__ == '__main__':
    main()