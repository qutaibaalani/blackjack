# BlackJack Card Game

# Importing the random module for shuffling the deck
import random

# List of card suits
MY_SUITS = ["♥️", "♦️", "♠️", "♣️"]
# List of card ranks
MY_RANKS = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]


class Card:
    def __init__(self, suit, rank):
        # Initialize card suit
        self.suit = suit
        # Initialize card rank
        self.rank = rank


# Define a class for a playing card with a rank and suit
def __str__(self):
    # Return string representation of the card
    return f"{self.rank} of {self.suit}"


# Define a class for a deck of cards
class Deck:
    def __init__(self, suits, ranks):
        # Initialize an empty list to hold cards
        self.cards = []
        for suit in suits:
            for rank in ranks:
                # Create a new card with given suit and rank
                new_card = Card(suit, rank)
                # Add the card to the deck
                self.cards.append(new_card)

    def __str__(self):
        deck_string = ""
        for card in self.cards:
            deck_string += " " + str(card)
        return deck_string

    # Shuffle the deck of cards
    def shuffle(self):
        random.shuffle(self.cards)


# Define a class for a dealer
class Dealer:
    def __init__(self):
        self.hand = []

    def __str__(self):
        return "Dealer"


# Define a class for a player
class Player:
    def __init__(self, name):
        self.hand = []
        self.name = name

    def __str__(self):
        return self.name

    # Ask the player for their choice to hit or stay
    def choice(self):
        choice = input("Would you like to (h)it or (s)tay? ")
        return choice


# Define a class for the game
class Game:
    def __init__(self, suits, ranks):
        # Create a player object with the player's name
        self.player = Player(self.get_player_name())
        # Create a dealer object
        self.dealer = Dealer()
        # Create a deck object with given suits and ranks
        self.deck = Deck(suits, ranks)
        # Shuffle the deck
        self.deck.shuffle()
        self.deal_card(self.player)
        self.deal_card(self.dealer)
        self.deal_card(self.player)
        self.deal_card(self.dealer)
        self.show_cards()

    # Get the player's name
    def get_player_name(self):
        name = input("What is your name? ")
        return name

    # Deal a card to a person (player or dealer)
    def deal_card(self, person):
        card = self.deck.cards.pop()
        person.hand.append(card)

    # Show the cards of the player and the dealer
    def show_cards(self):
        print(f"{self.player} has:")
        for card in self.player.hand:
            print(card)
        print("Dealer has: ")
        for card in self.dealer.hand:
            print(card)

    # Handle the player's decision to hit or stay
    def player_hand(self):
        choice = self.player.choice()
        if choice == "h":
            self.deal_card(self.player)


# Create a new game object with specified suits and ranks
new_game = Game(MY_SUITS, MY_RANKS)

# Let the player play their hand
new_game.player_hand()

# Show the cards after the player's move
new_game.show_cards()
