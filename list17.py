#17)ReadSeries
#Write a program that reads a series of integers in the range 1 to 20. The input is terminated by an integer that does not fall in this range.Print most often and least often inputs. (Mandatory)

while True:
    ranj = input('Enter The Number For Creating Range')
    
    try:
        ranj = int(ranj)
        if ranj <= 1:
            print('It Should Be More Then One')
            continue
        else: break

    except:
        print("Try again , '{}' It is Not A NUMBER *".format(ranj))
        continue

num = None
occurance = {}

while True:

    while True:
        num = input('Enter A Number')

        try:
            num = int(num)        
            break
            
        except:
            print("Try again , '{}' It is Not A NUMBER *".format(num))
            continue

    if num in range(1,ranj+1):
        occurance[num]=occurance.get(num,0)+1

    elif num not in range(1,ranj+1):
        maxNum = max(occurance,key=occurance.get)
        minNum = min(occurance,key=occurance.get) 
        
        print("Exiting Program Because '{}' is not in Range Of '1' to '{}' \n'{}' Is Most Occured Number\n'{}' Is Least Occured Number".format(num,ranj,maxNum,minNum))
        
        break