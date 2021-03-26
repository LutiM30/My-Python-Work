# Accepting rows
while True:
    rows=input("Enter Numbers of Rows :")
    try:
        rows=int(rows)
        break
    except:
        print("You Have Not Entered Number")
        continue

#Pyramid

rows2 = rows - 1
rows3 = rows - 1

for count in range(rows):
     
    for count2 in range(rows2):
        print(end=" ")
    rows2 = rows2 - 1

    for count2 in range(count+1):
        print("* ", end="")
    print("\n")


 
for count in range(rows):

    for count2 in range(count+1):
         print(end=" ")

    for count2 in range(rows3):
       print("* ", end="")
    rows3 = rows3 - 1

    
    print("\n")