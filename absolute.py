#5
# Write a program that compute the absolute value of a number.Print appropriate messages for 0 and 1 also. (Mandatory)
while True:
    value =input("Enter any number to get that's absolute value: ")
    try:
        value = float(value)
        break
    except: print("Invalid Input Try Again")


if value == 0.0:
    print('It is Zero')
    
if value == 1.0:
    print('It is One')

else:
    print("Absolute Value is: ",abs(value))