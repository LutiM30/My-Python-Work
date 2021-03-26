#10)operator+=
#Write a program that adds an item to the end of the list using "+=" operator. (Mandatory)

list=[]
while True:
    value=str(input('\nENter VALUE in list\nenter exit for exit from list: '))
    value=value.lower()
    if value == 'exit':
        print('this is list = ',list)
        break
    else:
        list+=[value]