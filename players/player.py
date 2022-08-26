from games.game import Game
import abc
import sys

sys.path.append("../")


class Player(metaclass=abc.ABCMeta):
    def __init__(self, name: str):
        self.name = name

    @abc.abstractmethod
    def play(self, game: Game) -> None:
        raise NotImplementedError

    def reset(self) -> None:
        pass

    def learn(self, result) -> None:
        pass

    def export_file(self):
        pass

    def import_file(self):
        pass
