player_wins = 0
computer_wins = 0
rounds = 0

while rounds < 3 and player_wins < 2 and computer_wins < 2:
    winner = game_play()  #one full tictactoe game, returns player, computer, or tie
    rounds += 1

    if winner == "player":
        player_wins += 1
    elif winner == "computer":
        computer_wins += 1

        print(f"Score Tallied: You: {player_wins} - Computer: {computer_wins}")

        #after loop, this decides the winner

        if player_wins > computer_wins:
            print("You won the best of 3!")
        elif computer_wins > player_wins:
            print("Computer won the best of 3!")
        else:
            print("The best of 3 ended in a draw")