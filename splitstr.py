# 10)SpliteStr
# #Write a program that takes one string and split that string by another string. Example .. String = "MyHelloName" After Splitting by the word "Hello" Output = ['My Name'] (Mandatory)
import re
string1=input("Enter 1st String: ")
res_list = re.findall('[A-Z][^A-Z]*', string1)
check=[]

while True:
    string2=input('Enter Word That You want to take out of string: ')
    string2=string2.rstrip()
    string2=string2.lstrip()


    for i in res_list:
        if i != string2:
            continue
        else:
            res_list.remove(string2)
        break
    break

spaces=None
for index in res_list:
    if spaces is None:
        spaces=index
    else:
        spaces=spaces+" "+index

print(spaces)