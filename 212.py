import matplotlib.pyplot as plt
import numpy as np
from fitter import Fitter
from scipy import stats

plt.figure()

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['mathtext.fontset'] = 'cm'

xx = np.arange(-1, 1.2, 0.001)

L = 20


def f(x):
    return np.exp(-(x - 0.1)**2 * L / 2) / (2 * np.pi / L)**0.5


plt.subplot(2, 1, 1)

plt.plot(xx, f(xx), label='target', linewidth=3)

plt.ylim(0, 2)
plt.xlim(-1, 1.2)

ts = 1
tz = 5
m = 0.99 * ts / tz
u0 = 17
gamma = 0.5
Lam = 20
dt = ts / 10
end_time = 5 * ts
T = int(end_time * 1000 / dt)
s = np.zeros(T)
y = np.zeros(T)
beta = tz / ts * ((ts / tz - m) * u0 / gamma + Lam)

for t in range(T - 1):
    ds = gamma / u0 * y[t]
    dy = -beta * gamma / u0 * y[t] + Lam * (0.1 - s[t]) + np.sqrt(
        2 * beta * ts / tz * tz / dt) * np.random.normal(0, 1)
    s[t + 1] = s[t] + ds * dt / ts
    y[t + 1] = y[t] + dy * dt / tz

f2 = Fitter(s)  # 创建Fitter类

f2.hist()
plt.legend()

plt.xticks([])
plt.yticks([])

plt.vlines(x=[0.1],
           ymin=[0],
           ymax=[1 / (2 * np.pi / L)**0.5],
           linestyle='--',
           color='black')

plt.ylabel("Probability", fontsize=20)

plt.subplot(2, 1, 2)

plt.xlim(-1, 1.2)
plt.xticks([])
plt.yticks([])
plt.xticks([0.1], [r'$s^{po}$'], size=15)
plt.axvline(x=0.1, linestyle='--', color='black')
plt.yticks([45000, 50000], [0.5, 0])
tt = np.arange(T, 0, -1)
plt.xlabel(r'Latent feature $s$', fontsize=18)
plt.ylabel(r'Time $t(/\tau_s)$', fontsize=18)
plt.plot(s[:5000], tt[:5000])
plt.subplots_adjust(wspace=0, hspace=0)
plt.show()