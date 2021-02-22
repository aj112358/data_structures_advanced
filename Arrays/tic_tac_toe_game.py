"""A quick and easy implementation of Tic-Tac-Toe, taken from book.

Does not implement strategic techniques.

Created By: AJ Singh
Date: Feb 21, 2021
"""


class TicTacToe:
    """Management of a Tic-Tac-Toe game."""

    def __init__(self):
        """Start a new game."""

        self._board = [[" "] * 3 for _ in range(3)]
        self._player = "X"

    def mark(self, i, j):
        """Place an 'X' or 'O' mark at position (i,j) on the board, and switch players."""

        # Check if a player's input is a valid position on the board.
        if not (0 <= i <= 2 or 0 <= j <= 2):
            raise ValueError("Invalid board position.")

        # Check if the board position is free.
        if self._board[i][j] != " ":
            raise ValueError("Board position already occupied.")

        # Check if a winner has been declared.
        if self.winner() is not None:
            raise ValueError("Game is already completed.")

        # Making the X or O mark on the board.
        self._board[i][j] = self._player

        # Switch players.
        if self._player == "X":
            self._player = "O"
        else:
            self._player = "X"

    def _is_win(self, mark):
        """Check whether the current board configuration is a win for a given player.

        @param mark: The player to check for as a winner, either X or O.
        """

        board = self._board  # A local variable for ease of use.

        return (mark == board[0][0] == board[0][1] == board[0][2] or  # row 0
                mark == board[1][0] == board[1][1] == board[1][2] or  # row 1
                mark == board[2][0] == board[2][1] == board[2][2] or  # row 2
                mark == board[0][0] == board[1][0] == board[2][0] or  # column 0
                mark == board[0][1] == board[1][1] == board[2][1] or  # column 1
                mark == board[0][2] == board[1][2] == board[2][2] or  # column 2
                mark == board[0][0] == board[1][1] == board[2][2] or  # diagonal
                mark == board[0][2] == board[1][1] == board[2][0])    # rev diag

    def winner(self):
        """Return mark (X or O) of winning player, or None to indicate either a tie or no winner yet."""

        for mark in "XO":
            if self._is_win(mark):
                return mark
            return None

    def __str__(self):
        """Return string representation of current board."""

        rows = ["|".join(self._board[row]) for row in range(3)]
        return "\n-+-+-\n".join(rows)


if __name__ == "__main__":

    game = TicTacToe()
    print()

    game.mark(1, 1); game.mark(0, 2)
    game.mark(2, 2); game.mark(0, 0)
    game.mark(0, 1); game.mark(2, 0)
    game.mark(2, 1);
    print(game)

    # game.mark(1, 2)
    # game.mark(1, 0)

    print()
    winner = game.winner()
    if winner is None:
        print('Tie')
    else:
        print(winner, 'wins')