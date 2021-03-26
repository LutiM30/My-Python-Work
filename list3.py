#3)ConcateLists
# Write a program that concatenates two lists , use 'append' and 'extend' methods. (Mandatory)

list1=[]
list2=[]
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
list1.append(list2)
print("Using append",list1)
list1.pop()
list1.extend(list2)
print("Using extend",list1)
