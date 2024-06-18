from simulated_annealing import SimulatedAnnealing
from state import State

class ExampleAnnealing(SimulatedAnnealing):
    """焼きなまし法の具体例として、状態クラスを使用するクラス"""

    def evaluate_energy(self, state):
        """
        状態のエネルギーを評価する関数
        :param state: 評価する状態
        :return: 状態のエネルギー
        """
        return state.evaluate_energy()

    def neighbor(self, state):
        """
        隣接する状態を生成する関数
        :param state: 現在の状態
        :return: 隣接する新しい状態
        """
        new_state_values = state.neighbor()
        return State(state.size, new_state_values)