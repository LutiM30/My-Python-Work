#4# Write a program that performs the following operations (Mandatory)
#Work Instructions
#	Take one variable and initialize it with 10
#	Input one number from user..
#	Now ,if user input is same as initialized number then print "success"
#	If user input is lessar then initialized number then print "smaller"
#	If user input is greater then initialized number then print "bigger"
num=10
while True:
    uservalue=input('Enter A Number')
    try: 
        uservalue=int(uservalue) 
        break
    except:
        print("INVALID INPUT")
        continue

if num > uservalue: print("Less than ",num)

if num < uservalue: print("Bigger than ",num)

if num == uservalue: print("U got it")
