import threading
response = None #define Global Variable

def user_input():
#assign input to global variable
    global response #use keyword global here
    response = input("What is your name? ")

def main():
    time = timer()
    for i in range(5):
        #user_input()
        time.start()
        if response is None:
            print('No Human')
        else:
            print("Hello,", response)

class timer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for i in range(5):
            print(i)
            time.sleep(1)
        #time.sleep(5)
        return

if __name__ == '__main__':
    main()