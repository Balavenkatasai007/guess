import random

def guess(x):
    random_num = random.randint(1,x)
    guess = 0
    while guess != random_num:
        guess=int(input(f"enter a number between 1 and {x}:"))
        if guess < random_num-2:
            print("the number is too low guess another number")
        elif random_num-2 <= guess < random_num:
            print("you almost got the answer just a bit low for the correct answer guess again")
        elif guess > random_num+2:
            print("you are too heigh than the correct answer guess again")
        elif random_num+2 >= guess > random_num:
            print("you almost got the answer you are just bit heigh than the correct answer guess again")
    print("you guessed the right answer congratulations")

guess(10)

def computer_guess(x):
    low=1
    heigh=x
    feedback=""
    t=0
    while feedback!="c":
        if low!=heigh:
            guess=random.randint(1,x)
        else:
            guess=low
        t=t+1

        feedback=input(f"is{guess} is the correct number(c),or very heigh(h),or very low(l)")
        if feedback == "h":
            guess=guess+1
        
        elif feedback == "l":
            guess=guess-1
            
    
    print(f"I guessed the number correctly with in  {t} tries")
computer_guess(100)
        
