#2)InsertList
#Write a program that inserts a value in the list using 'insert' method. (Mandatory)

list = []
for num in range(10):
    add=str(input('ENTER VALUE TO INSERT IN LIST: '))
    list.insert(num, add)

print(list)