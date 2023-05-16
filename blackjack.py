# BlackJack Card Game


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

    # Return string representation of the card
    def __str__(self):
        return f"{self.rank} of {self.suit}"


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
            # Concatenate the string representation of each card
            deck_string += " " + str(card)
        # Return the string representation of the deck
        return deck_string

    def shuffle(self):
        # Shuffle the deck
        random.shuffle(self.cards)


class Dealer:
    def __init__(self):
        # Initialize an empty list to hold dealer's cards
        self.hand = []

    def __str__(self):
        # Return the string representation of the dealer
        return "Dealer"

    def hit(self, card):
        # Add a card to the dealer's hand
        self.hand.append(card)


class Player:
    def __init__(self, name):
        # Initialize an empty list to hold player's cards
        self.hand = []
        # Initialize player's name
        self.name = name

    def __str__(self):
        # Return the player's name as the string representation
        return self.name

    def hit(self, card):
        # Add a card to the player's hand
        self.hand.append(card)


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

    def get_player_name(self):
        # Prompt the user to enter their name
        name = input("What is your name? ")
        # Return the player's name
        return name

    def __str__(self):
        # Return the string representation of the game
        return f"Game: {self.player} vs. {self.dealer}\nDeck: {self.deck}"


def main():
    # Create a new game object
    new_game = Game(MY_SUITS, MY_RANKS)
    # Print the string representation of the game
    print(new_game)


if __name__ == "__main__":
    main()
