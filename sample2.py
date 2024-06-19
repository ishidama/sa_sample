import matplotlib.pyplot as plt
import numpy as np
import random
import matplotlib.animation as animation

# 円の数を設定
num_circles = 100

# 使用する色のリストを定義
colors = ['red', 'green', 'blue', 'yellow']

# 系のエネルギーを評価する関数を定義


def evaluate_energy(state):
    energy = 0
    for i in range(len(state) - 1):
        if state[i] != state[i + 1]:
            energy += 1
    return energy


# 隣接する色をランダムに交換する関数を定義
def neighbor(state):
    new_state = state[:]
    i, j = random.sample(range(len(state)), 2)
    new_state[i], new_state[j] = new_state[j], new_state[i]
    return new_state


# 初期状態をランダムに生成
state = [random.choice(colors) for _ in range(num_circles)]
current_energy = evaluate_energy(state)
best_state = state[:]
best_energy = current_energy

# パラメータ設定
n_iterations = 100000
initial_temp = 10.0
cooling_rate = 0.003

# アニメーション用の設定
fig, ax = plt.subplots(figsize=(20, 2))

# 円を描画
patches = []
for i in range(num_circles):
    circle = plt.Circle((i * 2, 0), 1, edgecolor='black', facecolor=state[i])
    ax.add_patch(circle)
    patches.append(circle)


def init():
    ax.set_xlim(-1, num_circles * 2)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.grid(False)
    ax.axis('off')
    return patches


def update(frame):
    global state, current_energy, best_state, best_energy

    t = initial_temp / (1 + cooling_rate * frame)
    new_state = neighbor(state)
    new_energy = evaluate_energy(new_state)

    if new_energy < current_energy or random.random() < np.exp((current_energy - new_energy) / t):
        state = new_state
        current_energy = new_energy

        if new_energy < best_energy:
            best_state = new_state
            best_energy = new_energy

    for i, circle in enumerate(patches):
        circle.set_facecolor(state[i])

    return patches


ani = animation.FuncAnimation(
    fig, update, frames=n_iterations, init_func=init, blit=True, repeat=False, interval=1)

plt.show()

print(f"Best Energy: {best_energy}")
