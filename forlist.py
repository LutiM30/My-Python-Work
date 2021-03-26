# 13#Write a program that has a list having 5 numbers.Print the sum of all the 5 numbers using a for loop. (Mandatory)
list=[]
sum=None
userinp=None
while True:
    userinp=input("Enter the value: ")
    if userinp == 'DONE':
        for index in list:
            if sum is None:
                sum = index
            else :
                sum = sum + index
        print(sum)
        quit()
    try:
        userinp = int(userinp)
    except: 
        print('\n!!!ENTER NUMBERS!!!')
        continue
    list.append(userinp)