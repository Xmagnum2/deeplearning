import abc
from enum import Enum, auto


class Result(Enum):
    PROGRESS = auto()
    FIRST = auto()
    SECOND = auto()
    DRAW = auto()
    WIN = auto()
    LOSS = auto()


class Game(metaclass=abc.ABCMeta):
    def __init__(self):
        self.board: list
        self.turn: int
        self.move_list: list
        self.result: Result

    @abc.abstractmethod
    def print_board(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def play() -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def check_end() -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def reset(self) -> None:
        raise NotImplementedError
