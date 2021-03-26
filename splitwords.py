# 2)PrintLetter
# #Write a program that takes one string from user as input and print that string in as individual letters on each line. (Mandatory)
i=input("Enter STRING:")
letters=list()
letters[:] = i
try:
    letters.remove(" ")
except:
    print(letters)
print(letters)