#12)SlicinList
#Write a program that creates a list that contains the value [0,1,2,3,4,5,6,7,8,9].Performt the follwoing operations on the list with slicing : Output 1 : [0,1,2] Output 2 : [5,6,7,8,9] (Mandatory)

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
    
    till = input('Enter a word in the list that you want to slice from it:  ')
    
    if till not in list1:
        
        print('{} is not in list 1, List1 is {}'.format(till,list1))
        continue
    
    else:
        
        for i in list1:
            
            if i != till:
                
                list2.append(i)
                
            if i==till:
                
                break
        
        for i in list1:
            
            if i != till:
                list1.remove(i)

            if i==till:
                list1.remove(i)
                break
    
        for i in list1:
            for j in list2:
                if i==j:
                    list1.remove(i)

        break
print(list2,list1)