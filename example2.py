import numpy as np
from rectpsa import psa, cond
import matplotlib.pylab as plt


if __name__ == '__main__':
    A = np.array([[-1, 1], [0, -1]])
    B = np.array([[-1, 5], [0, -2]])

    print("Condition Number of A: {}".format(cond(A)))
    npts = 100
    xmin, xmax = -3.0, 1.0
    ymin, ymax = -2.0, 2.0
    # x = np.arange(xmin, xmax, (xmax-xmin) / (npts-1))
    # y = np.arange(ymin, ymax, (ymax-ymin) / (npts-1))
    # X, Y = np.meshgrid(x, y)
    X, Y = np.meshgrid(np.linspace(xmin, xmax, npts),
                       np.linspace(ymin, ymax, npts))

    spectra_a, s_max = psa(A, X, Y, method='svd')
    spectra_b, s_max = psa(B, X, Y, method='svd')

    plt.xkcd()
    fig = plt.figure(figsize=(9, 4))
    ax = fig.add_subplot(121)
    circles = np.logspace(np.log10(0.05), np.log10(2.1), 10)[:-3]
    CS = ax.contour(X, Y, spectra_a+1e-20, levels=circles)
    plt.clabel(CS, inline=1, fontsize=10)
    ax = fig.add_subplot(122)
    CS = ax.contour(X, Y, spectra_b+1e-20, levels=circles)
    plt.clabel(CS, inline=1, fontsize=10)
    plt.savefig('psuedo.pdf', axis='tight')
    plt.show()
