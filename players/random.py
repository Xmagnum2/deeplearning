import random
from players.player import Player


class Random(Player):
    def __init__(self, name: str = "Human"):
        super().__init__(name)

    def play(self, game) -> None:
        while True:
            move = random.choice(game.move_list)
            game.play(move)
            return
