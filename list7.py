#7)ListOperation
#Write a program that append an item, sort the items and deletes the item from the list. (Mandatory)
list=[]
while True:
    value=str(input('\nENter VALUE in list\nenter exit for exit from list: '))
    value=value.lower()
    if value == 'exit':
        print('this is list = ',list)
        break
    else:
        list.append(value)

while True:
    inp=input('''<<<Enter Which Operations You Want To Perform>>>
    1>Delete Operation
    2>ADD Operation
    3>Sort Operation
    4>Quit Program
    Your Response:  ''')
    try:
        inp=int(inp)
    except:
        print('Invalid Input! \n Try Again!')
        continue
    if inp in [1,2,3,4]:
        if inp == 1 :
            itemremove=input('Which One You Want to Delete:  ')
            if itemremove in list:
                list.remove(itemremove)
                print('This One Is REMOVED FROM Queue',itemremove)
                print('\n',list)
            else:
                print('item You want to remove from the list is not in the list Try Again!')
                continue
        if inp == 2: 
            push=input('Enter Which One You Want to ADD:  ')
            if push in list:
                print('This One Is ALREADY in LIST',push)
            else:list.append(push)
            print(list)

        if inp == 3:
            while True:
                sorting=input('''<<<Options Of How You can Sort>>>
                1> ascending
                2> descening 
                3> length wise
                Enter Here:  ''')
                try:
                    sorting=int(sorting)
                    if sorting == 1:
                        list.sort()
                        print(type(list))
                        print(list)
                        break
                    
                    if sorting == 2:
                        list.sort(reverse=True)
                        print(list)
                        break
                    
                    if sorting == 3:
                        list.sort(key=len)
                        print(list)
                        break
                except:
                    print('Invalid Input! \n Try Again!')
                    continue

        if inp == 4: quit()

    else:
        print('Invalid Input! \F Try Again!')
        continue
    while True:
        again=input('Do You Want to do it AGAIN>\n Y For YES \n N For NO \n Your Response: ')[0].upper()
        if again == 'Y': break
        if again == 'N': quit()
        else : 
            print('Invalid Input')
            continue