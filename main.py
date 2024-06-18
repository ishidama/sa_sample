from example_annealing import ExampleAnnealing
from state import State

# 初期状態としてStateインスタンスを生成
initial_state = State(size=100)

# 焼きなまし法の実行
sa = ExampleAnnealing(initial_state, initial_temp=10000.0, cooling_rate=0.9, n_iterations=1000)
best_state, best_energy = sa.run()

print("Initial State:", initial_state.state)
print("Best State:", best_state)
print("Best Energy:", best_energy)