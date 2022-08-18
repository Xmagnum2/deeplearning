from .game import Game, Result


class TicTacToe(Game):
    def __init__(self):
        self.board: list = ["-" for i in range(9)]
        self.turn: int = 0
        self.move_list: list = list(range(len(self.board)))
        self.result: Result = Result.PROGRESS

    def print_board(self) -> None:
        print(f"turn: {self.turn}")
        for i in range(0, len(self.board), 3):
            print(self.board[i], self.board[i + 1], self.board[i + 2])

    def play(self, pos: int) -> None:
        self.board[pos] = "X" if self.turn % 2 else "O"
        self.update_move_list()
        if self.check_end():
            if not self.move_list:
                self.result = Result.DRAW
            elif self.turn % 2:
                self.result = Result.SECOND
            else:
                self.result = Result.FIRST
        else:
            self.turn += 1

    def check_end(self) -> bool:
        if self.board[0] == self.board[1] == self.board[2] != "-":
            return True
        elif self.board[3] == self.board[4] == self.board[5] != "-":
            return True
        elif self.board[6] == self.board[7] == self.board[8] != "-":
            return True
        elif self.board[0] == self.board[3] == self.board[6] != "-":
            return True
        elif self.board[1] == self.board[4] == self.board[7] != "-":
            return True
        elif self.board[2] == self.board[5] == self.board[8] != "-":
            return True
        elif self.board[0] == self.board[4] == self.board[8] != "-":
            return True
        elif self.board[2] == self.board[4] == self.board[6] != "-":
            return True
        else:
            return not self.move_list

    def update_move_list(self):
        temp = list(range(len(self.board)))
        self.move_list = list(filter(lambda x: self.board[x] == "-", temp))

    def reset(self) -> None:
        self.__init__()
