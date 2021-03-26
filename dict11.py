#11)CreateDict
#Write a program that creates one dictionary that conatains Name ,Address pair..Minimum having 10 records.Also print the records. (Mandatory)

AddBook={}

while True:
    Name=input('Enter Name that you want to add in Address Book\nEnter exit if you want to stop adding\nEnter Here:  ')
    if Name in ['exit','Exit','EXIT']:
        break
    else:
        Address=input('ENTER Address OF {}: '.format(Name))
        AddBook[Name]=Address

print('Your Address Book Is',AddBook)