from game_manager import GameManager
from games.tic_tac_toe import TicTacToe
from players.human import Human
from players.random import Random
from players.q_learning import QLearning

manager = GameManager(
    TicTacToe(),
    QLearning("先手", file="1"),
    QLearning("後手", file="2"),
    1000000,
)
manager.manage_game()
manager = GameManager(
    TicTacToe(), QLearning("先手", epsilon=0, file="1"), Human("後手"), 1, show_board=True
)
manager.manage_game()
manager = GameManager(
    TicTacToe(), Human("先手"), QLearning("後手", epsilon=0, file="2"), 1, show_board=True
)
manager.manage_game()
