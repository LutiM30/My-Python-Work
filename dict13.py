#12Spanishword
#Write a function 'createDictionary' that creates 'spanish' dicitonary by assigning spanish equivalent of 1 to 10 like spnaish['one']='uno'. Now print values on the screen. (Mandatory)

def createDictionary(dict1):
    while True:
        spanish=input('Enter Spanish Number that you want to add in Dictionary: ')
        if spanish in ['exit','Exit','EXIT']:
            break
        else:
            english=input('ENTER english OF {}: '.format(spanish))
            dict1[spanish]=english


dicti={}
createDictionary(dicti)
print(dicti)