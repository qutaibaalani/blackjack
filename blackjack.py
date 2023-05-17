# BlackJack Card Game 💰🃏🎲🍺

# Importing the random module for shuffling the deck
import random

# Define a list of suits
suits = ["♥️", "♠️", "♦️", "♣️"]

# Define a list of ranks
ranks = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]


# Define the Card class
class Card:
    def __init__(self, suit, rank):
        # Initialize card suit
        self.suit = suit
        # Initialize card rank
        self.rank = rank

    # Define a class for a playing card with a rank and suit
    def __str__(self):
        return f"{self.rank} of {self.suit}"


# Define a class for a deck of cards
class Deck:
    def __init__(self, suits, ranks):
        self.cards = []
        # Create a deck of cards by iterating over suits and ranks
        for suit in suits:
            # Iterate over the list of ranks
            for rank in ranks:
                # Create a new Card object with the current suit and rank
                new_card = Card(suit, rank)
                # Add the new card to the deck
                self.cards.append(new_card)

    def __str__(self):
        # Convert the deck of cards to a string
        deck_string = ""
        for card in self.cards:
            # Convert the card to a string and append it to the deck_string
            deck_string += str(card) + "\n"
        # Return the final deck_string
        return deck_string

    def shuffle(self):
        # Shuffle the deck of cards
        random.shuffle(self.cards)


# Define a class for a dealer
class Dealer:
    def __init__(self):
        # Initialize an empty list to store the dealer's hand
        self.hand = []

    def __str__(self):
        # Return the string representation of the dealer
        return "Dealer"

    def hit(self, card):
        # Add a card to the dealer's hand
        self.hand.append(card)


# Define a class for a player
class Player:
    def __init__(self, name):
        # Initialize an empty list to store the player's hand
        self.hand = []
        # Set the player's name
        self.name = name

    def __str__(self):
        # Return the player's name when converting the object to a string
        return self.name

    def hit(self, card):
        # Add a card to the player's hand
        self.hand.append(card)

    # Ask the player for their choice to hit or stay
    def choice(self):
        # Get the player's choice to hit or stay
        choice = input("Would you like to (h)it or (s)tay?")
        return choice


# Define the Game class
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
        # Deal initial cards to the player and the dealer
        self.deal_card(self.player)
        self.deal_card(self.dealer)
        self.deal_card(self.player)
        self.deal_card(self.dealer)
        # Show the current cards of the player and the dealer
        self.show_cards()

    def get_player_name(self):
        # Get the player's name
        name = input("What is your name?")
        return name

    def deal_card(self, person):
        # Deal a card to a person
        card = self.deck.cards.pop()
        person.hit(card)

    def show_cards(self):
        # Show the player's and dealer's cards
        print(f"{self.player} has:")
        for card in self.player.hand:
            print(card)
        print("Dealer has:")
        for card in self.dealer.hand:
            print(card)

    def player_hand(self):
        # Handle the player's hand for their choice
        choice = self.player.choice()
        # Continue loop as long as player chooses to hit
        while choice == "h":
            # Deal a card to the player
            self.deal_card(self.player)
            # Show the player's cards
            self.show_cards()
            # Check if player's hand value exceeds 21
            if self.calculate_hand_value(self.player.hand) > 21:
                print("Bust! You lose.")
                # Return from the method
                return
            # Prompt the player for their choice again
            choice = self.player.choice()
        # Call the dealer_hand method to handle the dealer's hand
        self.dealer_hand()

    def dealer_hand(self):
        # Show the dealer's cards
        self.show_cards()
        # Continue loop as long as dealer's hand value is less than 17
        while self.calculate_hand_value(self.dealer.hand) < 17:
            # Deal a card to the dealer
            self.deal_card(self.dealer)
            # Show the dealer's cards
            self.show_cards()
        # Call the calculate_winner method
        self.calculate_winner()

    def calculate_hand_value(self, hand):
        value = 0
        num_aces = 0
        for card in hand:
            # If the card is an Ace
            if card.rank == "A":
                value += 11
                num_aces += 1
            # If the card is a King, Queen, or Jack
            elif card.rank in ["K", "Q", "J"]:
                value += 10
            else:
                value += card.rank
        # Continue loop as long as the value exceeds 21 and there are still Aces present
        while value > 21 and num_aces > 0:
            # Subtract 10 from the value
            value -= 10
            # Decrement the number of Aces
            num_aces -= 1

        return value

    def calculate_winner(self):
        # Calculate the value of the player's hand
        player_value = self.calculate_hand_value(self.player.hand)
        # Calculate the value of the dealer's hand
        dealer_value = self.calculate_hand_value(self.dealer.hand)
        # Print the value of the player's hand
        print(f"Player: {player_value}")
        # Print the value of the dealer's hand
        print(f"Dealer: {dealer_value}")

        if player_value > 21:
            print("Bust! You lose.")
        elif dealer_value > 21:
            print("Dealer busts! You win.")
        elif player_value > dealer_value:
            print("You win!")
        elif player_value < dealer_value:
            print("You lose.")
        else:
            print("No one comes out as the clear winner.")

    def play(self):
        # Call the player_hand method to start the game
        self.player_hand()


# Create a new game object with specified suits and ranks
new_game = Game(suits, ranks)

# Let the player play their hand
new_game.play()
