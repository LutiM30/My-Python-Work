#6)Queue
#Write a program that implements Queue data structure using lists to insert and delete items. (Mandatory)

from collections import deque
list=[]
while True:
    value=str(input('\nENter VALUE in list\nenter exit for exit from list: '))
    value=value.casefold()
    if value == 'exit':
        print('this is list = ',list)
        break
    else:
        list.append(value)

while True:
    inp=input('''<<<Enter Which Operations You Want To Perform>>>
    1>POP Operations
    2>PUSH Operations
    3>Quit Program
    Your Response:  ''')
    try:
        inp=int(inp)
    except:
        print('Invalid Input! \n Try Again!')
        continue
    if inp in [1,2,3]:
        if inp == 1 :
            print('This One Is REMOVED FROM Queue',list.pop())

        if inp == 2: 
            push=input('Enter Which One You Want to ADD:  ')
            list.append(push)
            print(list)

        if inp == 3: quit()

    else:
        print('Invalid Input! \n Try Again!')
        continue
    while True:
        again=input('Do You Want to do it AGAIN>\n Y For YES \n N For NO \n Your Response: ')[0].upper()
        if again == 'Y': break
        if again == 'N': quit()
        else : 
            print('Invalid Input')
            continue