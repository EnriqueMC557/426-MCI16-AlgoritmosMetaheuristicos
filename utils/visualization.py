#! /usr/bin/env python3
"""Visualization utilities."""

import os
import time

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import animation

from utils.casting import bin_array_to_int


def plot_aptitude(avg_aptitude: np.ndarray, max_aptitude: np.ndarray, max_generations: int, title: str):
    plt.figure(figsize=(10, 5))
    plt.title(title)
    plt.plot(avg_aptitude, "o-",label="Average aptitude")
    plt.plot(max_aptitude, "o-", label="Max aptitude")
    plt.xlabel("Generation")
    plt.ylabel("Aptitude")
    plt.xticks(range(max_generations))
    plt.legend()
    plt.grid()
    plt.savefig(f"./figures/{'_'.join(title.replace('+', '').lower().split())}.png", bbox_inches='tight')
    plt.show()


def plot_evolution(evolution: np.ndarray, title: str):
    fig, ax = plt.subplots()
    ax.set_xlim((-1, 1))
    ax.set_ylim((0, 1))
    
    x_ = np.linspace(-1, 1, 100)
    ax.plot(x_, x_**2, 'r--')
    plt.grid()
    
    txt_title = ax.set_title('')
    points = []
    for _ in range(6):
        pt, = ax.plot([], [], 'g.', ms=20)
        points.append(pt)

    frames = len(evolution)
    def drawframe(n):
        txt_title.set_text(f"{title} (Generation {n})")
        for idx, pt in enumerate(points):
            min = 0
            max = 2**6 - 1
            decoded_individue = bin_array_to_int(evolution[n%frames][idx])
            decoded_individue = (decoded_individue - min) / (max - min)
            decoded_individue = 2 * decoded_individue - 1
            pt.set_data([decoded_individue], [decoded_individue**2])
        return points

    anim = animation.FuncAnimation(fig, drawframe, frames=frames, interval=1, blit=True)
    
    filename = f"./figures/{'_'.join(title.replace('+', '').lower().split())}.gif"

    if os.path.exists(filename):
        os.remove(filename)

    _ = anim.save(filename, fps=2)
    plt.close(fig)
    time.sleep(1)

    return filename
