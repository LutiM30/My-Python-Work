#9)vegetable
#Write a program that create a dictionary "vegetable" with key and vaule like {'tomato':'red'}.Now keys in alphabetical order for the same dictionary. (Mandatory)
vegetables=[]
vegs={}

Total=0

while True:
    vegetable = input('\nEnter Which vegetable You Want to Add \n Enter Exit To Exit from it\nEnter Here: ').lower()
    try:
        vegetable =int(vegetable)
        print('ENTER vegetable NOT NUMBER!!!')
        continue
        
    except:

        if vegetable in ['Exit' , 'exit']:
            break
        else:
            vegetables.append(vegetable)
            print(vegetables)
            Total+=1


# veg=vegetables.sort()
vegetables.sort()

for vegetable in vegetables:
    while True:
        color = input('ENTER COLOR of {} '.format(vegetable))
        try:
            color =int(color)
            print('ENTER COLOR NOT NUMBER!!!')
            continue
        
        except:
            vegs[vegetable]=color
            break

print('SORTED WAY: ',vegs)