#7)program

#Definition :Create a dictionary with the ticker symbol and company name like 

#   {'GM':'General Motors','CAT':'Caterpillar','EK':'Eastman Kodak'}. Create a simple list of blocks of stock. These could be tuples with ticker symbols, prices, dates and number of shares. For example:

ticker={}
my_purchases={}

while True:
    short = str(input('\nEnter Which Record You want to Create: \n Enter Exit To Exit from it\nEnter Here: '))
    if short == 'exit':
        break
    while True:
        Company_Name = input("Enter Company_Name in '{}':  ".format(short))
        try:
            Company_Name = int(Company_Name)
            print('Enter Words Not Numbers!')
            continue
        except:
            break
    ticker[short]=Company_Name

print('There are {} Companies\nNames are: {}'.format(len(ticker),ticker))

#purchases = [ ( 'GE', 100, '10-sep-2001', 48 ), ( 'CAT', 100, '1-apr-1999', 24 ), ( 'EK', 200, '1-jul-1998', 56 ) ].
#Create a purchase history report that computes the full purchase price (shares times dollars) for each block of stock 	and uses the stockDict to look up the full company name.

Companies=list()
for key,value in ticker.items():
    Companies.append(key)

share_info=list()
purchase_history=list()
expense=[]
for company in Companies:
    si_t=list()
    ph_t=list()
    while True:
        price=input("Enter {}'s share price: ".format(company))
        try:
            price=int(price)
            break
        except:
            print('INVALID INVALID INPUT')
    date=input("Enter {}'s share purchase Date: ".format(company))
    while True:
        qty=input("Enter {}'s share Quantity: ".format(company))
        try:
            qty=int(qty)
            break
        except:
            print('INVALID INVALID INPUT')


    purchase_price=qty*price

    si_t.append(company)
    si_t.append(price)
    si_t.append(date)
    si_t.append(qty)
    si_t=tuple(si_t)
    share_info.append(si_t)
    
    ph_t.append(ticker.get(company))
    ph_t.append(purchase_price)
    ph_t.append(date)
    ph_t=tuple(ph_t)
    purchase_history.append(ph_t)
    expense.append(purchase_price)

exp=sum(expense)

print("This is The Share Information That You Owned \n{}\nTHIS IS THE PURCHASE HISTORY \n{}\n THIS IS SUM OF ALL THE PURCHASE '${}'".format(share_info, purchase_history,exp))