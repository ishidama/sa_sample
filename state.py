import random

class State:
    """状態を表すクラス。1次元リストで構成され、各要素は4色の色を持つ。"""

    COLORS = ['red', 'green', 'blue', 'yellow']

    def __init__(self, size, state=None):
        """
        コンストラクタ
        :param size: リストのサイズ
        :param state: 初期状態（省略可能）
        """
        self.size = size
        if state is None:
            self.state = [random.choice(self.COLORS) for _ in range(size)]
        else:
            self.state = state

    def evaluate_energy(self):
        """
        状態のエネルギーを評価する関数
        :return: 状態のエネルギー
        """
        # ここでは、隣接する異なる色のペアの数をエネルギーとする
        energy = 0
        for i in range(len(self.state) - 1):
            if self.state[i] != self.state[i + 1]:
                energy += 100
        return energy

    def neighbor(self):
        """
        隣接する状態を生成する関数
        :return: 隣接する新しい状態
        """
        new_state = self.state[:]
        i, j = random.sample(range(self.size), 2)
        new_state[i], new_state[j] = new_state[j], new_state[i]
        return new_state