import threading
import time
import random


score = 0
playerAnswer = None

def main():
    global score 
    for i in range(3):
        Q = generate_question()
        print(Q)
        question= Q[0]
        result= Q[1]
        #score += play_question(question,result)
        global user
        user = threading.Thread(target=play_question,args=(question,result,))
        #user.daemon = True
        user.start()
        for j in range(5):
            user.join(1)
        if playerAnswer is None:
            print('Time out')


        

        

    print("You've got:",score)


def play_question(question,result):
    life = 3
    print(life)
    #print(question)
    Answer = False
    global playerAnswerd
    playerAnswer = None
    global score
    while not Answer:


        if life>0: 

            while True:
                try:
                    playerAnswer = int(input('%s = '%question))
                    break
                except:
                    print('Answer should be integer only, try again')

            if playerAnswer == result:
                print('Correct!')
                score +=1
                Answer = True
                break
                
            else:
                life -= 1
                print(life) 
                if life >0:
                    print('Try again %s time(s) left'%life)
                else:
                    print('Too many try')
            
        
        else:
            break



def generate_question():
    v1 = random.randrange(99)
    v2 = random.randrange(99)
    question = '%d+%d'%(v1,v2)
    result =v1+v2
    return question,result




if __name__ == '__main__':
    main()
