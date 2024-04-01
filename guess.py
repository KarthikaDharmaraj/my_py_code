import random
import sys
import argparse

def guess(name="player1"):
    game_count=0
    player_wins=0
    # name=input("\nEnter your name: ")
    
    def play():
        nonlocal game_count
        nonlocal player_wins
        
        nonlocal name
        
        player_choice=input(f"\nHi {name} \nGuess which number i'm thinking of ....1,2 or 3 \n ")
        
        if player_choice not in["1","2","3"]:
            print(f"\n{name},please enter 1'2'or3")
            return play()
        computer_choice=random.choice("123")
        
        print(f"\n{name},you chose: {player_choice}")
        print(f"\nI was thinking about the number: {computer_choice}")
        player=int(player_choice)
        computer=int(computer_choice)
        def decide_winner(player,computer):
           nonlocal name
           nonlocal player_wins
        
           if player==computer:
               player_wins+=1
               return f"\n{name} , you wone🎉"
               
           else:
               return f"\nSorry {name},Better luck next time 😒"
  
  
        gameresult=decide_winner(player,computer)
        print(gameresult)
        nonlocal game_count
        game_count+=1
        print(f"\n Game count: {game_count}")
        print(f"\n {name}'s wins: {player_wins}")
        print(f"\nYour winning percentage: {player_wins/game_count:.2%}")
        print(f"\nplayagain,{name}?")

        while True:
            playagain=input("\nY for Yes \nq to Quit\n")
            if playagain.lower() not in ["y","q"]:
                continue
            else:
                break
        if playagain.lower()=="y":
            return play()
        else:
            print("Thanks for playing🎉🎉🎉🎉")
            if __name__=="__main__":
                    print(f"Bye {name}")
                    sys.exit(f"Bye {name}👋👋👋")
            else:
                return

            
    return play
#guess_my_number=guess()
# guess_my_number()

if __name__=="__main__":
    parse=argparse.ArgumentParser(
        description="personalised game feel"
    )
    parse.add_argument(
        "-n","--name",metavar="name",
        required=True,help="The player name"
    )
    args=parse.parse_args()
    guess_my_number=guess(args.name)
    
    guess_my_number()






    