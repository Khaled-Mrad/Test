from random import randint
play=True
while play:
    choice=["rock","paper","scissors"]
    computer_choice=choice[randint(0,2)]
    ch=""
    for i in choice:
        ch=ch+"   "+i
    ch="chose one from : "+ch+" :  "
    per_choice=input(ch)
    if (choice.index(computer_choice) < choice.index(per_choice)):
        print("YOU WON !!!!")
    elif (choice.index(per_choice) < choice.index(computer_choice)):
        print("YOU LOST !!!!")
    else:
        print("IT IS A DRAW !!!!")
    play_choice=input("Do you want to play again(yes/no) : ")
    if(play_choice=="yes"):play=True
    else:
        play=False
        print("Thank you for playing the game")

