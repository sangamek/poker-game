# Poker Game

A simple Texas Hold'em poker game implemented in Python.

## Project Structure

```
poker-game
├── src
│   ├── main.py        # Entry point of the poker game
│   ├── deck.py        # Deck class for managing cards
│   ├── player.py      # Player class for managing player actions
│   └── game.py        # Game class for managing game logic
├── requirements.txt    # List of dependencies
└── README.md           # Project documentation
```

## Requirements

- Flask==2.0.1
- numpy==1.21.0
- matplotlib==3.4.2

## How to Run

1. **Clone the repository**:
    ```bash
    git clone <your-repository-url>
    cd poker-game
    ```

2. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the game**:
    ```bash
    python3 src/main.py
    ```

## Game Description

This is a simple implementation of Texas Hold'em poker. Each player is dealt two private cards, and five community cards are dealt in stages. The game determines the winner based on the best hand according to poker hand rankings.

## Game Rules

- Each player is dealt a hand of cards.
- Players take turns to bet, call, raise, or fold.
- The game continues until a winner is determined based on the poker hand rankings.

Enjoy playing poker!