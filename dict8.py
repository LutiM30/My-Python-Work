#8)month
#A date of the form 8-MAR-85 includes the name of the month, which must be translated to a number. (Mandatory)
Months = {'JAN' :'1','FEB' :'2','MAR' :'3','APR' :'4','MAY' : '5','JUN' : '6','JUL' : '7','AUG' : '8','SEP' : '9','OCT' :'10','NOV' :'11','DEC' :'12'}
keys = Months.keys()
# length = None
while True:
    inp=input('Enter Date \nFORMAT: DD/MMM/YYYY \nENTER HERE:  ')
    length=len(inp)
    if length != 11:
        print('MATCH THE FORMAT!')
        continue
    else:
        print('Your INPUT WAS',inp)

        string = [char for char in inp]
        i=3
        M=None
        
        while i < 6:
            if M is None:
                M=string[i]
                i+=1
            M+=string[i]
            i+=1

        M=M.upper()
    
        
        if M in keys:
                month=Months.get(M)
        else:
            print('Invalid Input')
            continue

        day=None
        i=0
        while i < 3:
            if day is None:
                day=string[i]
                i+=1
            day+=string[i]
            i+=1

        year=None
        i=6
        while i < 11:
            if year is None:
                year=string[i]
                i+=1
            year+=string[i]
            i+=1
        break


print('Your Output is ',day+month+year) 