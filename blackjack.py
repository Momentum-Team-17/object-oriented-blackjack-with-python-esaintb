import random

SUITS = ['♠', '♥', '♦', '♣']
RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']


# OBJECT CLASSES
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    def __init__(self):
        self.cards = []
        self.add_cards()

    def add_cards(self):
        for suit in SUITS:
            for rank in RANKS:
                new_card = Card(suit, rank)
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)


class Player:
    def __init__(self):
        self.name = input("What is your name? ")
        self.hand = []

    def __str__(self):
        return f'{self.name} is the player'

    def view_cards(self):
        for card in self.hand:
            print(card)

    def calculate(self):
        pass


class Dealer(Player):
    def __init__(self):
        self.name = 'Dealer'
        self.hand = []

    def __str__(self):
        # when we write cariables and methods with the same
        # as the parent class, they override the code from
        # the parent class (Player)
        return f'{self.name} is the dealer'

    def end_game(self):
        pass


class Game:
    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()
        self.setup()

    def setup(self):
        # creates a deck
        self.deck = Deck()
        # adds card for deck
        self.deck.add_cards()
        for card in self.deck.cards:
            print(card)

    def deal(self):
        pass

    def player_turn(self):  # player decides how many times to hit before playig
        pass

    def dealer_turn(self):
        pass


new_game = Game()

# TO DO
# make a player, like we did with Deck
# make a dealer, also like we did with Deck
# play game
# shuffle deck
# deal cards
# players turn first (hit/stay)
# calculate score from cards in hand
# who won/lost/busted/21
# dealers turn
