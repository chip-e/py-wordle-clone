# py_wordle_clone.py

import pathlib #file path handling
import random
from string import ascii_letters
from rich.console import Console
from rich.theme import Theme

console = Console(width=40, theme=Theme({"warning": "red on yellow"}))

def main():
    # Pre-process
    word_path = pathlib.Path(__file__).parent / "wordlist.txt"
    word = get_random_word(word_path.read_text(encoding="utf-8").split("\n"))

    # Process (main loop)
    for guess_try in range (1,7):
        print(word)
        guess = input(f"\nGuess {guess_try}: ").upper()

        show_guess(guess, word)
        if guess == word:
            print("\nCorrect")
            break

    # Post-Process
    else:
        game_over()

def get_random_word(word_list):
    """ Get random 5-letter word from list of strings.

    ## Example:

    >>> get_random_word(["snake", "worm", "it'll"])
    'SNAKE'
    """

    words = [
        word.upper()
        for word in word_list
        if len(word) == 5 and all(letter in ascii_letters for letter in word)
    ]
    return random.choice(words)

def show_guess(guess, word):
    # doctest
    """Show the user's guess on the terminal and classify all letters.

    ## Example:

    >>> show_guess("CRANE", "SNAKE")
    Correct letters: A, E
    Misplaced letters: N
    Wrong letters: C, R
    """

    correct_letters = {
        letter for letter, correct in zip(guess, word) if letter == correct
    }
    misplaced_letters = set(guess) & set(word) - correct_letters
    wrong_letters = set(guess) - set(word)

    print("Correct letters:", ", ".join(sorted(correct_letters)))
    print("Misplaced letters:", ", ".join(sorted(misplaced_letters)))
    print("Wrong letters:", ", ".join(sorted(wrong_letters)))

def game_over(word):
    print(f"The word was {word}")

def refresh_page(headline):
    console.clear()
    console.rule(f"[bold blue]:books: {headline} :books:[/]\n")

if __name__ == "__main__":
    main()

