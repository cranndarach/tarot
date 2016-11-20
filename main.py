#!/usr/bin/env python3

import pyCardDeck


class TarotDeck:
    def __init__(self, **kwargs):
        # super().__init__()

        self.suits = kwargs.get("suits", ["Cups", "Wands", "Swords", "Pentacles"])
        #kwargs["suits"] if kwargs["suits"] else ["Cups", "Wands",
            #"Swords", "Pentacles"]
        self.values = kwargs.get("values", ["Ace"]+[str(x) for x in range(2, 11)]
            +["Page","Knight","Queen","King"])
            #kwargs["values"] if kwargs["values"] else ["Ace"]+[str(x) for x in range(2, 11)]+["Page","Knight","Queen","King"]
        self.cards = []
        for suit in self.suits:
            for value in self.values:
                self.cards.append("{} of {}".format(value, suit))
        self.deck = pyCardDeck.Deck(cards=self.cards, reshuffle=False)


if __name__ == "__main__":
    my_deck = TarotDeck()
    print(my_deck.cards)
