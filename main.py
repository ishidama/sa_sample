import random
from example_annealing import ExampleAnnealing

# 使用例
initial_state = [random.randint(0, 10) for _ in range(10)]  # 初期状態をランダムに生成
sa = ExampleAnnealing(initial_state, initial_temp=10000.0, cooling_rate=0.9, n_iterations=1000)
best_state, best_energy = sa.run()

print("Initial State:", initial_state)
print("Best State:", best_state)
print("Best Energy:", best_energy)