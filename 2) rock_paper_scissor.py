

# Task 2: Rock paper scissor

# Winning Rules as follows:

# Rock vs paper-> paper wins
# Rock vs scissor-> Rock wins
# paper vs scissor-> scissor wins.

import random
while True:
    a=int(input("What do you choose?\nType 0 for rock, 1 for paper , 2 for scissors "))
    if(a==0):
        print("you entered rock")
    elif(a==1):
        print("you entered paper")
    elif(a==2):
        print("you entered scissors")
    else:
        print("invalid choice")
        continue
 
    comp_ans=random.randint(0,2)
    if(comp_ans==0):
        print("comp entered rock")
    elif(comp_ans==1):
        print("comp entered paper")
    else:
        print("comp entered scissors")

    if(a==comp_ans):
        print("draw")
        #  no break here
    elif(a==0 and comp_ans==2)or(a==1 and comp_ans==0)or(a==2 and comp_ans==1):
        print("You win!")
        break
    else:
        print("computer wins")
        break
