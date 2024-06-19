import matplotlib.pyplot as plt

class InitialStatePlotter:
    """初期状態オブジェクトを描画するクラス"""

    def __init__(self, state):
        """
        コンストラクタ
        :param state: 初期状態のStateインスタンス
        """
        self.state = state
        self.fig, self.ax1 = plt.subplots(figsize=(state.size // 10, 2))
        self.fig.canvas.manager.set_window_title("初期状態")
        self.patches = self.create_patches()
        self.init_plot()
        self.show()

    def create_patches(self):
        """状態を描画するためのパッチを作成する関数"""
        patches = []
        for i in range(self.state.size):
            patch = plt.Rectangle((i, 0), 1, 1, edgecolor='black', facecolor=self.state.state[i])
            patches.append(patch)
            self.ax1.add_patch(patch)
        return patches

    def init_plot(self):
        """描画の初期化関数"""
        self.ax1.set_xlim(0, self.state.size)
        self.ax1.set_ylim(0, 1)
        self.ax1.set_aspect('equal')
        self.ax1.axis('off')

    def show(self):
        """初期状態を表示する関数"""
        plt.ion()  # インタラクティブモードを有効にする
        plt.show()