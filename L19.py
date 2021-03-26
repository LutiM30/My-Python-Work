# 19#Write a program that takes the user input until the user enters the string "quit" and if the string length that user inputs is less then three he should be prompted to again enter the string. (Mandatory)
while True:
    inp=str(input("Enter The String: "))
    inp.casefold()
    if len(inp)<=3:
        print("Length of input must be greater than THREE")
        continue
    else:
        print("Your String is : " + inp)
    if inp == 'exit':
        quit()
