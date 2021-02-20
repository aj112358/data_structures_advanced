"""A class to score high scores for a game, taken from book.

Created By: AJ Singh
Date: Feb 20, 2021
"""


class GameEntry:
    """Represents one entry of a list of high scores."""

    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return "({0}, {1})".format(self._name, self._score)


class Scoreboard:
    """Fixed-length sequence of high scores in non-decreasing order."""

    def __init__(self, capacity=10):
        """Initialize a scoreboard with a given capacity.

        All entries are initially 'None'.
        """

        self._board = [None] * capacity
        self._n = 0  # Number of actual entries.

    def __getitem__(self, k):
        """Return the high score entry at index k."""
        return self._board[k]

    def __str__(self):
        """Return (human readable) string representation of the high score list.

        Each high score will be displayed on a new line.
        """
        return "\n".join(str(self._board[j]) for j in range(self._n))

    def add(self, entry):
        """Checks if a new score should be entered, and enters it if so.

        @param entry: An instance of the GameEntry class.
        """

        new_score = entry.get_score()

        # check1 = self._n < len(self._board)
        # check2 = score > self._board[-1].get_score()
        #
        # if check1 or check2:

        # MUST do short-circuiting, otherwise you get a TypeError (comparing NoneType with int).
        # You cannot split these two checks like I tried to do above!
        # Checks first for room on the score board, then (if needed) checks if the new score is higher than current lowest.
        if self._n < len(self._board) or new_score > self._board[-1].get_score():

            if self._n < len(self._board):  # Increment number of entries if needed.
                self._n += 1

            j = self._n - 1
            # This loop also implements short-circuiting.
            # With the FIRST GameEntry added to the Scoreboard, j = 1-1 = 0, hence the loop won't execute.
            # For later entries, the second argument of the and-statement will not raise a TypeError anymore!
            while j > 0 and self._board[j-1].get_score() < new_score:
                self._board[j] = self._board[j-1]
                j -= 1

            self._board[j] = entry


if __name__ == "__main__":

    scores = Scoreboard(10)
    print(scores)

    alice = GameEntry("Alice", 100)
    bob = GameEntry("Bob", 90)
    carli = GameEntry("Carli", 80)
    # print(carli)

    scores.add(alice)
    scores.add(bob)
    scores.add(carli)
    print(scores)

    david = GameEntry("David", 85)
    scores.add(david)
    print(scores)
