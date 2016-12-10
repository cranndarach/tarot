#!/usr/bin/env python3

import sys
import pyCardDeck


class TarotDeck:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name", "My Tarot Deck")
        self.suits = kwargs.get("suits", ["Cups", "Wands", "Swords",
                                          "Pentacles"])
        self.values = kwargs.get("values", ["Ace"] + [str(x) for x in
                                                      range(2, 11)] +
                                 ["Page", "Knight", "Queen", "King"])
        self.cards = []
        for suit in self.suits:
            for value in self.values:
                self.cards.append("{} of {}".format(value, suit))
        self.deck = pyCardDeck.Deck(cards=self.cards, name=self.name,
                                    reshuffle=False)


class Reading:
    celtic_cross = ["The current situation", "The challenge",
                    "The recent past", "The near future", "Subconscious\
                    influences", "Hopes and goals", "What you contribute",
                    "What your environment contributes", "What you need\
                    to know", "Possible outcome of the current path"]
    ppf          = ["Past", "Present", "Future"]
    tree_spread  = ["Roots: You at present", "Knot: The current challenge",
                    "Trunk: How do you grow and shape your path?",
                    "Wind: How does the environment influence your situation?"
                    "Limbs: Past influences on the present", "Branches: Your\
                    fears", "Leaves: Your hopes", "Fruit: Possible outcome\
                    of the current path"]

    def __init__(self, deck):
        self.deck = deck

    def read(self):
        self.kind = str(input("""What kind of reading?
        a - Past, Present, Future (3 cards)
        b - Celtic Cross (10 cards)
        c - Tree Spread (8 cards)
        d - Custom (you decide how many cards)
        :\s
        """))

        self.topic = str(input("What is your question or topic? "))
        self.get_draw_number()
        self.get_shuffle_number()
        self.shuffle_n()
        print()
        print("Let's begin.")
        print('The topic is:\t\t\t"{}"'.format(self.topic))
        self.pull_n()
        self.check_if_satisfied()

    def check_if_satisfied(self):
        update = input("Enter [d] to draw more cards, or anything else to end the reading: ")
        if update == "d":
            self.get_draw_number()
            self.pull_n()
            self.check_if_satisfied()
        else:
            print("Have a nice day!")
            sys.exit(0)

    def get_draw_number(self):
        while True:
            try:
                self.how_many = int(input("How many cards will you draw? "))
                break
            except ValueError:
                print("Please input a whole number.")

    def get_ready(self):
        ready = input("Ready? [y|N] ")
        while True:
            if ready.lower() == "y" or ready.lower() == "yes":
                break
            else:
                ready = input('Let me know when you are ready by entering "yes" or "y". ')

    def get_shuffle_number(self):
        while True:
            try:
                self.shuffle_times = int(input("Shuffle how many times? "))
                break
            except ValueError:
                print("Please input a whole number.")

    def pull_n(self):
        card_num = 1
        while card_num <= self.how_many:
            input("Draw card #{}:".format(card_num))
            my_card = self.deck.draw()
            print("\tPulled {}".format(my_card))
            card_num += 1

    def shuffle_n(self):
        shuffled = 0
        while shuffled < self.shuffle_times:
            self.deck.shuffle()
            shuffled += 1
            print(str(shuffled), end="...")
        print()
        print("Shuffled {} times.".format(shuffled))

if __name__ == "__main__":
    my_deck = TarotDeck()
    my_reading = Reading(my_deck.deck)
    my_reading.read()
