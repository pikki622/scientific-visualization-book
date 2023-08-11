import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset


def simulate():
    d = 0.005
    x = np.random.uniform(0, d)
    y = d - x
    x, y = np.random.uniform(0, d, 2)

    dt = 0.05
    t = 35.0
    alpha = 0.25
    n = int(t / dt)
    X = np.zeros(n)
    Y = np.zeros(n)
    C = np.random.randint(0, 2, n)

    for i in range(n):
        dx = (alpha + (x - y)) * (1 - x) * dt
        dy = (alpha + (y - x)) * (1 - y) * dt
        x = max(x + dx, 0.0)
        y = max(y + dy, 0.0)
        X[i] = x
        Y[i] = y
    return X, Y


np.random.seed(11)
n = 250
S = [simulate() for _ in range(n)]
plt.figure(figsize=(20, 10))
ax = plt.subplot(121, aspect=1)
axins = zoomed_inset_axes(ax, 25, loc=3)
for i in range(n):
    X, Y = S[i]
    if X[-1] > 0.9 and Y[-1] > 0.9:
        c = "r"
        axins.scatter(X[0], Y[0], c="r", edgecolor="w", zorder=10)
    else:
        c = "b"
    lw = 1.0
    ax.plot(X, Y, c=c, alpha=0.25, lw=lw)
    axins.plot(X, Y, c=c, alpha=0.25, lw=lw)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xlabel("x position")
ax.set_ylabel("y position")
ax.set_title("%d trajectories of a dual particle system (x,y)" % n)
axins.set_xlim(0.01, 0.02)
axins.set_xticks([])
axins.set_ylim(0.01, 0.02)
axins.set_yticks([])

ax = plt.subplot(122, aspect=1)
axins = zoomed_inset_axes(ax, 50, loc=3)
axins.set_facecolor((1, 1, 0.9))
n = 9
lw = 2.0
for i in range(n):
    X, Y = S[i]
    ls = "-"
    if i == 2:
        ls = "--"
    if X[-1] > 0.9 and Y[-1] > 0.9:
        c = "r"
        axins.scatter(X[0], Y[0], s=150, c="r", edgecolor="w", zorder=10, lw=2)
    else:
        c = "b"
    ax.plot(X, Y, c=c, alpha=0.75, lw=lw, ls=ls)
    axins.plot(X, Y, c=c, alpha=0.75, lw=lw, ls=ls)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xticks([0, 1])
ax.set_yticks([0, 1])
ax.set_xticklabels(["0", "1"], fontsize=16)
ax.set_yticklabels(["0", "1"], fontsize=16)
ax.set_xlabel("x position", fontsize=20)
ax.set_ylabel("y position", fontsize=20)
# ax.set_title('%d trajectories of a dual particle system (x,y)' % n)
axins.set_xlim(0.01, 0.02)
axins.set_xticks([])
axins.set_ylim(0.01, 0.02)
axins.set_yticks([])

plt.savefig("../../figures/rules/rule-3.pdf")
plt.show()
