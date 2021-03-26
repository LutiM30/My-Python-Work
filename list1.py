# 1)SampleList
#Write a program that creates a sample list having 5 items and print those using for loop. (Mandatory)list=[]
list=[]
while True:
    items=str(input("Enter The Values To add in LIST \n enter EXIT for stop adding"))
    items=items.casefold()
    if items == 'exit':
        break
    else: list.append(items)

for i in list:
    print(i)

