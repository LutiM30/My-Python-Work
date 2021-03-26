# DONE 14)Pelindrome
#Write a program that takes the string and check that the string is pelindrome or not. Example : MADAM - Pelindrome (Mandatory)

checkit=input("Enter Any String To check for Pelindrome: ")
checkit=checkit.upper()
print("Your String is: ",checkit)
split = [char for char in checkit]
split.reverse()

spaces=None
for index in split:
    if spaces is None:
        spaces=index
    else:
        spaces=spaces+index
if spaces != checkit:
    print("Reverse Is : ",spaces,"\n They ARE NOT PALINDROME!")

else:
    print("Reverse Is : ",spaces,"\n They ARE PALINDROME!")