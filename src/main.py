def main():
    print("Welcome to the Poker Game!")
    
    # Initialize game and players
    game = Game()
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    
    game.add_player(player1)
    game.add_player(player2)
    
    # Start the game loop
    while True:
        game.start_round()
        if game.is_game_over():
            break
    
    print("Game Over! Thanks for playing.")

if __name__ == "__main__":
    main()