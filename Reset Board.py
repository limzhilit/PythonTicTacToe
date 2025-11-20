while True:
    board = reset_board()
    current_player = "X"

    # main game logic
    for move in range(9):
        print_board(board)
        play_turn(board, current_player)

        if winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        current_player = switch_player(current_player)
    else:
        print_board(board)
        print("It's a draw!")

    # Automatic reset message
    print("\n--- Resetting board for a new game! ---\n")