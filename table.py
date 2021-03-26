#15# Write a program that prints a table for a given input integer using a for loop. (Mandatory)
while True:
    try:
        number =int(input('ENTER A NUMBER '))
        break
    except:
        print('INVALID INPUT')
        continue

for i in range(1,10+1):
    table = number*i
    print('{}*{}={}'.format(number,i,table))