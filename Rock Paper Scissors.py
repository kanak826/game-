#workflow of project:
# input from user(rock,paper,scissor)
# computer choice (computer will choose randomly not cinditionally)
# result print
# 
# case1
# A-Rock...
# Rock=Rock->tie
# Rock=scissor->rock win
# Rock=paper->paper win


#B-Scissor....
# Scissor=Scissor->tie
# scissor=rock->rock win
# scissor=paper->scissor win

#C-Paper...
# paper=paper->tie
# paper=scissor->scissor win
# paper=rock->paper win

import random
item_list=["Rock","Paper","Scissor"]
user_choice=input("enter your move=Rock,Paper,Scissor")
comp_choice=random.choice(item_list)
print(f"user choice={user_choice},Computer choice={comp_choice}")

if user_choice==comp_choice:
    print("match is Tie")
elif user_choice=="Rock":
    if comp_choice=="Paper":
       print("paper covers rock =computer is win")
    else:
        print("Rock smashes scissor=user win") 
elif user_choice=="Paper":
    if comp_choice=="Scissor":
        print("paper is cut=user win")
    else:
        print("Paper cover Rocks")                   
elif user_choice== "Scissor":
    if comp_choice=="Paper":
        print("Paper is cut= user win")  
    else:
        print("Scissor cut=computer win")   
print("Great Game..")                