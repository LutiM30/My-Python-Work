#10# Write a program that print the current sum value where sum = 0 and var = 1 initially. Continue the process until user enters 0.(while) (Mandatory)
add=0
var=1
userinput = None
while userinput != 0:
    try:
        userinput=int(input('Enter The Value: '))
    except : 
        print("Enter Numbers ")
        continue
    if userinput == 0:
        break
    else: add=var+userinput
    print('{} + {} = {}'.format(var, userinput, add))