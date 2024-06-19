from example_annealing import ExampleAnnealing
from state import State
from state_plotter import StatePlotter
from energy_plotter import EnergyPlotter
from initial_state_plotter import InitialStatePlotter
import matplotlib.pyplot as plt

# インタラクティブモードを有効にする
plt.ion()

# 初期状態としてStateインスタンスを生成
initial_state = State(size=100)  # サイズを100に設定
initial_state_plotter = InitialStatePlotter(initial_state)
state_plotter = StatePlotter(initial_state)
energy_plotter = EnergyPlotter()

def on_step(state, iteration, best_energy):
    """シミュレーションのステップごとに呼ばれるコールバック関数"""
    state_plotter.update(state)
    energy_plotter.update(best_energy, iteration)
    plt.pause(0.01)

# 焼きなまし法の実行
sa = ExampleAnnealing(initial_state, initial_temp=10000.0, cooling_rate=0.9, n_iterations=1000, on_step=on_step)
best_state, best_energy = sa.run()

print("Initial State:", initial_state.state)
print("Best State:", best_state)
print("Best Energy:", best_energy)
plt.ioff()  # インタラクティブモードをオフにする
plt.show()  # 最後に全てのプロットを表示