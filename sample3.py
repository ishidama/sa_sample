import plotly.graph_objects as go
from plotly.subplots import make_subplots
import random
import numpy as np
import tkinter as tk
from tkinter import simpledialog

# 初期状態をランダムに生成する関数


def generate_initial_state(num_circles, colors):
    return [random.choice(colors) for _ in range(num_circles)]

# 系のエネルギーを評価する関数


def evaluate_energy(state):
    energy = 0
    for i in range(len(state) - 1):
        if state[i] != state[i + 1]:
            energy += 100
    return energy

# 隣接する色をランダムに交換する関数


def neighbor(state):
    new_state = state[:]
    i, j = random.sample(range(len(state)), 2)
    new_state[i], new_state[j] = new_state[j], new_state[i]
    return new_state


def simulate_annealing(steps):
    num_circles = 100
    colors = ['red', 'green', 'blue', 'yellow']
    state = generate_initial_state(num_circles, colors)

    initial_temp = 10000.0
    cooling_rate = 0.9

    current_energy = evaluate_energy(state)
    energy_history = [current_energy]
    frames = []

    for step in range(steps):
        t = initial_temp / (1 + cooling_rate * step)
        new_state = neighbor(state)
        new_energy = evaluate_energy(new_state)

        if new_energy < current_energy or random.random() < np.exp((current_energy - new_energy) / t):
            state = new_state
            current_energy = new_energy

        energy_history.append(current_energy)

        frames.append(go.Frame(
            data=[
                go.Scatter(
                    x=[i for i in range(num_circles)],
                    y=[0 for _ in range(num_circles)],
                    mode='markers',
                    marker=dict(color=state, size=20),
                    xaxis='x1',
                    yaxis='y1'
                ),
                go.Scatter(
                    x=list(range(len(energy_history))),
                    y=energy_history,
                    mode='lines',
                    name='Energy',
                    xaxis='x2',
                    yaxis='y2'
                )
            ],
            name=f'frame{step}'
        ))

    fig = make_subplots(rows=2, cols=1, subplot_titles=(
        'Circle States', 'Energy Over Iterations'))

    fig.add_trace(
        go.Scatter(
            x=[i for i in range(num_circles)],
            y=[0 for _ in range(num_circles)],
            mode='markers',
            marker=dict(color=state, size=20),
            name='Circles'
        ),
        row=1, col=1
    )

    fig.add_trace(
        go.Scatter(
            x=[0],
            y=[energy_history[0]],
            mode='lines',
            name='Energy'
        ),
        row=2, col=1
    )

    fig.update_layout(
        updatemenus=[{
            'buttons': [
                {
                    'args': [None, {'frame': {'duration': 100, 'redraw': True}, 'fromcurrent': True}],
                    'label': 'Play',
                    'method': 'animate'
                },
                {
                    'args': [[None], {'frame': {'duration': 0, 'redraw': True}, 'mode': 'immediate', 'transition': {'duration': 0}}],
                    'label': 'Pause',
                    'method': 'animate'
                }
            ],
            'direction': 'left',
            'pad': {'r': 10, 't': 87},
            'showactive': False,
            'type': 'buttons',
            'x': 0.1,
            'xanchor': 'right',
            'y': 0,
            'yanchor': 'top'
        }],
        sliders=[{
            'steps': [{'args': [[f'frame{step}'], {'frame': {'duration': 100, 'redraw': True}, 'mode': 'immediate'}],
                       'label': f'{step}', 'method': 'animate'} for step in range(steps)],
            'transition': {'duration': 0},
            'x': 0.1,
            'len': 0.9,
            'currentvalue': {'prefix': 'Step: ', 'font': {'size': 20}},
        }],
        title='Simulated Annealing Animation'
    )

    fig.frames = frames

    fig.update_xaxes(title_text='Circle Index', row=1, col=1)
    fig.update_yaxes(title_text='', row=1, col=1)
    fig.update_xaxes(title_text='Iteration', row=2, col=1)
    fig.update_yaxes(title_text='Energy', row=2, col=1)

    fig.show()


# Tkinterウィンドウを作成
root = tk.Tk()
root.withdraw()

# ユーザーにステップ数を入力させる
steps = simpledialog.askinteger(
    "Input", "Enter the number of steps:", minvalue=1, maxvalue=1000)

# シミュレーションを実行
if steps:
    simulate_annealing(steps)
