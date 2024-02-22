import random

def slot_machine():
    print("PACHINKO!")
    spin_reels()

def spin_reels():
    symbols = ['#', '@', '&', '$']
    tokens = 100
    
    print("Welcome to slots game")
    
    while tokens > 0:
        print("You have", tokens, "tokens.")

        try:
            bet = int(input("Please enter the number of tokens to bet: "))
        except ValueError:
            print("Enter a whole number")
            continue
        
        if bet > tokens:
            print("Not enough tokens")
        else:
            tokens -= bet
            
            # Spin the reels and get random symbols for each reel
            reel1 = random.choice(symbols)
            reel2 = random.choice(symbols)
            reel3 = random.choice(symbols)

            # Display the result
            print("Result 1:", reel1, "Result 2:", reel2, "Result 3:", reel3)

            # Check winning
            if reel1 == reel2 == reel3:
                print("Congratulations! You won", bet*100, "tokens!")
                tokens += bet * 100
            else:
                print("Better luck next time.")

    print("No more tokens left.")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        slot_machine()
    else:
        print("NO MONEY LEFT, I GUESS")

# Game runner
slot_machine()