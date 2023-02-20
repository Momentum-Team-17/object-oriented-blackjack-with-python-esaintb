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

    def add_cards(self):
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

        def shuffle(self):
            random.shuffle(self.deck)

        def deal(self):
            single_card = self.deck.pop()
            return single_card


test_deck = Deck()
print(test_deck)


class Game:
    def __init__(self):
        self.player = None
        self.dealer = None
        self.deck = None


class Player:
    def __init__(self):
        self.cards = []
        self.dealer = dealer
        self.game = game
        self.turn = turn


class Dealer:
    def __init__(self):
        self.cards = cards
        self.deck = deck
        self.game = game
        self.turn = turn

    def setup(self):
        # calls line 12
        self.deck = Deck()
        # calls line 15
        self.deck.add_cards()
        for card in self.deck.cards:
            print(card)

# def play_game():


# new_game = Game()
# new_game.setup()

# created the game and the deck with cards

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
