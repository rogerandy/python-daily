import random

word_list = ["roger", "lisa", "changmin"]
guess = random.choice(word_list)
word_length = len(guess)

end_of_game = False
level = 6

print(f"Your answer: {guess}")

display = ["_" for _ in range(word_length)]
print(' '.join(display))

while not end_of_game:
    enter_your_word = input("What is your word??").lower()
    letter_matched = False

    for position in range(word_length):
        letter = guess[position]
        if letter == enter_your_word:
            display[position] = letter
            letter_matched = True

    if not letter_matched:
        level -= 1
        print("no match!")
        if level == 0:
            print("game over")
            end_of_game = True  

    print(' '.join(display))

    if "_" not in display:
        print("you win")
        end_of_game = True  

