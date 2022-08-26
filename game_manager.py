from games.game import Game, Result
from players.player import Player
import matplotlib.pyplot as plt


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

        # 戦績表示用パラメータ
        self.record = []
        self.record_iteration = 100
        self.win_count = 0

        # 表示オプション
        self.show_board = show_board

    def manage_game(self):
        while self.iteration != self.step:
            self.progression_game()
            self.win_count += 1 if self.game.result == Result.FIRST else 0
            self.win_count += 1 if self.game.result == Result.DRAW else 0
            self.setup_game()
            # 50戦ごとに勝率を計算してレコードに格納
            if self.step != 0 and (not self.step % self.record_iteration):
                self.record.append(self.win_count)
                self.win_count = 0
        self.first_player.export_file()
        self.second_player.export_file()
        self.result()

    def setup_game(self):
        self.game.reset()
        self.first_player.reset()
        self.second_player.reset()

    def progression_game(self):
        while self.game.result == Result.PROGRESS:
            if not self.game.turn % 2:
                self.first_player.play(self.game)
                self.first_player.learn(Result.PROGRESS)
            else:
                self.second_player.play(self.game)
                self.second_player.learn(Result.PROGRESS)
            if self.show_board:
                self.game.print_board()
        match self.game.result:
            case Result.DRAW:
                self.draw_count += 1
                self.first_player.learn(Result.DRAW)
                self.second_player.learn(Result.DRAW)
            case Result.FIRST:
                self.first_player_win_count += 1
                self.first_player.learn(Result.WIN)
                self.second_player.learn(Result.LOSS)
            case Result.SECOND:
                self.second_player_win_count += 1
                self.first_player.learn(Result.LOSS)
                self.second_player.learn(Result.WIN)
        self.step += 1

    def result(self):
        self.draw_record()
        print("--------------------------------------")
        print(f"{self.first_player.name}: {self.first_player_win_count}")
        print(f"{self.second_player.name}: {self.second_player_win_count}")
        print(f"draw: {self.draw_count}")

    def draw_record(self):
        plt.plot(self.record)
        plt.show()
