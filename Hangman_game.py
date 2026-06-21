import random

def hangman():
    words = ["python", "hangman", "random", "string", "loops"]
    word = random.choice(words)
    guessed_word = ["_"] * len(word)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Guess the word: ", " ".join(guessed_word))

    while attempts > 0 and "_" in guessed_word:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f"Wrong guess! '{guess}' is not in the word.")
            print(f"Attempts left: {attempts}")

        print("Words: ", " ".join(guessed_word))

    if "_" not in guessed_word:
        print("Congratulations! You guessed the word:", word)
    else:
        print("Out of attempts! The word was:", word)

hangman()
