from game_manager import GameManager
from games.tic_tac_toe import TicTacToe
from players.player import *


manager = GameManager(TicTacToe(), Human("先手"), Random("後手"), 10)
manager.manage_game()
