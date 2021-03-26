#16#Write a program that takes the user input until the user enters the string "quit" (break statement) (Mandatory)
while True:
    user =str(input("Enter the EXIT to exit the program:"))
    user=user.upper()
    if user == "EXIT":
        print('GOODBYE')
        quit()
    else:
        print('this is Your INPUT: ',user)
        continue