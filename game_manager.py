from games.game import Game, Result
from players.player import Player


class GameManager:
    def __init__(
        self,
        game: Game,
        first_player: Player,
        second_player: Player,
        iteration: int = 1,
        show_board=False,
    ) -> None:
        self.game = game
        self.first_player = first_player
        self.second_player = second_player
        self.first_player_win_count = 0
        self.second_player_win_count = 0
        self.draw_count = 0
        self.iteration = iteration
        self.step = 0
        self.show_board = show_board

    def manage_game(self):
        while self.iteration != self.step:
            self.progression_game()
            self.setup_game()
        self.result()

    def setup_game(self):
        self.game.reset()

    def progression_game(self):
        while self.game.result == Result.PROGRESS:
            if not self.game.turn % 2:
                self.first_player.play(self.game)
            else:
                self.second_player.play(self.game)
            if self.show_board:
                self.game.print_board()
        match self.game.result:
            case Result.DRAW:
                self.draw_count += 1
            case Result.FIRST:
                self.first_player_win_count += 1
            case Result.SECOND:
                self.second_player_win_count += 1
        self.step += 1

    def result(self):
        print("--------------------------------------")
        print(f"{self.first_player.name}: {self.first_player_win_count}")
        print(f"{self.second_player.name}: {self.second_player_win_count}")
        print(f"draw: {self.draw_count}")
