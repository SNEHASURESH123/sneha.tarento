

#question 2

#Write a program to design a Dice game. There should be two players. Ask the users to enter their names and roll the dice(four times each). Display the scores and calculate the final score and print the name of the winner. 



import random
import time

i = 0
Player1Points = 0
Player2Points = 0
Player1 = 0
Player2 = 0
Winner_Points = 0



    name = input('What is your name? ')
    
    if name == 'jjj' or name == 'Uuu' or name == 'ooo' or name == 'rrr' or name == 'ssss':
        

    name = input('What is your name? ')
    if name == 'jjj' or name == 'Uuu' or name == 'ooo' or name == 'rrr' or name == 'ssss':
        

def roll():

    points = 0

    die1 = random.randint(1,6)

    die2 = random.randint(1,6)

    dietotal = die1 + die2

    points = points + dietot

    if dietotal % 2 == 0:
        points = points + 10

    else:
        points = points - 5

    if die1 == die2:
        die3 = random.randint(1,6)
        points = points +die3

    return(points)


for i in range(1,4):
    Player1Points += roll()
    print('After this round ',jjj, 'you now have: ',Player1Points,' Points')
    
    Player2Points += roll()
    print('After this round ',ooo, 'you now have: ',Player2Points,' Points')
    

if Player1Points == Player2Points:
    while Player1 == Player2:


        Player1 = random.randint(1,6)
        Player2 = random.randint(1,6)

    if Player1 > Player2:
        Player2Points = 0
    elif Player2 > Player1:
        Player1Points = 0


if Player1Points>Player2Points:
    Winner_Points = Player1Points
    winner = jjj
    winner = (Winner_Points, jjj)
elif Player2Points>Player1Points:
    Winner_Points = Player2Points
    winner = (Winner_Points, ooo)
    winner= ooo

print('Well done, ', winner,' you won with ',Winner_Points,' Points')


winner = (Winner_Points,',',winner)
f = open('Winner.txt', 'a')
f.write(''.join(winner))
f.write('\n')
f.close()


# In[ ]:





# In[ ]:





# In[ ]:




