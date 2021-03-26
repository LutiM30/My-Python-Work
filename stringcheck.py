# 17)StringCompare
#Write a program that compares two string and print the message accordingly whether they are equal , first string is smaller or bigger then the second. (Mandatory)
string1=input("Enter The First String")
string2=input("Enter The Second String")
split1 = [char for char in string1]
split2 = [char for char in string2]

if len(split1) == len(split2):
    print('Both have the same lengths')

elif len(split1) > len(split2):
    print(string1 ,"is Greater than" , string2)

else: print(string1 ,"is Smaller than" , string2)