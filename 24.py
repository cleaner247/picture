import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['mathtext.fontset'] = 'cm'

mth = 1.04 * 0.2
mmax = 0.64 * 0.2
m = np.arange(0, 0.3, 0.001)
h1 = 0.5 * (mth - m - np.sqrt(
    ((mth - m)**2 - 4 * 3 / 375 / 5).astype(np.complex_))).real
h2 = 0.5 * (mth - m - np.sqrt(
    ((mth - m)**2 - 4 * 3 / 375 / 5).astype(np.complex_))).imag
plt.ylim(0, 0.05)
plt.xlim(0, 0.3)

plt.plot(m, h1, linewidth=3)
plt.plot(m, -h2, linewidth=5)
plt.xlabel(r'Adaptation strength $m$', fontsize=15)
plt.xticks([])
plt.yticks([])
plt.xticks([0,mmax, mth], [0,r'$m_{max}$', r'$m_{th}$'], size=15)
plt.legend([r'$Re(h)$', r'$Im(h)$'], loc='upper left')
plt.vlines(x=[mmax, mth],
           ymin=[0, 0],
           ymax=[0.05, 0.05],
           linestyle='--',
           color='black')
plt.text(mmax + 0.01, 0.042, 'Oscillation', fontsize=15)
plt.text(mth + 0.02, 0.045, 'Traveling', fontsize=15)
plt.text(mth + 0.02, 0.042, 'wave', fontsize=15)
plt.text(mmax - 0.08, 0.035, 'Max speed', fontsize=15)
plt.scatter(mth, 0.04, marker='x', s=60, c='k')

plt.scatter(mmax, 0.04, marker='o', s=60, c='k')
plt.arrow(0.09,
          0.038,
          0.03,
          0.002,
          head_width=0.001,
          head_length=0.003,
          width=0.0001,
          color='k',
          length_includes_head=True)
plt.show()
