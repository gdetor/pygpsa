import numpy as np
from scipy.linalg import expm
import matplotlib.pylab as plt


if __name__ == '__main__':
    A = np.array([[-1, 1], [0, -1]])
    B = np.array([[-1, 5], [0, -2]])

    t = np.linspace(0.1, 5, 50)

    norm_a, norm_b = [], []
    for i in t:
        norm_a.append(np.linalg.norm(expm(A * i)))
        norm_b.append(np.linalg.norm(expm(B * i)))

    plt.xkcd()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.subplots_adjust(bottom=0.15, left=0.15)

    ax.plot(norm_a, 'b')
    ax.plot(norm_b, 'k')
    ticks = ax.get_xticks().astype('i')
    ax.set_xticklabels(ticks, fontsize=16, weight='bold')
    ticks = ax.get_yticks()
    ax.set_yticklabels(ticks, fontsize=16, weight='bold')
    ax.set_xlabel('Time', fontsize=18, weight='bold')
    ax.set_ylabel(r'$||exp(At)||$', fontsize=18, weight='bold')
    plt.savefig('spectra.pdf', axis='tight')
    plt.show()
