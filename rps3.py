import random
import sys
from enum import Enum
def rps():
    game_count=0
    player_wins=0
    computer_wins=0
    def play_rps():
            
            nonlocal player_wins
            nonlocal computer_wins

            class RPS(Enum):
                ROCK=1
                PAPER=2
                SCISSORS=3
            


            #print(RPS(1)) OUTPUT is RPS.ROCK
            player_choice= input("Enter 1 for ROCK\nEnter 2 for paper\nEnter 3 for scissors\n")
        
            if player_choice not in ["1","2","3"]:
                print("oh no! You must enter 1,2 or 3")
                return play_rps()
                #sys.exit("oh no! You must enter 1,2 or 3")
            player=int(player_choice)

            #print(player)
            computer_choice=random.choice("123")
            computer=int(computer_choice)

            print("you chose "+str(RPS(player)).replace("RPS.","")+".") #replace is to revome RPS.
            print("computer chose "+str(RPS(computer)).replace("RPS.","")+".")
            print("")
            def decide_winner(player,computer):
                nonlocal player_wins
                nonlocal computer_wins 
                if player==1 and computer==3:
                
                    player_wins+=1
                    return"🎉you won!"
                elif player==2 and computer==1:
                    
                    player_wins+=1
                    return "🎉you won!"

                elif player==3 and computer==2:
                    player_wins+=1
                    return "🎉you won!"
                        
                elif player== computer:
                    
                    return"😲It's a TIE" 
                 
                else:
                    computer_wins+=1
                    return" 👀😒computer won !"
                   
            game_result=decide_winner(player,computer)
            print(game_result)
            nonlocal game_count
            game_count+=1
            print("Game count: "+str(game_count))
            print("player wins: "+str(player_wins))
            print("computer wins: "+str(computer_wins))
            print("\n Play again?")
            while True:
                playagain =input("\nY for yes\nQ for quit\n\n")
                if playagain.lower() not in ["q","y"]:
                    continue
                else:
                    break
            if playagain.lower()=="y":
                return play_rps()
            

            
            else:
                print("Thanks for playing !🎉🎉🎉🎉")
                sys.exit('Bye 👋👋')
                
    return play_rps
play=rps()

play()