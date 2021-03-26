#1)#Write a program that creates one dictionary that conatains Name ,Address pair..Minimum having 10 records.Also print the records. (Mandatory)
#2)ADS
#In the above program Add , Delete and search records with various attributes. (del ,has_key) (Mandatory)
#3)Dict
#Create  a dictionary.Change the exixting value for one key. Delete one item from it. Add one item to it. Print everything on screen (Mandatory)
#11Method
#Write a program that shows the use of copy and clear method on the dictionary.
dict={}
i=0

while i<=3:
    key = str(input('Enter Which Record You want to Create: '))
    value = str(input("\nEnter VALUE in '{}':  ".format(key)))
    dict[key]=value
    i+=1

while True:
    options = input('''<<<THIS ARE AVAILABLE OPERATIONS>>>
    1> Delete Record
    2> Search Record
    3> Change Record
    4> Copy Dictionary
    5> Delete Dictionary
    6> Quit
    Enter Your OPTIONS:  ''')

    try:
        options =int(options)
        if options>6: 
            print('Invalid Input')
            continue

    except:
        print('Invalid Input')
        continue

    if options==1:
        delrec=input('Enter Which Record You want to Delete: ')
        if delrec in dict:
            del dict[delrec]
            print('Deleted Record is {} \n Updated Dictionary {}'.format(delrec,dict))
    
        else: 
            print('No record Found named ' + delrec)
            continue

    elif options==2:
        foundrec=input('Enter Which Record You want to Search: ')
        if foundrec in dict:
            print('FOUNDED {} Value: {}'.format(foundrec,dict.get(foundrec)))
        else :
            print('No record Found named ' +foundrec)
        
    elif options==3: 
        chngrec=input('Enter Which Record You want to Change:  ')
        
        if chngrec in dict:
            newvalue=input('FOUNDED {} Value: {} \nEnter New Value To add in it: '.format(chngrec,dict.get(chngrec)))
            dict[chngrec]=newvalue
            print(dict)
            
        else :
            print('No record Found named ' +chngrec)
    
    elif options== 4: 
        dict2=dict.copy()
        print('This is COPY of Dictionary 1: ',dict2)

    elif options==5: 
        dict.clear()
        print('This is Dictionary 1 After Clearing it: ',dict)

    elif options==6: quit()

    while True:
        clarify=input('You want to Do it Again??? \n Y for Yes \n N for No \n Enter Your Choice: ')[0].upper()
        if clarify == 'Y':
            break
        elif clarify == 'N':
            quit()
        else: continue