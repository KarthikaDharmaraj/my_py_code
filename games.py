from rps4 import rps
from guess import guess
import sys



def play_games(name="Player1"):
    welcome_back=False
    while True:
        if welcome_back==True:
            print(f"\nWelcome back to the games menu{name}")

    
        player_choice=input(f"{name} choose the game you want to play \n1 = Rock paper scissors\n2 = Guess my number\n3 = Exit\n")
        
        if player_choice not in["1","2","3"]:
            print(f"\n {name} pls choose 1,2 or 3")
            return play_games()
        welcome_back=True
        
        if player_choice=="1":
                rock_paper_scissors=rps(name)
                rock_paper_scissors()
        elif  player_choice=="2": 
                guess_num=guess(name) 
                guess_num()
        else:
                sys.exit(f"\nBye {name} 👋👋👋\nHave a nice day 🎉🎉🎉🎉🎉")
            
            
            


if __name__=="__main__":
    import argparse
    parse=argparse.ArgumentParser(
        description="personalised game feel"
    )
    parse.add_argument(
        "-n","--name",metavar="name",
        required=True,help="The player name"
    )
    args=parse.parse_args()
    print(f"\n{args.name} welcome to the GAMES MENU")
    play_games(args.name)
    
    
