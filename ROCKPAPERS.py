def rpp():


    import random as r

    rps = "Rock", "Paper", "Scissors"
    robochoice = r.choice(rps)  # Chooses at random R,P,S

    # What the bot chooses, disable to see what is chosen
    # print(robochoice)

    playerchoice = input("Rock Paper or Scissors?: ").capitalize()

    match playerchoice:
        case "Rock":
            if robochoice == "Rock":
                print("Tie")
            elif robochoice == "Scissors":
                print("You Won!")
            elif robochoice == "Paper":
                print("You Lost!")
        case "Paper":
            if robochoice == "Rock":
                print("You Won!")
            elif robochoice == "Scissors":
                print("You Lost!")
            elif robochoice == "Paper":
                print("Tie!")
        case "Scissors":
            if robochoice == "Rock":
                print("You Lost!")
            elif robochoice == "Scissors":
                print("Tie!")
            elif robochoice == "Paper":
                print("You Won!")

        case _:
            print("Error, try typing 'Rock', 'Paper', or 'Scissors'")