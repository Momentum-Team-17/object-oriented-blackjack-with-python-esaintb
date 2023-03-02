import random

SUITS = ['♠', '♥', '♦', '♣']
RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']


# OBJECT CLASSES
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank}{self.suit}'


class Deck:

    def __init__(self):
        self.cards = []
        self.add_cards()

    def __str__(self):
        output = []
        for card in self.cards:
            output.append(str(card))
        return str(output)

    def add_cards(self):
        for suit in SUITS:
            for rank in RANKS:
                new_card = Card(suit, rank)
                # print(new_card)
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_cards(self, n):
        drawn_cards = []
        for i in range(n):
            drawn_cards.append(self.cards.pop(0))
        return drawn_cards


class Player:
    def __init__(self):
        # self.name = input("What is your name? ")
        self.hand = []
        self.score = 0
        # TODO CHANGE BELOW THIS LINE
        self.name = "emmaline"
        self.calculate()

    def __str__(self):
        return f'{self.name} is the player'

# setting parameter (communicates between two separate classes) of card to connect the two objects
    def add_cards_to_player(self, cards):
        self.hand.extend(cards)
        # self.calculate

    def view_hand(self):
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
        # print('Your score: ', score)
        return score


class Dealer(Player):
    def __init__(self):
        self.name = 'Dealer'
        self.hand = []
        self.score = 0
        self.calculate()

    def __str__(self):
        # when we write cariables and methods with the same
        # as the parent class, they override the code from
        # the parent class (Player)
        return f'{self.name} is the dealer'

    # setting parameter (communicates between two separate classes) of card to connect the two objects
    def add_cards_to_dealer(self, cards):
        self.hand.extend(cards)

    def view_hand(self):
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
        # print('Dealer score: ', score)
        return score


class Game:
    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()
        self.deck = Deck()
        self.deck.shuffle()
        print(self.deck)
        self.deal_player()
        # self.deal_dealer()

    def deal_player(self):
        print("Your hand:")
        dealing_it = self.deck.draw_cards(2)
        self.player.add_cards_to_player(dealing_it)
        self.player.view_hand()
        # dealing_it = self.deck.draw_cards(2)
        # self.dealer.add_cards_to_dealer(dealing_it)
        # self.dealer.view_hand()

    def deal_dealer(self):
        print("Dealer's hand:")
        dealing_it = self.deck.draw_cards(2)
        self.dealer.add_cards_to_player(dealing_it)
        self.dealer.view_hand()

    def player_turn(self):
        while "decision" != "stay":
            player_total = self.player.calculate()
            decision = input("hit or stay? ")
            if (decision == "hit") or (decision == "Hit"):
                self.player.add_cards_to_player(self.deck.draw_cards(1))
                self.player.view_hand()
                print(f'Your score: {self.player.calculate()}')
            elif (decision == "stay") or (decision == "Stay"):
                print(f'Your score: {self.player.calculate()}')
                break
        dealer_sum = 0
        self.deal_dealer()
        while dealer_sum < 17:
            dealer_total = self.dealer.calculate()
            self.dealer.add_cards_to_dealer(self.deck.draw_cards(1))
            dealer_sum += dealer_total
            self.dealer.view_hand()
            print(f'Dealer score: {self.dealer.calculate()}')
            print(dealer_sum)
            if dealer_sum > 21:
                print("Dealer Bust!")
            elif dealer_sum == player_total:
                print("Tie!")
            elif dealer_sum > player_total:
                print("Dealer wins!")
            else:
                print("player wins")
                print(dealer_sum)
                print(player_total)
            break
            # else:
            #     print("oopsie, type something else")


# sets game-ending parameters

    def end_game(self, winner=None):
        pass


if __name__ == '__main__':
    print("Welcome to Blackjack!")
    my_game = Game()
    my_game.player_turn()

    '''
    # initialize the deck function
    my_deck = Deck()
    # calling the deck class, then specifying the shuffle method
    my_deck.shuffle()
    print(my_deck)
    # initializing the player
    player1 = Player()
    print(player1)
    # taking juice from deck object, removing it from deck object
    x = my_deck.draw_cards(2)
    print(x)
    # putting the juice into the players hand
    # x as parameter: communicates between classes
    player1.add_cards_to_player(x)
    player1.view_hand()

    # print(my_deck.cards[0])
    # my_deck.draw_cards(1)
    # print(my_deck.draw_cards(1)[0])
    # print(drawn_cards)
    # calculate()
'''
