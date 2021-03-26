#4)list
#Create two dictionaries callled prices (contains product & price) and my_purchases (product , number of purchase of this product). (Mandatory)
#Now print a grocery_bill with for loop that depicts your total exepense.

prices={}
my_purchases={}

Total=0

while True:
    products = str(input('\nEnter Which Record You want to Create: \n Enter Exit To Exit from it\nEnter Here: '))
    if products == 'exit':
        break
    while True:
        price = (input("Enter price in '{}':  ".format(products)))
        try:
            price = int(price)
            break
        except:
            print("Money Have Numbers Not Words")
            continue
    prices[products]=price
    Total+=1

print('Total Products are: {}\nPrices of Each Product is {}'.format(Total,prices))

Total2=0
while True:
    purchase=input('which product you want to purchase from these : \n{}\nEnter Here: '.format(prices))
    if purchase == 'exit':
        break
    elif purchase not in prices:
        print("There's no such product named {} \n !!!TRY AGAIN!!!".format(purchase))
        continue
    my_purchases[purchase] =my_purchases.get(purchase,prices.get(purchase)) + prices.get(purchase)
    Total2+=1

# print(my_purchases)
print('\n\nTotal Products You Purchased : {}\nPrices of Each Product is {} \n Your Bill is {} \n Amount To be paid: {}'.format(Total2,prices,my_purchases,sum(my_purchases.values())))