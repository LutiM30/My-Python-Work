#4)ConcateWith+
#Write a program that contains 3 lists , concatenate with '+' operator . Print Values on the screen.

list1 =[]
list2 =[]
list3 =[]
while True:
    value1=str(input('\nENter VALUE in list\nenter exit for exit from list1: '))
    value1=value1.casefold()
    if value1 == 'exit':
        print('this is list1 = ',list1)
        break
    else:
        list1.append(value1)

while True:
    value2=str(input('\nENter VALUE in list\nenter exit for exit from list2: '))
    value2=value2.casefold()
    if value2 == 'exit':
        print('this is list2 = ',list2)
        break
    else:
        list2.append(value2)

while True:
    value3=str(input('\nENter VALUE in list\nenter exit for exit from list3: '))
    value3=value3.casefold()
    if value3 == 'exit':
        print('this is list3 = ',list3)
        break
    else:
        list3.append(value3)
    
print(list1+list2+list3)