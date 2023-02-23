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
        card_value = 0
        score = 0
        for card in self.hand:
            if card.rank in ['J', 'Q', 'K']:
                card_value = 10
            elif card.rank == 'A':
                if score >= 11:
                    card_value = 1
                else:
                    card_value = 11
            else:
                card_value = card.rank
            score += card_value
        print('Player score: ', score)
        return score


class Dealer(Player):
    def __init__(self):
        self.name = 'Dealer'
        self.hand = []

    def __str__(self):
        # when we write cariables and methods with the same
        # as the parent class, they override the code from
        # the parent class (Player)
        return f'{self.name} is the dealer'

    def calculate(self):
        card_value = 0
        score = 0
        for card in self.hand:
            if card.rank in ['J', 'Q', 'K']:
                card_value = 10
            elif card.rank == 'A':
                if score >= 11:
                    card_value = 1
                else:
                    card_value = 11
            else:
                card_value = card.rank
            score += card_value
        print('Dealer score: ', score)
        return score


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
        # for card in self.deck.cards:
        #     print(card)

    def deal(self):
        self.setup()
        self.deck.shuffle()
        print(new_game.player)
        card = self.deck.cards.pop()
        self.player.hand.append(card)
        card = self.deck.cards.pop()
        self.player.hand.append(card)
        print(f'{self.player.name}s hand is ')
        self.player.view_cards()
        print(new_game.dealer)
        card = self.deck.cards.pop()
        self.dealer.hand.append(card)
        card = self.deck.cards.pop()
        self.dealer.hand.append(card)
        print('Dealer hand is ')
        self.dealer.view_cards()

    def player_turn(self):  # player decides how many times to hit before playing
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
