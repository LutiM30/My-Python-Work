#18)linearSearch
# Write a program of Linear Search using list. (Mandatory)
list1=[]
while True:

    value=str(input('\nENter VALUE in list 1\nenter exit for exit from list 1: '))
    value=value.lower()
    
    if value == 'exit':
        
        print('this is 1st list = ',list1)
        break
    
    else:
    
        list1.append(value)

while True:
    search=input('Enter Word To Find in List 1: ')
    search=search.lower()

    if search in list1:
        print('{} is in list1'.format(search))
    else: print('{} is not in list1'.format(search))