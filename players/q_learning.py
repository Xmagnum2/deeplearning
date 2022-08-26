import json
from pathlib import Path
import random
from games.game import Game, Result
from players.player import Player


class QLearning(Player):
    def __init__(
        self,
        name: str = "QLearning",
        alpha=0.1,
        gamma=0.8,
        epsilon=1,
        file: str = None,
    ):
        super().__init__(name)
        # Qテーブル
        self.q = {}
        # 状態と行動を保持
        self.sa = []
        # 学習率
        self.alpha = alpha
        # 割引率
        self.gamma = gamma
        # epsilon greedy（ランダム行動するかの閾値。学習が進むと減らす。）
        self.epsilon = epsilon

        self.file = file
        self.import_file()

    def play(self, game: Game) -> None:
        # ランダム or Qテーブルから最善手を選択
        move = self.select_move(game)
        # 盤面を進める
        game.play(move)
        return

    def select_move(self, game: Game):
        # dictのkeyにするため文字列変換
        s = str(game.board)
        # 現在の状態が登録されてなければ登録
        if not s in self.q:
            self.q[s] = {str(i): random.random() for i in range(9)}
        # ε-greedy
        if random.random() < self.epsilon or not s in self.q:
            if self.epsilon > 0.2:
                self.epsilon *= 0.99
            move = random.choice(game.move_list)
        else:
            while True:
                # qテーブルから最善手を取得
                move = max(self.q[s], key=self.q[s].get)
                # 最善手が不可能な手なら-1にする
                if int(move) not in game.move_list:
                    self.q[s][move] += -0.1
                else:
                    break
        # 次の学習に向けて状態と行動を保存
        self.sa.append({"s": str(game.board), "a": str(move)})
        return int(move)

    def learn(self, result):
        # Qテーブル更新
        if len(self.sa) > 1:
            match result:
                case Result.PROGRESS:
                    self.update_q(0)
                case Result.DRAW:
                    self.update_q(0)
                case Result.WIN:
                    self.update_q(1)
                case Result.LOSS:
                    self.update_q(-1)

    def update_q(self, reward):
        self.q[self.sa[-2]["s"]][self.sa[-2]["a"]] = self.alpha * (
            reward
            + self.gamma * self.q[self.sa[-1]["s"]][self.sa[-1]["a"]]
            - self.q[self.sa[-2]["s"]][self.sa[-2]["a"]]
        )

    def reset(self):
        self.pre_s = ""
        self.s = ""

    def export_file(self):
        if self.file != None:
            with open(
                f"{Path(__file__).resolve().parent}/trail_data/{self.file}.json", "w"
            ) as f:
                json.dump(self.q, f, ensure_ascii=False)

    def import_file(self):
        if self.file != None:
            try:
                with open(
                    f"{Path(__file__).resolve().parent}/trail_data/{self.file}.json",
                    "r",
                ) as f:
                    self.q = json.load(f)
            except Exception:
                pass
