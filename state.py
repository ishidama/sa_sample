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

    # def evaluate_energy(self):
    #     """
    #     状態のエネルギーを評価する関数
    #     :return: 状態のエネルギー
    #     """
    #     # ここでは、隣接する異なる色のペアの数をエネルギーとする
    #     energy = 0
    #     for i in range(len(self.state) - 1):
    #         if self.state[i] != self.state[i + 1]:
    #             energy += 100
    #     return energy

    def evaluate_energy(self):
        """
        状態のエネルギーを評価する関数
        :return: 状態のエネルギー
        """
        energy = 0
        for i in range(len(self.state)):
            for j in range(i + 1, len(self.state)):
                if self.state[i] != self.state[j]:
                    distance = abs(i - j)
                    energy += 100 / (distance ** 2)  # 距離の逆二乗に比例するエネルギー
        return energy

    def neighbor(self):
        """
        隣接する状態を生成する関数
        :return: 隣接する新しい状態
        """
        new_state = self.state[:]
        i, j = random.sample(range(self.size), 2)
        old_energy = self.evaluate_energy()
        new_state[i], new_state[j] = new_state[j], new_state[i]
        new_energy = self.evaluate_energy()

        # コンソールに情報を出力
        print(f"Swapped indices {i} ({self.state[i]}) and {j} ({self.state[j]})")
        print(f"Old energy: {old_energy}, New energy: {new_energy}")

        return new_state