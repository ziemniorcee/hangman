from add import pics, words
import random


def hangman():
    word = random.choice(words)
    check = list(word)
    result = "_" * len(word)
    result = list(result)
    hang = 0
    win = True

    while hang < 6 and win:
        print(result)
        print('\033[H\033[2J', end='', flush=True)
        b = 0
        x = input("Podaj literke").lower()

        if x in word:
            for let in word:

                if x == let:
                    result[b] = let
                b = b + 1
        else:
            hang = hang + 1
            print(pics[hang])
        if result == check:
            print("Wygrałeś!")
            win = False
    if hang == 6:
        print("Przegrałeś!")
        print(f"Słowo to: {word}")


hangman()
