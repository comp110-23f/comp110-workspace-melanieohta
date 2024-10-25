"""This program is a more structured wordle game that utilizes functions."""

__author__ = "730671130"


def contains_char(word: str, char: str) -> bool:
    """This function searches through a word 'guess' for a specific character 'char'."""
    assert len(char) == 1
    index: int = 0
    while index < len(word):
        if word[index] == char:
            return True
        index += 1
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(user_guess: str, secret_word: str) -> str:
    """This function compares a guess and a secret word to make an emojified version of wordle."""
    assert len(user_guess) == len(secret_word)
    idx: int = 0
    emoji: str = ""
    while idx < len(secret_word):
        if user_guess[idx] == secret_word[idx]:
            emoji += GREEN_BOX
        else:
            if contains_char(secret_word, user_guess[idx]):
                emoji += YELLOW_BOX
            else:
                emoji += WHITE_BOX
        idx += 1
    return emoji


def input_guess(num_char: int) -> str:
    """This function asks the user to enter a word of a certain number of characters."""
    guess: str = input(f"Enter a { num_char } character word: ")
    # continues to ask player to input a guess until they get the correct length
    while len(guess) != num_char:
        guess = input(f"That wasn't { num_char } chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    game_won: bool = False
    secret: str = "codes"
    # continues until player reaches 6 turns or they win the game
    while turn <= 6 and game_won is False:
        print(f"=== Turn { turn }/6 ===")
        new_guess: str = input_guess(len(secret))
        print(emojified(new_guess, secret))
        if new_guess == secret:
            game_won = True
            print(f"You won in { turn }/6 turns!")
        turn += 1
    if game_won is False:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()