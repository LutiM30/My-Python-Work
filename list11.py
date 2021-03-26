#11)Print3rdList
#Write a program that creates two lists with some values in them.Now create a third list which contains these two lists.Print the data of the third list on the screen. (Mandatory)

list1=[]
list2=[]

while True:
    value=str(input('\nENter VALUE in list 1\nenter exit for exit from list 1: '))
    value=value.lower()
    if value == 'exit':
        print('this is 1st list = ',list1)
        break
    else:
        list1.append(value)

while True:
    value=str(input('\nENter VALUE in list 2\nenter exit for exit from list 2: '))
    value=value.lower()
    if value == 'exit':
        print('this is 2nd list = ',list2)
        break
    else:
        list2.append(value)

list3 = list1+list2

print('This is 3rd list = ',list3)