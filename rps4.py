import random
import sys
from enum import Enum
def rps(name="Player1"):
    game_count=0
    player_wins=0
    computer_wins=0
    def play_rps():
            nonlocal name
            nonlocal player_wins
            nonlocal computer_wins

            class RPS(Enum):
                ROCK=1
                PAPER=2
                SCISSORS=3
            


            #print(RPS(1)) OUTPUT is RPS.ROCK
            player_choice= input(f"\n{name}\nEnter 1 for ROCK\nEnter 2 for paper\nEnter 3 for scissors\n")
        
            if player_choice not in ["1","2","3"]:
                print(f"\n{name}oh no! You must enter 1,2 or 3")
                return play_rps()
                #sys.exit("oh no! You must enter 1,2 or 3")
            player=int(player_choice)

            #print(player)
            computer_choice=random.choice("123")
            computer=int(computer_choice)

            print(f"you chose {str(RPS(player)).replace("RPS.","")}.") #replace is to revome RPS.
            print(f"computer chose {str(RPS(computer)).replace("RPS.","")}.")
            print("")
            def decide_winner(player,computer):
                nonlocal name
                nonlocal player_wins
                nonlocal computer_wins 
                if player==1 and computer==3:
                
                    player_wins+=1
                    return f"{name}🎉you won!"
                elif player==2 and computer==1:
                    
                    player_wins+=1
                    return f"{name}🎉you won!"

                elif player==3 and computer==2:
                    player_wins+=1
                    return f"{name}🎉you won!"
                        
                elif player== computer:
                    
                    return"😲It's a TIE" 
                 
                else:
                    computer_wins+=1
                    return" 👀😒computer won !"
                   
            game_result=decide_winner(player,computer)
            print(game_result)
            nonlocal game_count
            game_count+=1
            print(f"Game count: {game_count}")
            print(f"{name}'s wins: {player_wins}")
            print(f"computer wins: {computer_wins}")
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
                if __name__=="__main__":
                    print(f"Bye {name}")
                    sys.exit(f"Bye {name}👋👋👋")
                else:
                    return
                
    return play_rps
#rock_paper_scissor=rps()
if __name__ == "__main__":
    import argparse
    parse=argparse.ArgumentParser(
        description="provides a personalized game experience"
    )
    parse.add_argument(
        "-n","--name",metavar="name",
        required=True,help="The name of the person playing."
    )
    args=parse.parse_args()
    rock_paper_scissor=rps(args.name)
    rock_paper_scissor()