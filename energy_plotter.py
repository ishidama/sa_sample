import matplotlib.pyplot as plt

class EnergyPlotter:
    """エネルギー履歴を描画するクラス"""

    def __init__(self):
        """コンストラクタ"""
        self.fig, self.ax2 = plt.subplots()
        self.energy_history = []
        self.line, = self.ax2.plot([], [], lw=2)
        self.init_plot()

    def init_plot(self):
        """描画の初期化関数"""
        self.ax2.set_xlim(0, 1)
        self.ax2.set_ylim(0, 1)
        self.ax2.set_title('Energy History')
        self.ax2.set_xlabel('Iteration')
        self.ax2.set_ylabel('Energy')

    def update(self, energy, iteration):
        """エネルギー履歴を更新して描画する関数"""
        self.energy_history.append(energy)
        self.line.set_data(range(len(self.energy_history)), self.energy_history)
        self.ax2.set_xlim(0, len(self.energy_history))
        self.ax2.set_ylim(0, max(self.energy_history) * 1.1)
        plt.draw()