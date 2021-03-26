#18# Write a program that finds out prime numbers in the range 2 to 10. But display the multiples if the number is not prime. Example : 9 equals 3 * 3 (Mandatory)
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
mix=[]
nonprimes=[]
mix=[]
num=2
while num <= number:
    prime = True    
    for index in range(2,num):
        if (num % index) == 0:
            prime = False
            if prime is False:
                mix.append('{} = {} * {}'.format(num,index, int(num/index)))
            break
        
    if prime :
        mix.append(num)
    num+=1
print(mix)