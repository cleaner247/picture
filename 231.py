import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['mathtext.fontset'] = 'cm'

s = np.arange(0, 12, 0.01)

mu1 = 8
sigma1 = 1.5**0.5
mu2 = 5
sigma2 = 0.5**0.5
mu3 = 3
sigma3 = 0.7**0.5

spr = 1 / np.sqrt(2 * np.pi * sigma1**2) * np.exp(-(s - mu1)**2 /
                                                  (2 * sigma1**2))

spo = 1 / np.sqrt(2 * np.pi * sigma2**2) * np.exp(-(s - mu2)**2 /
                                                  (2 * sigma2**2))

z = 1 / np.sqrt(2 * np.pi * sigma3**2) * np.exp(-(s - mu3)**2 /
                                                (2 * sigma3**2))*0.8

plt.plot(s, spr, linewidth=3)
plt.plot(s, spo, linewidth=3)
plt.plot(s, z, linewidth=3)
plt.legend([r'$I^{ext}(x,t)$', r'$U(x,t)$', r'$V(x,t)$'], loc='upper right')

plt.ylim(0, 0.7)
plt.xlim(0, 12)
plt.xticks([])
plt.yticks([])
plt.xlabel(r'Feature space $x$', fontsize=18)
plt.ylabel("Current", fontsize=20)
plt.xticks([8, 5, 3], [r'$s^{o}$', r'$s(t)$', r'$s(t)-z(t)$'], size=12)
y1max = 1 / np.sqrt(2 * np.pi * sigma1**2)
y2max = 1 / np.sqrt(2 * np.pi * sigma2**2)
y1 = 1 / np.sqrt(2 * np.pi * sigma1**2) * np.exp(-(0.5 - mu1)**2 /
                                                 (2 * sigma1**2))
y2 = 1 / np.sqrt(2 * np.pi * sigma2**2) * np.exp(-(5.6 - mu2)**2 /
                                                 (2 * sigma2**2))
plt.vlines(x=[8, 5, 3],
           ymin=[0, 0, 0],
           ymax=[y1max, y2max, 1 / np.sqrt(2 * np.pi * sigma3**2)*0.8],
           linestyle='--',
           color='black')

plt.show()
