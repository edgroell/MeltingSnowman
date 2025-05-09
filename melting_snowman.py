import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    secret_word = get_random_word()
    print("Welcome to Melting Snowman!")
    print("Secret word selected: " + secret_word)  # for testing only, to be removed later

    # TODO: Build game loop here.
    # For now, simply prompts the user once:
    user_guess = input("Guess a letter: ").lower()
    print("You guessed:", user_guess)


if __name__ == "__main__":
    play_game()