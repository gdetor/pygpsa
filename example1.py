import numpy as np
from rectpsa import psa, cond
import matplotlib.pylab as plt


if __name__ == '__main__':
    A = np.array([[1, 10, 10], [0, 2.1, 4.2], [0, 0.1, 0.2], [0, 0.1, 0.2]])

    print("Condition Number of A: {}".format(cond(A)))
    npts = 300
    # x = np.arange(xmin, xmax, (xmax-xmin) / (npts-1))
    # y = np.arange(ymin, ymax, (ymax-ymin) / (npts-1))
    # X, Y = np.meshgrid(x, y)
    X, Y = np.meshgrid(np.linspace(-.4, .4, npts),
                       np.linspace(-.4, .4, npts))

    spectra = psa(A, X, Y, method='svd')

    plt.figure()
    circles = np.logspace(np.log10(10e-5), np.log10(1), 10)
    # CS = plt.contour(X, Y, spectra+1e-20, levels=circles)
    CS = plt.contour(X, Y, np.log10(spectra+1e-20))
    plt.clabel(CS, inline=1, fontsize=10)
    plt.show()
