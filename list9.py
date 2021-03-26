#9)Operater*
# Write a program that modifies the existing list with N times using "*" operator. Example : [1,2] * N  (Mandatory)

list=[]
while True:
    value=input('\nENter VALUE in list\nenter exit for exit from list: ')
    if value == 'exit':
        print('this is list = ',list)
        break
    else:
        try:
            value=int(value)
            list.append(value)
            # print('this is list = ',list)
        except:
            print('Invalid Input\nTry Again!')
            continue
while True:
    ntimes=input('Enter Multiplcation Number: ')
    try:
            ntimes=int(ntimes)
            break
    except:
        print('Invalid Input\nTry Again!')
        continue


print('{} * {} = {}'.format(list,ntimes,list*ntimes))