import random


# class for the rank of the card: 2-10, Jack, King, Queen, Ace
class Rank:
    value = None

    def __init__(self, number):
        self.value = number


# class for the suit of the card: Spade, Heart, Diamond, Club
class Suit:
    card_suit = None

    def __init__(self, suit_name):
        self.card_suit = suit_name


# class to make a card using rank and suit
class Card:
    rank = None
    suit = None

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return 'rank: {} of suit: {}'.format(self.rank.value, self.suit.card_suit)


# class for the deck of 52 cards
class Deck:
    card = None

    def __init__(self):
        self.card = []

        for rank in range(0, 52):
            for suit in range(rank, 52):
                card_value = Rank(rank)
                card_suit = Suit(suit)
                new_card = Card(card_value, card_suit)
                self.add(new_card)

    # adds card to deck
    def add(self, card):
        self.card.append(card)

    # creates a deck of 52 cards
    def create_deck(self):
        return self

    # shuffles the current deck, rearranging them in a random order
    def shuffle_deck(self):
        random.shuffle(self)

    # returns the top card from the deck, each call returns the next card in order
    def get_card(self):
        return self.card.pop()


# class to create a hand, accepting various sizes
class Hand:
    card = None

    def __init__(self, size):
        self.card = []

        for i in range(0, size + 1):
            self.add(Deck.get_card())

    # prints the current hand
    def print_hand(self):
        for card in self.card:
            print(card)

    # adds a card to the hand
    def add(self, card):
        self.card.append(card)


deck = Deck.create_deck(self=Deck)
deck.shuffle_deck()
hand = Hand(5)
hand.print_hand()
