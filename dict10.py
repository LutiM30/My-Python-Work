#10)Update
#Write a program that shows the use of 'update' method which updates any existing item in the dictionary. (Mandatory)

# Syntax: dict.update([other])

# Parameters: This method takes either a dictionary or an iterable object of key/value pairs (generally tuples) as parameters.

# Returns: It doesn’t return any value but updates the Dictionary with elements from a dictionary object or an iterable object of key/value pairs.

dict1={}
dict2={}

while True:
    K1=input('Enter Key that you want to add in Dictionary1: ')
    if K1 in ['exit','Exit','EXIT']:
        break
    else:
        V1=input('ENTER VALUE OF {}: '.format(K1))
        dict1[K1]=V1

while True:
    K2=input('\nEnter Key that you want to add in Dictionary2: ')
    if K2 in ['exit','Exit','EXIT']:
        break
    else:
        V2=input('ENTER VALUE OF {} '.format(K2))
        dict2[K2]=V2

print('BEFORE UPDATE METHOD\nDict1={}\nDict2{}'.format(dict1,dict2))
dict1.update(dict2)
print('After UPDATE METHOD\nDict1={}\nDict2{}'.format(dict1,dict2))