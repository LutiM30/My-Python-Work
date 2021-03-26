#16)Vote
#Write a program that tallies the votes of a four-candidate election.Votes arrive one at a time, where a vote for Candidate i is denoted by the number, i.At last print the winner on the screen. (Mandatory)

Candidate_A = []
Candidate_B = []
Candidate_C = []
Candidate_D = []
Index = 1
while True:
    
    votes = input('''<<<Candidates>>>
    1> Candidate A
    2> Candidate B
    3> Candidate C
    4> Candidate D
    5> !DONE!
    Press CHOICE Of NUMBER: ''')
    
    try:

        votes=int(votes)

    except:
        print('Invalid Input')

    if votes == 1:
        
        Candidate_A.append('1')
        Index+=1

    elif votes == 2:

        Candidate_B.append('1')
        Index+=1

    elif votes == 3:

        Candidate_C.append('1')
        Index+=1
    
    elif votes == 4:

        Candidate_D.append('1')
        Index+=1

    elif votes == 5:
        surity=input('ARE YOU SURE ALL VOTING IS DONE???\nPress Y for Yes \nPress N for No \nYour Choice: ')[0].upper()
        if surity == 'Y':
            break
        elif surity == 'N':
            continue
        else :
            print('Invalid Input \nTry Again\n GOING to MAIN MENU')

a=len(Candidate_A)
b=len(Candidate_B)
c=len(Candidate_C)
d=len(Candidate_D)

if a > b and c and d :

    print('There Are {} Voters\nAnd Winner Is Candidate A'.format(Index))

elif b > c and d and a :

    print('There Are {} Voters\nAnd Winner Is Candidate B'.format(Index))

elif c > d and a and b :

    print('There Are {} Voters\nAnd Winner Is Candidate C'.format(Index))

elif d > a and b and c :

    print('There Are {} Voters\nAnd Winner Is Candidate D'.format(Index))