#5)Telephone
#Create a dictionary which has names and telephone numbers as keys,values (Mandatory)
#This program should give the telephone number of a person given by the user and if the person is not existing in the list then it creates this entry in the dictionary.

TelDict={}

Total=0

while True:
    
    while True:
        name = input('\nEnter Which Name You Want to Add \n Enter Exit To Exit from it\nEnter Here: ')
        
        try:
            name =int(name)
            print('ENTER NAME NOT NUMBER!!!')
            continue
        
        except:
            break

    
    if name == 'exit':
        break
    
    if name in TelDict:
        
        print('{} is Already in TelephoneBook And Number of His/Her is {}:'.format(name,TelDict.get(name)))
        cont=input('Do you want to Continue? \n Y for yes \n N for No \n ENTER HERE: ')[0].upper()
        if cont=='Y': continue
        elif cont=='N': break
        else:
            print('INVALID INPUT \n CONTINUING...')
    else:
        while True:
            number = (input("Enter number in '{}':  ".format(name)))
        
            try:
                number = int(number)
                break
        
            except:
                print("Money Have Numbers Not Words")
                continue
    
    TelDict[name]=number
    Total+=1

#13TelePhoneMenu

# Write a program which shows menu 	 1.Show Phone Number 
#					 2.Add Phone Number 
#					 3.Delete Phone Number
#					 0.Exit.
 # 	Now as per the user input 1,2,3 or 0 the respected operations of Showing Phone Numbers ,
#Addning new phone number and delete a phone number should be performed.All are functions like show_menu, #show_phonelist , add_phone and del_phone.Use dictionary where key is name and value is phone number.
while True:
    options = input('''<<<THIS ARE AVAILABLE OPERATIONS>>>
    1> Show Record
    2> Add Record
    3> Delete Record
    4> Quit
    Enter Your OPTIONS:  ''')

    try:
        options =int(options)
        if options>4: 
            print('Invalid Input')
            continue

    except:
        print('Invalid Input')
        continue

    if options==1:
        shwrec=input('Enter Which Record You want to See: ')
        if shwrec in TelDict:
            print('Number of {} is {}'.format(shwrec,TelDict.get(shwrec)))
        else: 
            print('No record Found named ' + shwrec)
            continue

    elif options==2:
        newrec=input('Enter Which Name You want to Add: ')
        if newrec in TelDict:
            print('{} is Already in TelephoneBook And Number of His/Her is {}:'.format(newrec,TelDict.get(newrec)))
        else :
            newrecnum=input('Enter Number Of {} :'.format(newrec))
            TelDict[newrec]=newrecnum
        
    elif options==3: 

        delrec=input('Enter Which Record You want to Delete: ')
        if delrec in TelDict:
            del TelDict[delrec]
            print('Deleted Record is {} \n Updated Dictionary {}'.format(delrec,TelDict))

    
    elif options==4: quit()
    
    while True:
        clarify=input('You want to Do it Again??? \n Y for Yes \n N for No \n Enter Your Choice: ')[0].upper()
        if clarify == 'Y':
            break
        elif clarify == 'N':
            print(TelDict)
            quit()
        else: continue