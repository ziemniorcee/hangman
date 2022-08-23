word = "anakonda"
check = list("anakonda")
result = "_" * len(word)
result = list(result)


hang = 0
pics = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="]

win = True

while hang < 6 and win:
    print(result)
    b = 0
    x = input("Podaj literke")
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


