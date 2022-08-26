from players.player import Player


class Human(Player):
    def __init__(self, name: str = "Human"):
        super().__init__(name)

    def play(self, game) -> None:
        game.print_board()
        while True:
            move = input("位置：")
            if move.isnumeric() and int(move) in game.move_list:
                game.play(int(move))
                return
