import random #importing random module

while True: #iterate loop
    user_action = input("Enter a choice (rock,paper,scissors): ") #take input
    possible_actions = ["rock","paper","scissors"]
    #using random fuction
    computer_action = random.choice(possible_actions)
    print(f"\n you chose {user_action}, computer chose {computer_action}. \n") #display both output what is selected by you and computer
#conditions to check who won the game
    if user_action == computer_action:
        print(f"both player selected {user_action}. it is a tie!")
    elif user_action == "rock":
        if computer_action == "scissor":
            print("you win")
        else:
            print("you lose")
    elif user_action == "paper":
        if computer_action == "rock":
            print("you win")
        else:
            print("you lose")
    elif user_action == "scissor":
        if computer_action == "paper":
            print("you win")
        else:
            print("you lose")
        #take input for playing again
        play_again = input("play again? (y/n):")
        if play_again != "y":
            break
