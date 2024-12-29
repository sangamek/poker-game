class Game:
    def __init__(self):
        self.players = []
        self.deck = None
        self.current_round = 0

    def start_game(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.current_round = 1
        self.deal_cards()

    def deal_cards(self):
        for player in self.players:
            player.hand = self.deck.deal(2)

    def next_round(self):
        self.current_round += 1
        # Logic for the next round goes here

    def determine_winner(self):
        # Logic for determining the winner goes here
        pass

    def add_player(self, player):
        self.players.append(player)