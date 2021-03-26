# 9)Write a program that print the calender for the month of January , 2012. 
import calendar
while True:
    while True:
        year = input("Enter Year: ")
        year.rstrip()
        if year in ('Exit' , 'exit'):
            quit()
        try:
            year = int(year)
            
        except:
            print("ENTER NUMBER NOT LETTERS")
            continue
        break

    while True:
        month = input("Enter Month in NUMBERS : ")
        month.rstrip()
        if month in ('Exit' , 'exit'):
            quit()
        try:
            month=int(month)
            
        except:
            print("ENTER NUMBER NOT LETTERS")
            continue

        if month > 12:
            print("There Are ONLY '12' Months which I KNOW")
            continue
        break

    if month == 1:
        print('Calender of ',end="")
        print(year,end="")
        print("'s January is")
        print(calendar.month(year, month))
        

    elif month == 2:
        
        print('Calender of ',end="")
        print(year,end="")
        print("'s Febuary is")
        print(calendar.month(year, month))

    elif month == 3:
        
        print('Calender of ',end="")
        print(year,end="")
        print("'s March is")
        print(calendar.month(year, month))
    
    elif month == 4:
        
        print('Calender of ',end="")
        print(year,end="")
        print("'s April is")
        print(calendar.month(year, month))
    
    elif month == 5:
        
        print('Calender of ',end="")
        print(year,end="")
        print("'s May is")
        print(calendar.month(year, month))

    elif month == 6:
        
        print('Calender of ',end="")
        print(year,end="")
        print("'s June is")
        print(calendar.month(year, month))

    elif month == 7:
        
        print('Calender of ',end="")
        print(year,end="")
        print("'s July is")
        print(calendar.month(year, month))

    elif month == 8:
        
        print('Calender of ',end="")
        print(year,end="")
        print("'s August is")
        print(calendar.month(year, month))

    elif month == 9:
        
        print('Calender of ',end="")
        print(year,end="")
        print("'s September is")
        print(calendar.month(year, month))

    elif month == 10:
        
        print('Calender of ',end="")
        print(year,end="")
        print("'s October is")
        print(calendar.month(year, month))
    
    elif month == 11:
        
        print('Calender of ',end="")
        print(year,end="")
        print("'s November is")
        print(calendar.month(year, month))
    
    elif month == 12:
        
        print('Calender of ',end="")
        print(year,end="")
        print("'s December is")
        print(calendar.month(year, month))
        
    again=input("Do You Want To Do Again ??? \n (ACCEPTED WORDS ARE 'Yes' and 'No' )")
    if again in ('Yes' , 'yes'):
        continue
    elif again in ('No' , 'no'):
        quit()
