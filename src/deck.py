class Deck:
    def __init__(self):
        self.cards = self.create_deck()
        self.shuffle()

    def create_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        return [(rank, suit) for suit in suits for rank in ranks]

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, num_cards):
        dealt_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return dealt_cards

    def remaining_cards(self):
        return len(self.cards)