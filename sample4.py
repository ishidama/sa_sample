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
            energy += 100
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
energy_history = [current_energy]

# パラメータ設定
n_iterations = 10000
initial_temp = 10000.0
cooling_rate = 0.9

# アニメーション用の設定
fig1, ax1 = plt.subplots(figsize=(20, 2))
fig2, ax2 = plt.subplots()

# 円を描画
patches = []
for i in range(num_circles):
    circle = plt.Circle((i * 2, 0), 1, edgecolor='black', facecolor=state[i])
    ax1.add_patch(circle)
    patches.append(circle)

line, = ax2.plot([], [], lw=2)


def init():
    ax1.set_xlim(-1, num_circles * 2)
    ax1.set_ylim(-1.5, 1.5)
    ax1.set_aspect('equal')
    ax1.grid(False)
    ax1.axis('off')

    ax2.set_xlim(0, n_iterations)
    ax2.set_ylim(0, max(energy_history))
    ax2.set_title('Energy Transition')
    ax2.set_xlabel('Iteration')
    ax2.set_ylabel('Energy')

    return patches + [line]


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

    energy_history.append(current_energy)

    for i, circle in enumerate(patches):
        circle.set_facecolor(state[i])

    line.set_data(range(len(energy_history)), energy_history)

    return patches + [line]


ani = animation.FuncAnimation(
    fig1, update, frames=n_iterations, init_func=init, blit=True, repeat=False, interval=0.01)


def update_energy_graph(*args):
    ax2.set_ylim(0, max(energy_history) * 1.1)
    fig2.canvas.draw_idle()


fig2.canvas.mpl_connect('draw_event', update_energy_graph)

plt.show()

print(f"Best Energy: {best_energy}")
