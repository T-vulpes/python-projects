import random

print("*****  WELCOME TO THE NUMBER GUESSING GAME!  *****")
print("Rules: ")
print("You have 7 guesses.")
print("You need to guess a number between 1 and 100.\n")

number = random.randint(1, 100)
attempts = 0

while attempts < 7:
    guess = int(input("Enter your guess: "))

    if number == guess:
        print("Congratulations, you guessed it right!")
        break

    elif number > guess:
        print("The number is higher!")
        attempts += 1
        print(f"{attempts}. attempt")

    else:
        print("The number is lower!")
        attempts += 1
        print(f"{attempts}. attempt")

    if attempts == 7:
        print("YOU LOST! The correct number was:", number)
        break

input("Press Enter to exit...")  # Keeps the terminal window open after guessing the number
