from games.game import Game
import abc
import random
import sys

sys.path.append("../")


class Player(metaclass=abc.ABCMeta):
    def __init__(self, name: str):
        self.name = name

    @abc.abstractmethod
    def play(self, game: Game) -> None:
        raise NotImplementedError


class Human(Player):
    def __init__(self, name: str = "Human"):
        super().__init__(name)

    def play(self, game) -> None:
        while True:
            move = input("位置：")
            if move.isnumeric() and int(move) in game.move_list:
                game.play(move)
                return


class Random(Player):
    def __init__(self, name: str = "Human"):
        super().__init__(name)

    def play(self, game) -> None:
        while True:
            move = random.choice(game.move_list)
            game.play(move)
            return
