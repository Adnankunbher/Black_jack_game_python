
import random
from blackjack_logo import logo
print(logo)

def play_game():
    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card=random.choice(cards)
        return card

    def calculate_score(cards):
        """Take a list of cards and return score calculated from the cards"""
        if sum(cards)==21 and len(cards)==2:
            return 0
        if 11 in cards and sum(cards)>21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)
    def compare(user_score,computer_score):

        if computer_score==0:
            return 'Lose, Opponent has Black jack'
        elif user_score==0:
            return 'Wins with Blackjack'
        elif user_score>21:
            return 'You went over! You Lose'
        elif computer_score>21 or computer_score<0:
            return 'Opponent went Over! You win'
        elif computer_score>user_score:
            return 'Computer wins'
        elif computer_score == user_score:
            return 'Its Draw'
        else:
            return 'You win'
    user_cards = []
    computer_cards = []
    is_gameover=False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_gameover:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)

        print(f"Your Cards: {user_cards}, Current Score: {user_score}")
        print(f"Computer's First Cards: {computer_cards[0]}")

        if user_score ==0 or computer_score==0 or user_score>21:
                is_gameover=True
        else:
            user_should_deal=input("Type 'y' to get another card, Type 'n' to pass. " )
            if user_should_deal=='y':
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
            else:
                is_gameover=True

    while computer_score != 0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)
    print(compare(user_score,computer_score))


while input("Do you want to play of Blackjack? Type 'y' or 'n': ")=='y':
    play_game()
    


