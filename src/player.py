class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.chips = 100  # Starting chips for the player

    def bet(self, amount):
        if amount > self.chips:
            raise ValueError("Insufficient chips to make this bet.")
        self.chips -= amount
        return amount

    def receive_card(self, card):
        self.hand.append(card)

    def show_hand(self):
        return self.hand

    def clear_hand(self):
        self.hand = []