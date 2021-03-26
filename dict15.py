# 14student

# Write a menu driven program that contains the menu
#  1. Add Student 
#  2. Remove Student
#  3.Print Grades
#  4.Record Student Grade
#  5.Print Menu
#  6.Exit.
  
# There is a Maximum Point Limit for Assignmments say : max_points = [25,25,50,25,100] and
# 						     assignments = ['HW 1' , 'HW 2','Quiz','HW 3','test'].

# Now define one dictionary students = {'#Max' : max_points} and one by one show the use of all menu items.

Students=list()
HW_1={}
HW_2={}
HW_3={}
Quiz={}
Test={}
Max_HW={}
i=0

while True:
    options = input('''\n<<<THIS ARE AVAILABLE OPERATIONS>>>
    1> Add Student
    2> Record Student Grade
    3> Print Grades
    4> Remove Student
    5> Maximum in Homework
    6> Quit
    Enter Your OPTIONS:  ''')

    try:
        options =int(options)
        
        if options>5: 
            print('Invalid Input')
            continue

    except:
        print('Invalid Input')
        continue

    if options==1:
        
        while True:
            student=input('\nEnter Student Name\nif You Done with Adding Student Name enter -> Done\nEnter Here:')
            
            if student in ['done','Done','DONE']:
                break
            
            elif student in Students:
                print('\n##Name is Already Here##')
                continue

            else:
                Students.append(student)
                i+=1
                continue

        print('\nThere Are Total {} Students Name Of them are {}'.format(i,Students))

    elif options==2:
        
        while True:
            student=input("\nEnter Which Student's Grades You want to Enter\nif You Done with Adding Grades enter -> Done\nEnter Here:  ")
            
            if student in Students:
                
                while True:            
                    hw1=input('Enter HW 1 Marks\nIt Should Not be MORE THAN 25: ')
                    try:
                        hw1=int(hw1)
                        if hw1>25:
                            print("NOT VALID")
                            continue
                    
                    except:
                        print('Invalid Input')
                        continue
                    HW_1[student]=hw1
                    break
                
                while True:            
                    hw2=input('Enter HW 2 Marks\nIt Should Not be MORE THAN 25: ')
                    try:
                        hw2=int(hw2)
                        if hw2>25:
                            print("NOT VALID")
                            continue
                    
                    except:
                        print('Invalid Input')
                        continue
                
                    HW_2[student]=hw2
                    break
                
                while True:            
                    hw3=input('Enter HW 3 Marks\nIt Should Not be MORE THAN 25: ')
                    
                    try:
                        hw3=int(hw3)
                        if hw3>25:
                            print("NOT VALID")
                            continue
                    
                    except:
                        print('Invalid Input')
                        continue
                
                    HW_3[student]=hw3
                    break
                
                while True:            
                    quiz=input('Enter Quiz Marks\nIt Should Not be MORE THAN 50: ')
                    
                    try:
                        quiz=int(quiz)
                        if quiz>50:
                            print("NOT VALID")
                            continue
                    
                    except:
                        print('Invalid Input')
                        continue
                
                    Quiz[student]=quiz
                    break
                
                while True:            
                    test=input('Enter Test Marks\nIt Should Not be MORE THAN 100: ')
                    
                    try:
                        test=int(test)
                        if test>100:
                            print("NOT VALID")
                            continue
                    
                    except:
                        print('Invalid Input')
                        continue
                
                    Test[student]=test
                    break

                if hw1 > hw2 and hw3:
                    Max_HW[student]=hw1
                if hw2 > hw3 and hw1:
                    Max_HW[student]=hw2
                if hw3 > hw1 and hw2:
                    Max_HW[student]=hw3
            
            if student in ['done','Done','DONE']:
                break
            
            else:
                print('No Student Found Named ',student)
                continue


    elif options== 3: 

        findgrades=input("\nEnter Which Student's Grades You want to find:  ")

        if findgrades in HW_1 and HW_2 and HW_3 and Quiz and Test:
            if len(findgrades) == 5:
                print("""
            ___________________
            |{}'s Grades   |
            |HW 1 Grades is {}|
            |HW 2 Grades is {}|
            |HW 3 Grades is {}|
            |Quiz Grades is {}|
            |Test Grades is {}|
            |_________________|
            """.format(findgrades,HW_1.get(findgrades),HW_2.get(findgrades),HW_3.get(findgrades),Quiz.get(findgrades),Test.get(findgrades)))
            elif len(findgrades) == 4:
                print("""
            ___________________
            |{}'s Grades    |
            |HW 1 Grades is {}|
            |HW 2 Grades is {}|
            |HW 3 Grades is {}|
            |Quiz Grades is {}|
            |Test Grades is {}|
            |_________________|
            """.format(findgrades,HW_1.get(findgrades),HW_2.get(findgrades),HW_3.get(findgrades),Quiz.get(findgrades),Test.get(findgrades)))
            elif len(findgrades) == 3:
                print("""
            ___________________
            |{}'s Grades     |
            |HW 1 Grades is {}|
            |HW 2 Grades is {}|
            |HW 3 Grades is {}|
            |Quiz Grades is {}|
            |Test Grades is {}|
            |_________________|
            """.format(findgrades,HW_1.get(findgrades),HW_2.get(findgrades),HW_3.get(findgrades),Quiz.get(findgrades),Test.get(findgrades)))

        else :
            print("{}'s Grades Is not ENTERED YET" .format(findgrades))

    elif options==4:

        delrec=input('\nEnter Which Record You want to Delete: ')

        if delrec in HW_1 and HW_2 and HW_3 and Quiz and Test:
            
            del HW_1[delrec]
            del HW_2[delrec]
            del HW_3[delrec]
            del Quiz[delrec]
            del Test[delrec]
            del Max_HW[delrec]
            Students.remove(delrec)
            print('Sucessfully Deleted')
    
        else: 
            print('No record Found named ' + delrec)
            continue
    
    elif options==5:
        print(Max_HW)
    
    elif options==6: quit()

    while True:
        clarify=input('You want to Do it Again??? \n Y for Yes \n N for No \n Enter Your Choice: ')[0].upper()
        if clarify == 'Y':
            break
        elif clarify == 'N':
            quit()
        else: continue