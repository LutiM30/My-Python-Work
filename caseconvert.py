# 4)CaseCovert
#Write a program that takes a string from the user and print the string in both uppercase and lowercase. (Mandatory)
while True:
    string=input("Enter the string : ")
    try:
        string=int(string)
        print("ENter Words Not Numbers ")
        continue
    except:
        break

print("UPPERCASE version Of Your String is : \n",string.upper())
print("lowercase version Of Your String is : \n",string.lower())
