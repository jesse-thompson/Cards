import random

ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']


# class to make a card using rank and suit
class Card:
    def __init__(self, rank, icon, suit):
        self.rank = rank
        self.icon = icon
        self.suit = suit

    def __str__(self):
        return '{} of {}'.format(self.icon, self.suit)


# class for the deck of 52 cards
class Deck:
    card_rank = None
    card_icon = None
    card_suit = None

    def __init__(self):
        self.deck_of_cards = []

        for card_suit in suits:
            for card_rank in ranks:

                match card_rank:
                    case 11:
                        card_icon = 'Jack'
                    case 12:
                        card_icon = 'Queen'
                    case 13:
                        card_icon = 'King'
                    case 14:
                        card_icon = 'Ace'
                    case _:
                        card_icon = card_rank

                new_card = Card(card_rank, card_icon, card_suit)
                self.add(new_card)

    # adds card to deck
    def add(self, card):
        self.deck_of_cards.append(card)

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

        for i in range(0, size):
            new_card = deck_in_play.get_card()
            self.add(new_card)

    # prints the current hand
    def print_hand(self):
        for card in self.hand_of_cards:
            print(card)

    # adds a card to the hand
    def add(self, card):
        self.hand_of_cards.append(card)


deck = Deck()
deck.shuffle_deck()
hand = Hand(deck, 5)
hand.print_hand()
