# #UnDONE # Write a program that takes a variable and initialize with 100 (Mandatory)
# #Check the following conditions.
# #Now check the var with various values like 200 , 150 ,100 and print the messages accordingly unless you get the same value.
# #If you don't get it then print the message unsuccessful.

Check_List =[]
while True:
    
    Check_List_Value = input('Enter Values to List: ')
    
    if Check_List_Value in ['Done', 'done','DONE']:
        break

    else:
    
        try:
            Check_List_Value=int(Check_List_Value)
        
        except:
            print('Invalid Input')
            continue

        Check_List.append(Check_List_Value)
    
while True:

    User_input=input("Enter The Value to Find in List: ")
    try :
        User_input=int(User_input)

    except :
        print('INVALID INPUT')
        continue

    if User_input in Check_List:
        print('FOUND IT !!! it is at',Check_List.index(User_input)+1)
        break

    else:
        print('{} is NOT IN THE LIST Try Again! '.format(User_input))
        continue