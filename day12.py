from random import randint

EASY_LEVEL=10
HARD_LEVEL=5

def correct(answer,guess,turns):
    if guess>answer:
        print("too high!")
        return turns -1
    elif guess<answer:
        print("too low")
        return turns -1
    else:
        print(f"you got it,correct: {answer}")

def set_diffcultly():
    level=input("what is your level?").lower()
    if level=="easy":
        return EASY_LEVEL
    elif level == "hard":
        return HARD_LEVEL
def game():   
    print("hello! welcome to number house!")
    print("choice your number?")
    answer=randint(1,100)
    print(f"your correct answer is {answer}")
    turns=set_diffcultly()
    

    X=20
    while X>15: 
        print(f"ypu have {turns} attempts,")
    #guess the number
        guess=int(input("make a guess"))
        turns=correct(answer, guess,turns)
        if turns==0:
            print("you are lose")
            break



game()