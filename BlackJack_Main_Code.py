import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
dealer_cards = []

# Function definitions

def deal_cards(num_cards, the_user):
    if the_user == "player":
        for i in range(num_cards):
            player_cards.append(cards[random.choice(cards)])
        print(f"Player cards: {player_cards}")
             
    if the_user == "dealer":
        for i in range(num_cards):
            dealer_cards.append(cards[random.choice(cards)])
        print(f"Dealer cards: {dealer_cards}")
    
def calculate_score(the_user):
    invalid_pair = [11, 11]
    cards_sum = sum(the_user)    
    
    if the_user == player_cards:
        current_user = "Player"
        
    elif the_user == dealer_cards:
        current_user = "Dealer"           
    
    if the_user == invalid_pair:
        the_user = [11, 1]        
        cards_sum = sum(the_user)
        
    print(f"{current_user} total: {cards_sum}")
        
    if cards_sum == 21:
        cards_sum = 0
        # print(f"{current_user} has Blackjack! >>>>GAME OVER<<<<")        
    
    if cards_sum > 21:
        # print(f"{current_user} BUST!")
        return

# Create a function called compare() and pass in the user_score and computer_score
def compare(user_score, computer_score):
    
    # If the computer and user both have the same score, then it's a draw. 
    if user_score == computer_score:
        print("PUSH!")
    
    # If the computer has (0), then the user loses. 
    elif computer_score == 0:
        print("Dealer has Blackjack. You lose.")
    
    # If the user has (0), then the user wins.     
    elif user_score == 0:
        print("You have Blackjack. You win!")
    
    # If the user_score is over 21, then the user loses.     
    elif user_score > 21:
        print("You Bust. You lose.")
    
    # If the computer_score is over 21, then the computer loses. 
    elif computer_score > 21:
        print("Dealer Bust. You win!")
        
    elif user_score > computer_score:
        print("Your score is higher, you win!")
        
    else:
        print("Your score is lower, you lose.") 
        
# Function Calls
deal_cards(2, "player") # Deals player starting cards
deal_cards(2, "dealer") # Deals dealer starting cards
calculate_score(player_cards) # Calculate player score
calculate_score(dealer_cards) # Calculate dealer score

"""
Ask the user if they want to restart the game. If they answer yes, clear the console and start a new 
game of blackjack
"""

game_on = True

while game_on is True:
    
    hit = input("Do you want to hit? 'y' or 'n' ").lower()
    
    if hit == 'y':
        deal_cards(1, "player")
        calculate_score(player_cards)
        
        # Check if the player's score is greater than or equal to 21
        if sum(player_cards) >= 21:
            game_on = False
    else:
        game_on = False

# Dealer's turn
while sum(dealer_cards) < 17:
    
    deal_cards(1, "dealer")
    calculate_score(dealer_cards)

compare(sum(player_cards), sum(dealer_cards))