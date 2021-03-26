
import time

def countdown(secs):
    while secs:
        mins,secs= divmod(secs,60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer,end='\r')
        time.sleep(1)
        secs-=1

    print('TIMER DONE')

while True:
    secs= input('Enter The Time in Seconds: ')
    
    try:
        secs= int(secs)
        break
    except:
        print('Invalid Input')
        continue

countdown(secs)