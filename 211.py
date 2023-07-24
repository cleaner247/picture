import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['mathtext.fontset'] = 'cm'

s = np.arange(0, 10, 0.01)

mu1 = 2
sigma1 = 3**0.5
mu2 = 5
sigma2 = (6 / 5)**0.5

spr = 1 / np.sqrt(2 * np.pi * sigma1**2) * np.exp(-(s - mu1)**2 /
                                                  (2 * sigma1**2))

spo = 1 / np.sqrt(2 * np.pi * sigma2**2) * np.exp(-(s - mu2)**2 /
                                                  (2 * sigma2**2))

plt.plot(s, spr, '--', linewidth=3)
plt.plot(s, spo, linewidth=3)

plt.legend(["prior", "posterior"], loc='upper right')

plt.ylim(0, 0.38)
plt.xlim(0, 10)
plt.xticks([])
plt.yticks([])
plt.xlabel(r'Latent feature $s$', fontsize=18)
plt.ylabel("Probability", fontsize=20)
plt.xticks([2, 5, 7], [r'$s^{pr}$', r'$s^{po}$', r'$s^o$'], size=15)
y1max = 1 / np.sqrt(2 * np.pi * sigma1**2)
y2max = 1 / np.sqrt(2 * np.pi * sigma2**2)
y1 = 1 / np.sqrt(2 * np.pi * sigma1**2) * np.exp(-(0.5 - mu1)**2 /
                                                 (2 * sigma1**2))
y2 = 1 / np.sqrt(2 * np.pi * sigma2**2) * np.exp(-(5.6 - mu2)**2 /
                                                 (2 * sigma2**2))
plt.vlines(x=[2, 5],
           ymin=[0, 0],
           ymax=[y1max, y2max],
           linestyle='--',
           color='black')

plt.arrow(2,
          y1,
          -1.5,
          0,
          head_width=0.01,
          head_length=0.3,
          linewidth=2,
          color='k',
          length_includes_head=True)

plt.arrow(2,
          y1,
          1.5,
          0,
          head_width=0.01,
          head_length=0.3,
          linewidth=2,
          color='k',
          length_includes_head=True)

plt.arrow(5,
          y2,
          -0.6,
          0,
          head_width=0.01,
          head_length=0.3,
          linewidth=2,
          color='k',
          length_includes_head=True)

plt.arrow(5,
          y2,
          0.6,
          0,
          head_width=0.01,
          head_length=0.3,
          linewidth=2,
          color='k',
          length_includes_head=True)

plt.text(2, y1 + 0.01, r'$L^{-1}$', fontsize=15)
plt.text(4.5, y2 - 0.03, r'$ (L+\Lambda)^{-1}$', fontsize=15)

plt.show()
