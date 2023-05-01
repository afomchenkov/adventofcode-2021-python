from collections import namedtuple
from random import choice

Card = namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        self._cards = [Card(rank, suit)
                       for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        print(f"slice() -> {position}")
        return self._cards[position]

def spades_high(card):
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

if __name__ == "__main__":
    deck = FrenchDeck()

    # for card in reversed(deck):
    for card in deck:
        print(card)

    print("-------")

    print(len(deck))
    print(deck[0])
    print(choice(deck))
    print(deck[:3:1])

    for card in sorted(deck, key=spades_high):
        print(card)

    """
        for i in x:
            calls iter(x) -> then
                x.__iter__()
                OR
                x.__getitem__()
    """