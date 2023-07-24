import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams["axes.grid"] = False
xx = np.arange(-1, 1.2, 0.001)

L = 20


def f(x):
    return np.exp(-(x - 0.1)**2 * L / 2) / (2 * np.pi / L)**0.5


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
        2 * beta * ts / tz * tz / dt) * np.random.normal(0, 1) * 10
    s[t + 1] = s[t] + ds * dt / ts
    y[t + 1] = y[t] + dy * dt / tz


# 定义高斯能量函数
def gaussian_energy_function(x, t, x0_t, sigma):
    return np.exp(-((x - x0_t)**2) /
                  (2 * sigma**2)) * (1 + 0.1 * np.random.random())


# 创建时间坐标轴和空间坐标轴
t_values = np.linspace(0, 10, 100)
x_values = np.linspace(-15, 15, 100)

# 设置参数
sigma = 3

# 创建网格点
T, X = np.meshgrid(t_values, x_values)

# 初始化波包顶点位置随时间的变化
x0_t_values = s[:100]

# 计算能量函数随时间和空间的变化
energy_values = gaussian_energy_function(X, T, x0_t_values, sigma)

# 绘制三维图
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_zlim([0, 2])
ax.set_ylim([-15, 15])

ax.plot_surface(T, X, energy_values, rstride=1, cstride=1, cmap=plt.cm.cool)

# 标记波包顶点位置随时间的变化
ax.plot(t_values,
        x0_t_values,
        np.max(energy_values, axis=0),
        color='k',
        linewidth=5,
        label=r'Sampling trace $s(t)$')
ax.set_xlabel('Time')
ax.set_ylabel('X')
ax.set_zlabel('Energy')
plt.axis('off')
# 设置图形标题
plt.title('Gaussian Energy Function with Time-varying Center')

plt.legend()

plt.show()
