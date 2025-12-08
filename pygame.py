from lib2to3.fixes.fix_urllib import build_pattern
import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 15
LINE_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (255, 255, 255)
CIRCLE_COLOR = (242, 85, 96)
X_COLOR = (28, 170, 156)
GRID_SIZE = 3
CELL_SIZE = WIDTH // GRID_SIZE
RADIUS = CELL_SIZE // 4
CIRCLE_WIDTH = 15
X_WIDTH = 25

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Game variables
board = [[None, None, None], [None, None, None], [None, None, None]]
player = "X"  # X starts

# Draw grid
def draw_grid():
    for row in range(1, GRID_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (0, row * CELL_SIZE), (WIDTH, row * CELL_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (row * CELL_SIZE, 0), (row * CELL_SIZE, HEIGHT), LINE_WIDTH)

# Draw X or O on the grid
def draw_marker(row, col, marker):
    x_center = col * CELL_SIZE + CELL_SIZE // 2
    y_center = row * CELL_SIZE + CELL_SIZE // 2

    if marker == "O":
        pygame.draw.circle(
            screen,
            CIRCLE_COLOR,
            (x_center, y_center),
            RADIUS,
            CIRCLE_WIDTH
        )

    elif marker == "X":
        offset = CELL_SIZE // 3
        pygame.draw.line(screen, X_COLOR,
                         (x_center - offset, y_center - offset),
                         (x_center + offset, y_center + offset),
                         CIRCLE_WIDTH)
        pygame.draw.line(screen, X_COLOR,
                         (x_center + offset, y_center - offset),
                         (x_center - offset, y_center + offset),
                         CIRCLE_WIDTH)

# Check for a winner
def check_winner():
    for i in range(GRID_SIZE):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    for row in board:
        if None in row:
            return None

    return "Draw"

# Main game loop
def main():
    global player, board
    game_over = False
    winner = None
    end_time = None

    while True:
        screen.fill(BACKGROUND_COLOR)
        draw_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                row, col = y // CELL_SIZE, x // CELL_SIZE

                if board[row][col] is None:
                    board[row][col] = player
                    player = "O" if player == "X" else "X"
                    winner = check_winner()

                    if winner:
                        game_over = True
                        end_time = pygame.time.get_ticks()

        # Draw all markers
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                if board[r][c] is not None:
                    draw_marker(r, c, board[r][c])

        # Display result and reset after 2 seconds
        if game_over:
            font = pygame.font.Font(None, 36)

            if winner == "Draw":
                text = font.render("It's a Draw!", True, (0, 0, 0))
            else:
                text = font.render(f"Player {winner} Wins!", True, (0, 0, 0))

            screen.blit(text, (WIDTH // 4, HEIGHT // 3))

            # Reset after 2 seconds
            if pygame.time.get_ticks() - end_time > 2000:
                board = [[None, None, None], [None, None, None], [None, None, None]]
                player = "X"
                game_over = False
                winner = None

        pygame.display.update()

# Run the game
if __name__ == "__main__":
    main()
