from ascii_art import STAGES
import random


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def get_user_guess():
    """Prompts the user to guess a letter and validates it is a single letter."""
    while True:
        user_guess = input("Guess a letter: ").lower().strip()
        print("\n*******************************************")
        if len(user_guess) == 1 and user_guess not in "0123456789!$%&/()=?@-_#'+*":
            return user_guess
        print("Please enter a single letter.")


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

    print("*******************************************")
    print("The secret word is: ", display_word)
    print("*******************************************")
    print()

    return display_word


def prompt_replay():
    user_answer = input("\nDo you want to play again? (y/n): ").lower().strip()
    print("\n*******************************************")

    if user_answer == "y":
        play_game()
    return user_answer


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    # Display initial stage
    display_game_state(mistakes, secret_word, guessed_letters)

    while mistakes < len(STAGES) - 1:
        # Prompt user for guesses
        user_guess = get_user_guess()

        if user_guess in guessed_letters:
            print(f"\nYou've tried '{user_guess}' already!")
        else:
            guessed_letters.append(user_guess)

            if user_guess not in secret_word:
                mistakes += 1
                if mistakes == len(STAGES) - 1:
                    print(f"\nGame Over! The secret word was: {secret_word}")
                    print(STAGES[mistakes])
                    prompt_replay()
                    break

            display_word = display_game_state(mistakes, secret_word, guessed_letters)

            if "_" not in display_word:
                print(">>Congratulations, you saved the snowman!<<")
                prompt_replay()