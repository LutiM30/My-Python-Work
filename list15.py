#15)FruitList
#Write a program that creates a fruitlist of say 5 items.First sort the list.Print the list .Now delete the first item from the list and then print the list. (Mandatory)

FruitList=[]
while True:

    Fruit=str(input('\nENter Fruit in FruitList\nenter exit for exit from FruitList: '))
    Fruit=Fruit.lower()
    
    try:
        Fruit=int(Fruit)
        print('Fruits Have Names Not NUMBERS')

    except:
        if Fruit == 'exit':
            
            print('this is 1st list = ',FruitList)
            break
        
        else:
        
            FruitList.append(Fruit)

FruitList.sort()
print('Sorted Fruitlist = ',FruitList)

while True:
    
    pop_op=input('''ENTER INDEX NUMBER OF FRUIT FROM FRUIT LIST TO REMOVE IT
    Fruitlist = {} 
    your input: '''.format(FruitList))
    
    try:
        pop_op=int(pop_op)
        break
    
    except:
        print('Invalid Input')
        continue

FruitList.pop(pop_op-1)
print('Updated Fruitlist = ',FruitList)