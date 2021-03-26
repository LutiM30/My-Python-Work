#CONTROLFLOW
#1 Write a program that takes two variable and initialize them with 100 and 0 respectively.Now check if variable has some value then print "Got a true expression value" and at the end print "Good Bye (Mandatory)
correct=[100,0]
while True:
    guess=input("Enter A Number: \n (Press Exit If You Want to exit or You Got All The Number): ")
    try:
        guess=int(guess)
            
    except:
        if guess in ['Exit', 'exit']:
            quit()
        else:
            print("'Enter Number Not Letters!'")
            continue
        
    while True:
        for i in correct:
        
            if guess == i :
                print("\n")
                print("'Got The Number'")
                correct.remove(i)
                break
            
            else:
                print("\n") 
                continue
        print("'Try Again!'")        
        break