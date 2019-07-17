import numpy as np
from rectpsa import psa, cond
import matplotlib.pylab as plt


if __name__ == '__main__':
    # A = np.array([[1, 1, 0], [0, 1, 1], [1, 0, 1]])
    A = np.random.uniform(-0.5, 0.5, (50, 2)) * 2.0
    print(A.max(), A.min())

    print("Condition Number of A: {}".format(cond(A)))
    npts = 100
    xmin, xmax = -5.0, 5.0
    ymin, ymax = -5.0, 5.0
    X, Y = np.meshgrid(np.linspace(xmin, xmax, npts),
                       np.linspace(ymin, ymax, npts))

    spectra_a, s_max = psa(A, X, Y, method='svd')

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111)
    # circles = np.logspace(np.log10(0.05), np.log10(2.1), 10)[:-3]
    # CS = ax.contour(X, Y, spectra_a+1e-20, levels=circles)
    CS = ax.contour(X, Y, spectra_a+1e-20)
    plt.clabel(CS, inline=1, fontsize=10)
    plt.show()
