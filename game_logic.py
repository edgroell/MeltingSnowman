from ascii_art import STAGES
import random


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print()

    return display_word


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    # Display initial stage
    display_game_state(mistakes, secret_word, guessed_letters)

    while mistakes < len(STAGES) - 1:
        # Prompt user for guesses
        user_guess = input("Guess a letter: ").lower()

        if user_guess in guessed_letters:
            print(f"You've tried '{user_guess}' already!")
        else:
            guessed_letters.append(user_guess)

            if user_guess not in secret_word:
                mistakes += 1

                if mistakes == len(STAGES) - 1:
                    print(f"Game Over! The secret word was: {secret_word}")
                    print(STAGES[mistakes])
                    break

            display_word = display_game_state(mistakes, secret_word, guessed_letters)

            if "_" not in display_word:
                print("Congratulations, you saved the snowman from melting!")
                break