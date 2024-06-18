import random
from simulated_annealing import SimulatedAnnealing

class ExampleAnnealing(SimulatedAnnealing):
    """焼きなまし法の具体例として、リストの要素の合計を最小化するクラス"""

    def evaluate_energy(self, state):
        """
        状態のエネルギーを評価する関数
        :param state: 評価する状態
        :return: 状態のエネルギー
        """
        # ここでは、リストの要素の合計がエネルギーとなる
        return sum(state)

    def neighbor(self, state):
        """
        隣接する状態を生成する関数
        :param state: 現在の状態
        :return: 隣接する新しい状態
        """
        # リストの2つの要素をランダムに入れ替える
        new_state = state[:]
        i, j = random.sample(range(len(state)), 2)
        new_state[i], new_state[j] = new_state[j], new_state[i]
        return new_state