import random

class Rank:
    value = None

    def __init__(self, number):
        self.value = number


class Suit:
    card_suit = None

    def __init__(self, suit_name):
        self.card_suit = suit_name


class Card:
    rank = None
    suit = None

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return 'rank: {} of suit: {}'.format(self.rank.value, self.suit.card_suit)


class Hand:
    card = None

    def __init__(self, size):
        self.card = []

        for rank in range(0, size + 1):
            for suit in range(rank, size + 1):
                card_value =
                card_suit =
                new_card = Card(card_value, card_suit)
                self.add(new_card)

