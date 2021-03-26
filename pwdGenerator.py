## Import RANDOM to generate Unpredictable VALUES
import random

print('WELCOME TO YOUR PASSWORD GENERATOR')

## RANDOM VALUES FROM CHARS
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_-=+,.?0123456789'

##GETTING PASSWORD QUANTITY
while True:
    qty = input('ENTER HOW MANY PASSWORDS YOU WANT: ')
    try:
        qty=int(qty)
        break
    except:
        print('INVALID INPUT')
        continue

## LENGTH OF PASSWORDS
while True:
    length = input('ENTER LENGTH OF YOUR PASSWORDS: ')
    try:
        length=int(length)
        break
    except:
        print('INVALID INPUT')
        continue


print('\n<<<HERE ARE YOUR PASSWORDS>>>')

##GENERATING PASSWORDS
for pwd in range(qty):
    password = ''
    
    for C in range(length):
        password += random.choice(chars)
    print('       ',password)