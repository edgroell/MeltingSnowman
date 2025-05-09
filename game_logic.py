from ascii_art import STAGES
import random


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word() -> str:
    """
    Select a random word from the list.
    :return: secret_word: str: Word randomly selected from the WORDS constant (list).
    """
    secret_word = WORDS[random.randint(0, len(WORDS) - 1)]

    return secret_word


def get_user_guess() -> str:
    """
    Prompt the user to guess a letter and validate it is a single letter.
    :return: user_guess: str: Current letter guess from the user.
    """
    while True:
        user_guess = input("Guess a letter: ").lower().strip()

        print("\n*******************************************")

        if len(user_guess) == 1 and user_guess not in "0123456789!$%&/()=?@-_#'+*":

            return user_guess

        print("Please enter a single letter.")


def display_game_state(mistakes: int, secret_word: str, guessed_letters: list) -> str:
    """
    Display the current stage of the game based on the current number of mistakes.
    :param mistakes: int: Current number of mistakes done by the user.
    :param secret_word: str: Current secret word picked randomly.
    :param guessed_letters: list: List of all guesses from the user so far.
    :return: display_word: str: Current secret word whereby only correctly guessed letters are displayed.
    """
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])

    display_word = ""

    for letter in secret_word:

        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("*******************************************")
    print("The secret word is: ", display_word)
    print("*******************************************\n")

    return display_word


def prompt_replay() -> str:
    """
    Prompt the user whether they want to play again.
    :return: user_answer: str: The answer provided by the user.
    """
    user_answer = input("\nDo you want to play again? (y/n): ").lower().strip()

    print("\n*******************************************")

    if user_answer == "y":
        play_game()

    return user_answer


def play_game() -> None:
    """
    Articulate the logic of the game and controls the win (guessed all letters of the secret word) or
    lose (too many mistakes) parameters.
    :return: None
    """
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    # Display initial stage
    display_game_state(mistakes, secret_word, guessed_letters)

    while mistakes < len(STAGES) - 1:

        user_guess = get_user_guess()

        if user_guess in guessed_letters:
            print(f"\nYou've tried '{user_guess}' already!")
        else:
            guessed_letters.append(user_guess)

            if user_guess not in secret_word:
                mistakes += 1

                if mistakes == len(STAGES) - 1:
                    print(STAGES[mistakes])
                    print(f"\n>>              GAME OVER!!              << ")
                    print("\n*******************************************")
                    print(f"The secret word was: {secret_word}")
                    print("*******************************************")
                    prompt_replay()
                    break

            display_word = display_game_state(mistakes, secret_word, guessed_letters)

            if "_" not in display_word:
                print(">>Congratulations, you saved the snowman!<<")
                print("\n*******************************************")
                prompt_replay()
                break