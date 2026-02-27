import random
from listofwords import listofwords
from Stages import Stages

def play_game():
    word = list(random.choice(listofwords))
    dash = [" " if i == " " else "_" for i in word]
    lives = 6
    guessed_letters = []

    while lives > 0:
        print(Stages[lives])
        print(f"\nWord: {' '.join(dash)}")
        print(f"Letters guessed: {', '.join(guessed_letters)}")

        if "_" not in dash:
            print(f"Congratulations! You won with {6 - lives} mistakes!")
            return

        guess = input("Enter your letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print(f"--- You already guessed '{guess}'. Try a different one! ---")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for index in range(len(word)):
                if word[index] == guess:
                    dash[index] = guess
            print("Correct!")
        else:
            lives -= 1
            if lives > 0:
                print(f"Wrong! You have {lives} guesses remaining.")
            else:
                print(Stages[0])
                print(f"\nGame Over! The word was: {''.join(word)}")

wish = input("Would you like to play Hangman Python? (y/n):\n").lower()
while wish == "y":
    play_game()
    wish = input("Would you like to play again? (y/n):\n").lower()

print("Bye then")

