#9#Write a program that Waits until a password has been entered. Use control-C to break out without the password.(while)
password = False
while not password:
    word=input('Enter The Password: ')
    if not word:
        print('It should not be empty')
        continue
    else:
        password = True
    if KeyboardInterrupt:
        quit()