import time 

def countdown_timer(seconds):
    while seconds > 0:
        min = int(seconds / 60)
        sec = int(seconds % 60)
        if min < 10:
            timer = f'0{min}:{sec}'
        else:
            timer = f'{min}:{sec}'
        if sec < 10:
            timer = f'{min}:0{sec}'
        else:
            timer = f'{min}:{sec}'
        print(timer,end='\r')
        time.sleep(1)
        seconds -= 1
    print('time is up')

seconds = int(input("enter the time in seconds:  "))
countdown_timer(seconds)
