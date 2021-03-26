# 18)AbecedarianSeries
#Write a program that generates the abecedarian series. Prefixes = "JKLM" Suffix = "ack" Output : Jack Kack Lack Mack (Mandatory)
while True:
    prefix = input("Enter First String -> \n (Max Length 6 Length is ALLOWED) : ")
    if  len(prefix) > 6:
        print("\n \nLength Exceeded , Try Again!")
        continue
    else:
        break

while True:
    suffix = input("Enter a Word : ")
    if  len(suffix) > 6:
        print("\n \nLength Exceeded , Try Again!")
        continue
    else:
        break

split = [char for char in prefix]

for index in split:
    index=index+suffix
    print(index)
