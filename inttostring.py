# 5)IntToString
# #Write a program that converts an integer to string first.Perform some operation on it..Again convert it to integer and perform addition on that. (Mandatory)
while True:
    while True:
        string=input("Enter any number between 0 to 10 \n (ENTER 'Exit' If You want to quit program)\n :")
        if string in ('Exit' , 'exit'):
            quit()
        try :
            integer=int(string)
            break
        except :
            print("Enter Numbers not letters")
            continue
    if integer is 1:
        string = string+" This is One"
        print(string)
        integer=integer+2+3+4+5
        print("Next 5 numbers's addition is : ",integer)

    if integer is 2:
        string = string+" This is Two"
        print(string)
        integer=integer+(integer+1)+(integer+2)+(integer+3)+(integer+4)
        print("Next 5 numbers's addition is : ",integer)

    if integer is 3:
        string = string+" This is Three"
        print(string)
        integer=integer+(integer+1)+(integer+2)+(integer+3)+(integer+4)
        print("Next 5 numbers's addition is : ",integer)

    if integer is 4:
        string = string+" This is Four"
        print(string)
        integer=integer+(integer+1)+(integer+2)+(integer+3)+(integer+4)
        print("Next 5 numbers's addition is : ",integer)


    if integer is 5:
        string = string+" This is Five"
        print(string)
        integer=integer+(integer+1)+(integer+2)+(integer+3)+(integer+4)
        print("Next 5 numbers's addition is : ",integer)


    if integer is 6:
        string = string+" This is Six"
        print(string)
        integer=integer+(integer+1)+(integer+2)+(integer+3)+(integer+4)
        print("Next 5 numbers's addition is : ",integer)


    if integer is 7:
        string = string+" This is Seven"
        print(string)
        integer=integer+(integer+1)+(integer+2)+(integer+3)+(integer+4)
        print("Next 5 numbers's addition is : ",integer)


    if integer is 8:
        string = string+" This is Eight"
        print(string)
        integer=integer+(integer+1)+(integer+2)+(integer+3)+(integer+4)
        print("Next 5 numbers's addition is : ",integer)


    if integer is 9:
        string = string+" This is Nine"
        print(string)
        integer=integer+(integer+1)+(integer+2)+(integer+3)+(integer+4)
        print("Next 5 numbers's addition is : ",integer)


    if integer is 10:
        string = string+" This is Ten"
        print(string)
        integer=integer+(integer+1)+(integer+2)+(integer+3)+(integer+4)
        print("Next 5 numbers's addition is : ",integer)

    while True:
        again=input("Do You Want To Do Again ??? \n (ACCEPTED WORDS ARE 'Yes' and 'No' )")
        if again not in ('Yes' , 'yes' , 'No' , 'no','YES','NO'):
            print("Enter Valid Option only")
            continue
        if again in ('Yes' , 'yes','YES'):
            break
        elif again in ('No' , 'no','NO'):
            quit()