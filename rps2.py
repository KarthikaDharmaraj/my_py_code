import random
import sys
from enum import Enum
def play_rps():
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

    if player==1 and computer==3:
        print("🎉you won!")
    elif player==2 and computer==1:
        print("🎉you won!")   

    elif player==3 and computer==2:
        print("🎉you won!")    
    elif player== computer:
        print("😲It's a TIE")   
    else:
        print(" 👀😒computer won !") 
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
         

# play_rps()
if __name__=="__main__":
    play_rps()