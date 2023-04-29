import random

rps_list = ["rock","paper","scissors"]

pc_points = 0
user_points = 0
check = True

while check:

    if pc_points == 3:
        print(f"You lost with the score of PC: {pc_points} - You: {user_points}")
        check = False
        break

    elif user_points == 3:
        print(f"You won with the score of PC: {pc_points} - You: {user_points}!")
        check = False
        break
    
    pc_choice =  random.choice(rps_list)
    user_choice = (input("Choose rock, paper or scissors: ")).lower()

    if user_choice not in rps_list:
        print("PLease choose only one of these three options: rock, paper or scissors!")
        continue
    else:
        print("ROCK, PAPER, SCISSORS, SHOOOTT")

    # Comparing both inputs
    if (pc_choice == 'rock' and user_choice == "scissors") or (pc_choice == 'paper' and user_choice == "rock") or (pc_choice == 'scissors' and user_choice == "paper"):
        pc_points += 1
        print(f"Pc chose {pc_choice} and you chose {user_choice}, so pc wins a point.")
        print(f"The score is {user_points} - {pc_points}")
        continue
    
    elif (user_choice == "rock" and pc_choice == 'scissors') or (user_choice == "paper" and pc_choice == 'rock') or (user_choice == "scissors" and pc_choice == 'paper'):
        user_points += 1
        print(f"Pc chose {pc_choice} and you chose {user_choice}, so You win a point.")
        print(f"The score is {user_points} - {pc_points}")
        continue
    else:
        print(f"Pc chose {pc_choice} and you chose {user_choice}, we go again.")
        print(f"The score is {user_points} - {pc_points}")
        continue