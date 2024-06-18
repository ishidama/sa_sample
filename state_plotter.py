import matplotlib.pyplot as plt

class StatePlotter:
    """状態オブジェクトを描画するクラス"""

    def __init__(self, state):
        """
        コンストラクタ
        :param state: 初期状態のStateインスタンス
        """
        self.state = state
        self.fig, self.ax = plt.subplots(figsize=(state.size // 10, 2))
        self.patches = self.create_patches()
        self.init_plot()

    def create_patches(self):
        """状態を描画するためのパッチを作成する関数"""
        patches = []
        for i in range(self.state.size):
            patch = plt.Rectangle((i, 0), 1, 1, edgecolor='black', facecolor=self.state.state[i])
            patches.append(patch)
            self.ax.add_patch(patch)
        return patches

    def init_plot(self):
        """描画の初期化関数"""
        self.ax.set_xlim(0, self.state.size)
        self.ax.set_ylim(0, 1)
        self.ax.set_aspect('equal')
        self.ax.axis('off')

    def update(self, state):
        """状態を更新して描画する関数"""
        self.state = state
        for i, patch in enumerate(self.patches):
            patch.set_facecolor(state.state[i])
        plt.draw()