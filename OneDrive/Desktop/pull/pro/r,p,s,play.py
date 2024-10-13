import random

# Initialize counters outside the function to keep track of scores
n = 0  # Ties
m = 0  # Wins
b = 0  # Losses

def play():
    global n, m, b  # Use global to modify the counters
    user = input("Enter your choice (r) for rock, (p) for paper, and (s) for scissors: ")
    computer = random.choice(["r", "p", "s"])
    print(f"Computer chose: {computer}")
    
    if user == computer:
        #return statement will exit a function so first we will increment and then return the statement
        n += 1
        return "It is a tie!"
    
    if win(user, computer):
        m += 1
        return "You won!"
    
    b += 1
    return "You lost!"

def win(x, y):
    if (x == "r" and y == "s") or (x == "s" and y == "p") or (x == "p" and y == "r"):
        return True

# Infinite loop to keep playing the game
while True:
    print(play())
    play_again = input("Do you want to play again? (y/n): ").lower()
    # .lower() converts the input to lowercase
    if play_again != "y":
        print(f"Final score: You won {m} times, you lost {b} times, and it was a tie {n} times.")
        break
