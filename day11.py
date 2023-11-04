# import random

# def deal_card():
#     cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
#     card=random.choice(cards)
#     return card



# def calculate_score(cards):
   
#    if sum(cards)==21 and len(cards)==2:
#        return 0
#    if 11 in cards and sum(cards)>21:
#        cards.remove(11)
#        cards.append(1)
   
#    return sum(cards)

# def compare(user_score,computer_score):
#     if user_score == computer_score:
#         return "draw"
#     elif user_score == 0:
#         return "you win!!!!"
#     elif computer_score == 0 :
#        return "yourr lose"
#     elif user_score>21:
#         return "yourr lose"
#     elif computer_score>21:
#          return "you win!!!!"
#     elif user_score>computer_score:
#          return "you win!!!!"
#     else:
#         return "you llllloseeeee!!!"
# def play_again():
#     user_card=[]
#     computer_card=[]
#     is_game_over=False



#     for _ in range(2):
#         user_card.append(deal_card())
#         computer_card.append(deal_card())

#     while not is_game_over:
#         user_score=calculate_score(user_card)
#         computer_score=calculate_score(computer_card)
#         print(f"your card{user_card}and{user_score}")
#         print(f"Computer's first card: {computer_card[0]}")

#         if user_score ==0 and computer_score == 0 and user_score >21 :
#             is_game_over=True
#         else:
#             should_deal=input('what do you have pass cards"y","n"')
#             if should_deal == "y":
#                 user_card.append(deal_card())
#             else:
#                 is_game_over=True

#     while computer_score !=0 and computer_score<17:
#         computer_card.append(deal_card())
#         computer_score=calculate_score(computer_card)
#     print(f"your finally card{user_card},and your score{user_score}")
#     print(f"computer finally cards{computer_card}and finally score{computer_score}")
#     print(compare(user_score,computer_score))

# while input("what do you play again?")=="y":
#     play_again()



   
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def display_hand(cards, score):
    print(f"Cards: {cards}, Score: {score}")

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw!"
    elif user_score == 0:
        return "You win!"
    elif computer_score == 0:
        return "You lose."
    elif user_score > 21:
        return "You lose."
    elif computer_score > 21:
        return "You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose."

def play_game():
    user_card = []
    computer_card = []

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    is_game_over = False

    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)

        display_hand(user_card, user_score)
        print(f"Computer's first card: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            should_deal = input('Do you want to draw another card? "y" or "n": ')
            if should_deal == "y":
                user_card.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    display_hand(user_card, user_score)
    print(f"Computer's final cards: {computer_card}, Score: {computer_score}")
    result = compare(user_score, computer_score)
    print(result)

    # 計算勝場數
    if result == "You win!":
        return 1
    return 0

# 初始化勝場數
wins = 0

while input("Do you want to play again? Enter 'y' to continue: ") == "y":
    wins += play_game()
    print(f"Total wins: {wins}")
