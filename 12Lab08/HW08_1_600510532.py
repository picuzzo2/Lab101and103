# -*- coding: utf-8 -*-
# @Author: CSB307
# @Date:   2018-02-09 02:56:43
# @Last Modified by:   CSB307
# @Last Modified time: 2018-03-09 11:29:31
# 600510532 SEC2
# Keattisak wongsathan 
import datetime
def main():
    rand_sym()

def rand_sym():
    print('p for Paper, r for Rock, s for Scissor')
    print('--------')
    playerScore = 0
    compScore = 0
    i=0
    while i <3 and playerScore <2 and compScore <2:
        print('Turn',i+1)
        Player = input()  #STR input1
        Player = forComfy(Player)

        Comp = datetime.datetime.now().microsecond % 3
        Comp = forComfy(Comp)

        print('You choose',Player)
        print('Computor choose',Comp)
        check = checkWin(Player,Comp)
        if check != 'Draw':
            print('You',check)
            if check == 'Win':
                playerScore += 1
            else:
                compScore +=1
        else:
            print(check)
            
        print('--------')
        i+=1
    print('******************')
    if playerScore > compScore:
        print("You win")
    elif playerScore == compScore:
        print('Draw')
    else:
        print('Computer win')


def checkWin(Player,Comp):
    if Player == Comp:
        result = 'Draw'
    elif Player == 'Rock':
        if Comp == 'Scissor':
            result = "Win"
        else:
            result = 'Lose'
    elif Player == 'Scissor':
        if Comp == 'Rock':
            result = 'Lose'
        else:
            result = 'Win'
    else:
        if Comp == 'Scissor':
            result = 'Lose'
        else:
            result = 'Win'
    return result

def forComfy(sim):
    if sim == 1 or sim == 'p':
        result = 'Paper'
    elif sim ==2 or sim == 'r':
        result = 'Rock'
    elif sim ==0 or sim == 's':
        result = 'Scissor'
    return result

# rock win sc
# sc win paper
# paper win rock
        



if __name__ == '__main__':
    main()