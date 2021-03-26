# 3)Write a program that performs add , subtract , multilply and devide operations on numbers. (Mandatory)

while True:
    while True:
        Num1 = input("Enter Your Number: ")
        Num1.rstrip()
        if Num1 in ('Exit' , 'exit'):
            quit()
        try:
            Num1 = int(Num1)
            
        except:
            print("ENTER NUMBER NOT LETTERS")
            continue
        break

    while True:
        Num2 = input("Enter Your 2nd Number: ")
        Num2.rstrip()
        if Num2in ('Exit' , 'exit'):
            quit()
        try:
            Num2=int(Num2)
            
        except:
            print("ENTER NUMBER NOT LETTERS")
            continue
        break

    while True:
        operation= input("Type Number for Choosing Operation \n 1 -> Addition \n 2 -> Substraction \n 3 -> Multiplication \n 4 -> Division \n if You Type Exit the program will be Close :")
        if operation in ('Exit' , 'exit'):
            quit()
        try:
            operation=int(operation)
        except:
            print("ENTER NUMBER NOT LETTERS")
            continue
        if operation > 4 :
            print("ENTER VALID NUMBER")
            continue
        break

    if operation == 1:
        operation=Num1+Num2
        print('Addition Of ',end="")
        print(Num1,end=" ")
        print("And",end=" ")
        print(Num2,end=" ")
        print("is : ",operation)

    elif operation == 2:
        operation=Num1-Num2
        print('Substraction Of ',end="")
        print(Num1,end=" ")
        print("And",end=" ")
        print(Num2,end=" ")
        print("is : ",operation)

    elif operation == 3:
        operation=Num1*Num2
        print('Multiplication Of ',end="")
        print(Num1,end=" ")
        print("And",end=" ")
        print(Num2,end=" ")
        print("is : ",operation)

    elif operation == 4:
        operation=Num1/Num2
        print('Division Of ',end="")
        print(Num1,end=" ")
        print("And",end=" ")
        print(Num2,end=" ")
        print("is : ",operation)

    again=input("Do You Want To Do Again ??? \n (ACCEPTED WORDS ARE 'Yes' and 'No' )")
    if again in ('Yes' , 'yes'):
        continue
    elif again in ('No' , 'no'):
        break
