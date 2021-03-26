# 19)ChangeString
#Write a program that changes the string "Hello World!" to "Jello World!" (Mandatory)
while True:
    string = input("Enter String -> ")
    try:
        string =int(string)
        print("Only Letters are supported TRY AGAIN!")
        continue

    except :
        break

print("\n Your String is",string)

chng={'A':'B','B':'C','C':'D','D':'E','E':'F','F':'G','G':'H','H':'I','I':'J','J':'K','K':'L','L':'M','M':'N','N':'O','O':'P','P':'Q','Q':'R','R':'S','S':'T','T':'U','U':'V','V':'W','W':'X','X':'Y','Y':'Z','Z':'A'}
chng2={'a':'b','b':'c','c':'d','d':'e','e':'f','f':'g','g':'h','h':'i','i':'j','j':'k','k':'l','l':'m','m':'n','n':'o','o':'p','p':'q','q':'r','r':'s','s':'t','t':'u','u':'v','v':'w','w':'x','x':'y','y':'z','z':'a'}

split= [char for char in string]

ans=[]

for index in split:
    if index.islower() is True: 
        ans.append(chng2[index])
    
    elif index.isupper() is True:
        ans.append(chng[index])

    if index == ' ':
        ans.append(' ')

spaces=None

for index in ans:
    if spaces is None:
        spaces=index
    else:
        spaces=spaces+index

print("\n Your output is",spaces)