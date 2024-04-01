import random
import math

lower=int(input("\nENTER LOWER BOUND: "))
upper=int(input("\nENTER UPPER BOUND: "))

x=random.randint(lower,upper)
num_of_guess=round(math.log(upper-lower+1,2))

print(f'\n You have {num_of_guess} chances to guess  the number ! \n ')
count=0
while count<num_of_guess:
    count +=1
    guess=int(input("Guess the number: "))

    if guess==x:
        print(f"\ncoungratulation🎉 you did it in {count} try")
        break
    elif guess>x:
        print("you guessed greater than the number")
    elif guess<x:
        print("you guessed less than the number")

if count>=num_of_guess:
    print(f"The Number is {x} ")
    print("Better luck next time 👋")