"""A wordle game where the user only has one chance to guess the secret word."""
__author__ = "730671130"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret: str = "python"
guess: str = input("What is your " + str(len(secret)) + "-letter guess? ")
index: int = 0
emoji: str = ""

while len(guess) != 6:
    print(input("That was not 6 letters! Try again: "))

while index < len(secret):
    if guess[index] == secret[index]:
        emoji += GREEN_BOX
    else:
        guess_elsewhere: bool = False
        other_index: int = 0
        while bool == False and other_index < len(secret):
            if secret[other_index] == guess[index]:
                guess_elsewhere = True
            else:
                other_index += other_index
        if guess_elsewhere == True:
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
    
    index += 1
    print(emoji)
    
if secret != guess:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")