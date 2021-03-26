#7
#Create a program to count by prime numbers. Ask the user to input a number, then print each prime number up to that number.(while) (Mandatory)
while True:
    number=input("Enter a number to get prime numbers: ")
    try: 
        number=int(number)
        if number<=1:
            print("ENter NUMBER WHICH IS GREATER THAN ONE")
            continue
        else:break
    except : 
        print("Enter a NUMBER not STRING and It should be Greater than one")
        continue
# flag = False
primes=[]
index=2

while index <= number:
    
    temp =0
    for index2 in range(2,index):
        if (index%index2)==0:
            break
        else:
            primes.append(index)
            # temp = index
    # if temp != 0 :
    #     primes.append(temp)
    index+=1
print(primes)