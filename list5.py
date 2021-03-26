#5)compareLists
# Write a program that compares two lists with "==" and "is" operators..Print both the output on screen. (Mandatory)
list1 =[]
list2 =[]
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

print(list1==list2) 
print(list1 is list2)