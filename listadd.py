#17#Write a loop that takes a list of integers and computes the sum of all the integers up until a zero is found in the list. Use the break statement. (Mandatory)
list =[]
while True:
    
    num =input("Enter The Number :")

    try:
        num = int(num)
        list.append(num)
        if num == 0:
            break

    except:
        print("INVALID INPUT")
        continue

print(sum(list))