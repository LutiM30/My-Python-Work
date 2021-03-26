# 7)Justification
# #Write a program that takes one string as input and print the string with center , right and left justification. (Mandatory)
string=input("Enter String : ")
print("Your String is: ",string)

print("Your left Aligned String is : \n")
print(string.ljust(40, "#"))

print("Your Right Aligned String is : \n")
print(string.rjust(40, "#"))

print("Your left Aligned String is : \n")
print(str.center(string40, "#"))