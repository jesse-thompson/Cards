from behave import *
import cards

# TODO: make all tests


@Given('I have created a new deck object')
def step_impl(context):
    pass


@When('I create the new class')
def step_impl(context):
    new_deck = cards.Deck
    assert new_deck is not None
    context.card_holder = new_deck
    assert context.new_deck.deck_of_cards.__len__() == 52


@Then('the card value should be recorded')
def step_impl(context):
    assert context.card_holder.count == context.num_of_cards


@Given('I have a set number of cards')
def step_impl(context):
    context.card_deck = cards.Deck
    assert context.card_deck is not None


@When('I draw a card')
def step_impl(context):
    context.num_of_cards = context.new_deck.deck_of_cards.__len__()
    context.drawn_card = context.new_deck.get_card()
    assert context.drawn_card is not None


@Then('it is removed from the deck')
def step_impl(context):
    assert context.new_deck.deck_of_cards.__len__() < context.num_of_cards
    assert context.drawn_card not in context.new_deck.deck_of_cards

# @Given('I have a deck of cards')
# def step_impl(context):
#
#
# @When('I shuffle them')
# def step_impl(context):
#
#
# @Then('The order has changed')
# def step_impl(context):
#
