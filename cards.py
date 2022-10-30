import random


# class for the rank of the card: 2-10, Jack, King, Queen, Ace
class Rank:
    def __init__(self, rank_value, icon):
        self.rank_value = rank_value
        self.icon = icon


# class for the suit of the card: Spade, Heart, Diamond, Club
class Suit:
    def __init__(self, suit_name):
        self.card_suit = suit_name


# class to make a card using rank and suit
class Card:
    def __init__(self, rank, icon, suit):
        self.rank = rank
        self.icon = icon
        self.suit = suit

    def __str__(self):
        return '{} of {}'.format(self.rank.icon, self.suit.card_suit)


# class for the deck of 52 cards
class Deck:
    card_rank = None
    card_icon = None
    card_suit = None

    def __init__(self):
        self.deck_of_cards = []

        for rank in range(1, 53):
            card_rank = rank

            if rank % 13 == 0:
                card_icon = 'A'
            elif 0 < rank % 13 < 10:
                card_icon = rank + 1
            elif rank == 10:
                card_icon = 'J'
            elif rank == 11:
                card_icon = 'Q'
            elif rank == 12:
                card_icon = 'K'

            if rank < 13:
                card_suit = 'Spades'
            elif 13 <= rank < 26:
                card_suit = 'Hearts'
            elif 26 <= rank < 39:
                card_suit = 'Clubs'
            elif 39 <= rank < 52:
                card_suit = 'Diamonds'

            new_card = Card(card_rank, card_icon, card_suit)
            self.add(new_card)

    # adds card to deck
    def add(self, card):
        self.deck_of_cards.append(card)

    # creates a deck of 52 cards
    def create_deck(self):
        return self.deck_of_cards

    # returns the top card from the deck, each call returns the next card in order
    def get_card(self):
        top_card = self.deck_of_cards[0]
        self.deck_of_cards = self.deck_of_cards[1:]
        return top_card

    # shuffles the current deck, rearranging them in a random order
    def shuffle_deck(self):
        random.shuffle(self.deck_of_cards)


# class to create a hand, accepting various sizes
class Hand:
    def __init__(self, deck_in_play, size):
        self.hand_of_cards = []

        for i in range(0, size + 1):
            new_card = deck_in_play.get_card()
            self.add(new_card)

    # prints the current hand
    def print_hand(self):
        for card in self.hand_of_cards:
            print(card)

    # adds a card to the hand
    def add(self, card):
        self.hand_of_cards.append(card)


deck = Deck
deck.shuffle_deck()
hand = Hand(deck, 5)
hand.print_hand()
