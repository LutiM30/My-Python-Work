#15NestedDict
#Write one program that has nested dictionaries and accessing those values from nested directories.
dict1={}
keys=[]
while True:
    K1=input("\nEnter Key in Dictionary 1\nEnter Exit to stop adding\nEnter Here:  ")
    if K1 in ['Exit','exit','EXIT']:
        break
    else:
        keys.append(K1)
        V1=input("Enter Value Of {} :  ".format(K1))
        dict1[K1]=V1

dict2={}

while True:
    K2=input("\n\nEnter Key in Dictionary 2\nEnter Exit to stop adding\nEnter Here:  ")
    if K2 in ['Exit','exit','EXIT']:
        break
    else:
        V2=input("Enter Value Of {} :  ".format(K2))
        dict2[K2]=V2

while True:
    chng=input("Enter in which key of Dictionary 1 you want to add Dictionary 2:  ")
    if chng in keys:
        dict1[chng] = dict2
        break
    else:
        print("There's No key named {} in {}".format(chng,keys))

print(dict1)