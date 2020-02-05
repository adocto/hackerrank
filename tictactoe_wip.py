# game
# initialize game: >>COMPLETE
#     - set or reset board to empty board
#     - print board

# print board: >>COMPLETE
#     - print status of board

# prompt player for input: >>COMPLETE
#     - set of coordinates
#     - if validate move is true:
#         - set on board (place player marker on spot on board)
#         - decrement moves remaining
#     - else:
#         - notify user
#         - reprompt for move
#

# check win condition: >>COMPLETE
#     - check for win
#     - set appropriate boolean
#     - set winner

# validate move: >>COMPLETE
#     - check if out of bounds of array
#     - check if spot is taken
#     - return true or false


# play game(): >>COMPLETE
#    - while win condition is false or move_rem == 0:
#      - prompt player for input >>COMPLETE
#      - print board >>COMPLETE
#      - check win condition
#      - switch player >>COMPLETE

#    if win condition = true - print self.winner wins!
#    else it's a tie


class Game:

    def __init__(self):
        self.board = [[None] * 3] * 3
        self.player = 0
        self.win = False
        self.moves_remaining = 9
        self.winner = -1

    def resetBoard(self):
        self.board = [[None] * 3] * 3

    def playGame(self):

        # prompt player for turns until someone wins or game is tied
        while (not self.win) and self.moves_remaining > 0:
            self.print_board()
            self.prompt_input()
            self.check_win()
            self.switch_player()

        # check and report winner or tie
        if self.win:
            print("Player %d wins!" % self.winner)
        else:
            print("It's a tie!")

    # switch players after turn
    def switch_player(self):
        if self.player == 0:
            self.player = 1
        else:
            self.player = 0

    def check_win(self):
        # check each row for win condition
        for row in self.board:
            if None not in row:
                if sum(row) == 0:
                    self.winner = 0
                    self.win = True
                    return
                elif sum(row) == 3:
                    self.winner = 1
                    self.win = True
                    return

        # iterating through the rows
        for i in range(len(self.board)):
            col_sum = 0
            # iterating through the columns
            for j in range(len(self.board[i])):
                if self.board[j][i] is not None:
                    col_sum += self.board[j][i]

            # check if players won by column
            if col_sum == 0:
                self.winner = 0
                self.win = True
                return
            elif col_sum == 3:
                self.winner = 1
                self.win = True
                return

        # check for win condition in main diagonal
        diag_sum = 0
        for i in range(len(self.board)):
            # iterate through both rows and columns
            if self.board[i][i] is not None:
                diag_sum += self.board[i][i]
        if diag_sum == 0:
            self.winner = 0
            self.win = True
            return
        elif diag_sum == 3:
            self.winner = 1
            self.win = True
            return

        # check for alternate diagonal
        alt_sum = 0
        for i in range(len(self.board)):
            if self.board[i][len(self.board) - 1 - i] is not None:
                alt_sum += self.board[i][len(self.board) - 1 - i]
        if alt_sum == 0:
            self.winner = 0
            self.win = True
            return
        elif alt_sum == 3:
            self.winner = 1
            self.win = True
            return

    def print_board(self):
        for i in self.board:
            print(", ".join([str(l).rjust(2) for l in i]))

    def prompt_input(self):
        # prompt player for input
        move = input("Player %d enter coordinates for move as tuple (x,y)" % self.player)

        # keep reprompting until move is valid
        while not self.validate_move(move):
            move = input("Player %d enter coordinates for move as tuple (x,y)" % self.player)

        # set move on board
        x, y = move
        self.board[x][y] = self.player
        self.moves_remaining -= 1

    def validate_move(self, move):
        # move is a tuple of x and y coordinates
        valid_input = False  # valid input flag
        empty_space = False  # valid empty space flag
        # are inputs from player within bounds of array?
        while valid_input == False and empty_space == False:
            for int in move:
                if 0 <= int and 2 >= int:
                    valid_input = True
                else:
                    print("You entered an invalid coordinate")
                    return False
            # check if value at tupple index == None:
            if self.board[move[0]][move[1]] == None:
                empty_space = True
            else:
                print("That space is taken")
                return False
        return True
        pass


if __name__ == "__main__":
    game = Game()
    game.playGame()
