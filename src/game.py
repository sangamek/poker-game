from deck import Deck
from player import Player
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
from collections import Counter
from itertools import combinations

class PokerGame:
    def __init__(self):
        self.deck = Deck()
        self.players = [Player("Player 1"), Player("Player 2")]
        self.community_cards = []

    def start(self):
        # Deal two private cards to each player
        for _ in range(2):
            for player in self.players:
                player.receive_card(self.deck.deal())

        # Deal five community cards
        self.deal_community_cards()

        for player in self.players:
            print(f"{player.name} has {player.show_hand()}")

        print(f"Community cards: {self.community_cards}")

        self.determine_winner()

    def deal_community_cards(self):
        # Deal three cards (the flop)
        self.community_cards.extend([self.deck.deal() for _ in range(3)])
        # Deal one card (the turn)
        self.community_cards.append(self.deck.deal())
        # Deal one card (the river)
        self.community_cards.append(self.deck.deal())

    def determine_winner(self):
        def hand_rank(hand):
            ranks = '23456789TJQKA'
            rank_dict = {r: i for i, r in enumerate(ranks, start=2)}
            rank_dict['10'] = 10  # Handle '10' correctly
            rank_name_dict = {r: name for r, name in zip(ranks, ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'])}
            rank_name_dict['10'] = '10'  # Handle '10' correctly
            hand = sorted(hand, key=lambda card: rank_dict[card[0]], reverse=True)
            counts = Counter(card[0] for card in hand)
            counts = sorted(counts.items(), key=lambda x: (x[1], rank_dict[x[0]]), reverse=True)
            is_flush = len(set(card[1] for card in hand)) == 1
            is_straight = len(counts) == 5 and rank_dict[counts[0][0]] - rank_dict[counts[-1][0]] == 4
            if is_straight and is_flush:
                return (8, rank_dict[counts[0][0]], "Straight flush")  # Straight flush
            if counts[0][1] == 4:
                return (7, rank_dict[counts[0][0]], rank_dict[counts[1][0]], f"Four of a kind of {rank_name_dict[counts[0][0]]}")  # Four of a kind
            if counts[0][1] == 3 and counts[1][1] == 2:
                return (6, rank_dict[counts[0][0]], rank_dict[counts[1][0]], f"Full house with {rank_name_dict[counts[0][0]]} over {rank_name_dict[counts[1][0]]}")  # Full house
            if is_flush:
                return (5, [rank_dict[card[0]] for card in hand], "Flush")  # Flush
            if is_straight:
                return (4, rank_dict[counts[0][0]], "Straight")  # Straight
            if counts[0][1] == 3:
                return (3, rank_dict[counts[0][0]], [rank_dict[card[0]] for card in hand if card[0] != counts[0][0]], f"Three of a kind of {rank_name_dict[counts[0][0]]}")  # Three of a kind
            if counts[0][1] == 2 and counts[1][1] == 2:
                return (2, rank_dict[counts[0][0]], rank_dict[counts[1][0]], f"Two pair with {rank_name_dict[counts[0][0]]} and {rank_name_dict[counts[1][0]]}")  # Two pair
            if counts[0][1] == 2:
                return (1, rank_dict[counts[0][0]], [rank_dict[card[0]] for card in hand if card[0] != counts[0][0]], f"One pair of {rank_name_dict[counts[0][0]]}")  # One pair
            return (0, [rank_dict[card[0]] for card in hand], f"High card {rank_name_dict[counts[0][0]]}")  # High card

        def best_hand(player):
            all_cards = player.hand + self.community_cards
            all_combinations = list(combinations(all_cards, 5))
            return max(all_combinations, key=hand_rank)

        player1_best = best_hand(self.players[0])
        player2_best = best_hand(self.players[1])

        player1_rank = hand_rank(player1_best)
        player2_rank = hand_rank(player2_best)

        if player1_rank > player2_rank:
            winner = self.players[0]
            winning_hand = player1_best
            winning_hand_description = f"{self.players[0].name} wins with {player1_rank[2]}"
            print(winning_hand_description)
        elif player2_rank > player1_rank:
            winner = self.players[1]
            winning_hand = player2_best
            winning_hand_description = f"{self.players[1].name} wins with {player2_rank[2]}"
            print(winning_hand_description)
        else:
            winner = None
            winning_hand = None
            winning_hand_description = "It's a tie!"
            print(winning_hand_description)

        self.visualize_cards(winner, winning_hand, winning_hand_description)

    def visualize_cards(self, winner, winning_hand, winning_hand_description):
        fig, ax = plt.subplots(3, 5, figsize=(15, 9))
        card_dir = os.path.join(os.path.dirname(__file__), 'cards')
        placeholder_path = os.path.join(card_dir, 'placeholder.png')

        for i, player in enumerate(self.players):
            for j, card in enumerate(player.hand):
                card_filename = f"{card[0]}_of_{card[1].lower()}.png"
                if card[0] == 'Joker':
                    card_filename = f"{card[1].lower()}_joker.png"
                card_path = os.path.join(card_dir, card_filename)
                if os.path.exists(card_path):
                    img = mpimg.imread(card_path)
                else:
                    img = mpimg.imread(placeholder_path)
                ax[i, j].imshow(img)
                ax[i, j].axis('off')
                if winning_hand and card in winning_hand:
                    ax[i, j].set_title('Winner', color='red')

        for j, card in enumerate(self.community_cards):
            card_filename = f"{card[0]}_of_{card[1].lower()}.png"
            if card[0] == 'Joker':
                card_filename = f"{card[1].lower()}_joker.png"
            card_path = os.path.join(card_dir, card_filename)
            if os.path.exists(card_path):
                img = mpimg.imread(card_path)
            else:
                img = mpimg.imread(placeholder_path)
            ax[2, j].imshow(img)
            ax[2, j].axis('off')
            if winning_hand and card in winning_hand:
                ax[2, j].set_title('Winner', color='red')

        # Remove empty subplots
        for i in range(2):
            for j in range(len(self.players[i].hand), 5):
                fig.delaxes(ax[i, j])

        plt.suptitle(winning_hand_description)
        plt.show()