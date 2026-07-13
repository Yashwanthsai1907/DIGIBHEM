"""
Tic Tac Toe - two player console game.
"""

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
    (0, 4, 8), (2, 4, 6),              # diagonals
]


def create_board():
    """1. Create a 3x3 grid to represent the Tic Tac Toe board."""
    return [" "] * 9


def display_board(board):
    """2. Display the board to the players."""
    print()
    for row in range(3):
        cells = board[row * 3:row * 3 + 3]
        print(f" {cells[0]} | {cells[1]} | {cells[2]} ")
        if row < 2:
            print("---+---+---")
    print()


def get_move(board, player):
    """Ask the current player for a valid, empty cell (1-9)."""
    while True:
        raw = input(f"Player {player}, choose a cell (1-9): ").strip()
        if not raw.isdigit():
            print("Please enter a number between 1 and 9.")
            continue
        pos = int(raw) - 1
        if pos < 0 or pos > 8:
            print("Please enter a number between 1 and 9.")
            continue
        if board[pos] != " ":
            print("That cell is already taken. Try again.")
            continue
        return pos


def check_winner(board):
    """Return 'X' or 'O' if there's a winner, else None."""
    for a, b, c in WIN_LINES:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_tie(board):
    return " " not in board


def play_round():
    """3 & 4. Run turns, checking for a win or tie after each move."""
    board = create_board()
    current_player = "X"

    display_board(board)

    while True:
        pos = get_move(board, current_player)
        board[pos] = current_player
        display_board(board)

        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins!")
            return winner

        if is_tie(board):
            print("It's a tie!")
            return "tie"

        current_player = "O" if current_player == "X" else "X"


def main():
    scores = {"X": 0, "O": 0, "tie": 0}

    print("Welcome to Tic Tac Toe!")
    print("Cells are numbered 1-9, left to right, top to bottom.")

    while True:
        result = play_round()
        scores[result] += 1

        print(f"Score - X: {scores['X']}  O: {scores['O']}  Ties: {scores['tie']}")

        # 5. Display the result and ask if the players want to play again.
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
