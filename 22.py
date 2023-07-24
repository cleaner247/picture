import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['mathtext.fontset'] = 'cm'

s = np.arange(0, 10, 0.01)

mu2 = 5
sigma2 = (6 / 5)**0.5

spr = 1 / np.sqrt(2 * np.pi * sigma2**2) * np.exp(-(s - mu2)**2 /
                                                  (2 * sigma2**2))
y2max = 1 / np.sqrt(2 * np.pi * sigma2**2)
plt.plot(s, spr, linewidth=3,color='orange')
plt.vlines(x=[5], ymin=[0], ymax=[y2max], linestyle='--', color='black')

plt.ylim(0, 0.38)
plt.xlim(2, 8)
plt.xticks([])
plt.yticks([])
plt.axis('off')
plt.xticks([5], [r'$s^{pr}$'], size=15)
plt.show()