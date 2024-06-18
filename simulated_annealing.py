import random
import math

class SimulatedAnnealing:
    """焼きなまし法を実行するクラス"""

    def __init__(self, initial_state, initial_temp, cooling_rate, n_iterations):
        """
        コンストラクタ
        :param initial_state: 初期状態のStateインスタンス
        :param initial_temp: 初期温度
        :param cooling_rate: 冷却率
        :param n_iterations: 繰り返し回数
        """
        self.state = initial_state
        self.initial_temp = initial_temp
        self.cooling_rate = cooling_rate
        self.n_iterations = n_iterations
        self.current_temp = initial_temp
        self.best_state = initial_state
        self.best_energy = self.evaluate_energy(initial_state)

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

    def cool_down(self, temp, iteration):
        """
        温度を低下させる関数
        :param temp: 現在の温度
        :param iteration: 現在の繰り返し回数
        :return: 低下後の温度
        """
        return temp / (1 + self.cooling_rate * iteration)

    def run(self):
        """焼きなまし法を実行する関数"""
        for iteration in range(self.n_iterations):
            new_state = self.neighbor(self.state)
            new_energy = self.evaluate_energy(new_state)
            energy_diff = new_energy - self.best_energy

            if energy_diff < 0 or random.random() < math.exp(-energy_diff / self.current_temp):
                self.state = new_state
                if new_energy < self.best_energy:
                    self.best_state = new_state
                    self.best_energy = new_energy

            self.current_temp = self.cool_down(self.initial_temp, iteration)

        return self.best_state.state, self.best_energy