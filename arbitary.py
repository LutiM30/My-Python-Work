# Instruct the user to pick an arbitrary number from 1 to 100 and proceed to guess it correctly with in seven tries.
import random
input("You have to Pick a number which is between 1 to 100 , When you pick a number press Enter I'll Guess it.")
low = 1 
high = 100
done = False
for chances in range(7) :
    guess = random.randint(low, high)
    print(" My Guess is", guess)
    while True :
        resp= input("Enter H if Number is Higher \n Enter L if Number is Lower \n Enter E if Number is Equal \n \n Enter Here :")[0].upper()
        if resp == 'E':
            print("Number is ", guess , end=(' '))
            if chances == 1:
                print("In 1 Guess")
            else:
                print("In ", chances+1, end=(' '))
                print("Guesses")
                done = True
                break
        if resp == 'H':
            build=input('is your number between {} and {} \n Y for YES \n N for NO'.format(guess+1,guess+6))[0].upper()
            if build =='Y':
                
                high = guess +6
                low = guess+1
            elif build == 'N':    
                low=guess+6
            break

        if resp == 'L':
            build=input('is your number between {} and {} \n Y for YES \n N for NO'.format(guess-1,guess-6))[0].upper()
            if build =='Y':
    
                high = guess-1
                low = guess-6
            elif build == 'N':    
                high=guess-6
            break
        else:
            print('Not A Valid Response')
    if done:
        break
        

print("End")