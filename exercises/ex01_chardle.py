"""Ex01 - Chardle, a freshman CS major's version of wordle."""

__author__ = "730671130"

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

character: str = input("Enter a single character: ")
if len(character) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + character + " in " + word)

num_match: int = 0

if word[0] == character:
    print(character + " found at index 0")
    num_match += 1

if word[1] == character:
    print(character + " found at index 1")
    num_match += 1

if word[2] == character:
    print(character + " found at index 2")
    num_match += 1

if word[3] == character:
    print(character + " found at index 3")
    num_match += 1

if word[4] == character:
    print(character + " found at index 4")
    num_match += 1

if num_match > 1:
    print(str(num_match) + " instances of " + character + " found in " + word)
elif num_match == 1:
    print(str(num_match) + " instance of " + character + " found in " + word)
else:
    print("No instances of " + character + " found in " + word)