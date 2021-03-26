# 6)Alphabet
# #Write a program that takes one string as input , now check whether string is alphabet or a digit. (Mandatory)
while True:
    check=input("Enter any String to Quit the program")
    try:
        check=int(check)
        print("You have entered Numbers Do it Again")
        continue
    except:
        print("You can Go Now")
        quit()