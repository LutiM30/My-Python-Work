#11# Write a program that prints 1 2 3 4 5 using for loop. (Mandatory)
while True:
    try:
        enter =int(input("Enter the number : "))
        break

    except:
        print('Invalid Input')
        continue
op=[]
for i in range(1,enter+1):
    op.append(i)
print(op)