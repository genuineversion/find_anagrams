import random

welcomeNote= "Welcome to the Rock, Paper & Scissors Game. Here, you aim at beating your opponent. \n Rule of the game: \n 1. Rock > Scissors \n 2. Scissors > Paper \n 3. Paper > Rock \n \n"

#This is the dictionary holding the keys (word) and value (codes) the players (player and CPU) are expected to choose.
gameKeys={"rock":"R", "paper":"P", "scissors":"S"}

#The values (i.e. options to be selected) are stored in this list 
gameOptions=[gameKeys["rock"], gameKeys["paper"], gameKeys["scissors"]]

#The final display require the choice of each player to be selected. While the players play using the game options which are codes, this link the codes with what it signifies.  
outputMapping={"R":"Rock", "P":"Paper", "S":"Scissors"}

#These are the players in this game. The lists holds the information.
players=["Player", "CPU"]

def rpsGame ():
    playAgain="yes"

    while playAgain=="yes":
        #The computer choice will be randomly selected while the Player will enter a choice using the input.
        cpuChoice=random.choice(gameOptions)
        playerChoice=input("Select your choice: R, P or S \n")
        #This checks if the Player selection is valid, i.e. if R, P or S has been selected. If no, it restarts the game
        if playerChoice not in gameKeys.values():
            print("Invalid options selected. Choose R, P or S")
            playAgain="yes"
        #This checks if the Player and CPU inputs are the same.
        elif playerChoice==cpuChoice:
            print(f"{players[0]} ({outputMapping[playerChoice]}) : {players[1]} ({outputMapping[cpuChoice]})")
            print(f"This is a draw, kindly play again")
            #Since it is a draw, this automatically restarts the game
            playAgain="yes"
        
        elif playerChoice==gameKeys["rock"] and cpuChoice==gameKeys["scissors"]:
            winner=players[0]
            print(f"{players[0]} ({outputMapping[playerChoice]}) : {players[1]} ({outputMapping[cpuChoice]})")
            print(f"Congratulations {winner}")
            playAgain=input("Do You want to play again? yes or no \n")

        elif playerChoice==gameKeys["scissors"] and cpuChoice==gameKeys["rock"]:
            winner=players[1]
            print(f"{players[0]} ({outputMapping[playerChoice]}) : {players[1]} ({outputMapping[cpuChoice]})")
            print(f"Congratulations {winner}")
            playAgain=input("Do You want to play again? yes or no \n")
        
        elif playerChoice==gameKeys["scissors"] and cpuChoice==gameKeys["paper"]:
            winner=players[0]
            print(f"{players[0]} ({outputMapping[playerChoice]}) : {players[1]} ({outputMapping[cpuChoice]})")
            print(f"Congratulations {winner}")
            playAgain=input("Do You want to play again? yes or no \n")

        elif playerChoice==gameKeys["paper"] and cpuChoice==gameKeys["scissors"]:
            winner=players[1]

            print(f"{players[0]} ({outputMapping[playerChoice]}) : {players[1]} ({outputMapping[cpuChoice]})")
            print(f"Congratulations {winner}")
            playAgain=input("Do You want to play again? yes or no \n")

        elif playerChoice==gameKeys["paper"] and cpuChoice==gameKeys["rock"]:
            winner=players[0]
            print(f"{players[0]} ({outputMapping[playerChoice]}) : {players[1]} ({outputMapping[cpuChoice]})")
            print(f"Congratulations {winner}")
            playAgain=input("Do You want to play again? yes or no \n")

        elif playerChoice==gameKeys["rock"] and cpuChoice==gameKeys["paper"]:
            winner=players[1]
            print(f"{players[0]} ({outputMapping[playerChoice]}) : {players[1]} ({outputMapping[cpuChoice]})")
            print(f"Congratulations {winner}")
            playAgain=input("Do You want to play again? yes or no \n")

print(welcomeNote)

print(f"The game keys are as follows:\n Rock is {gameKeys['rock']} \n Paper is {gameKeys['paper']} \n Scissors is {gameKeys['scissors']}\n \n")

rpsGame ()