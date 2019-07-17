import numpy as np
from rectpsa import psa, cond
import matplotlib.pylab as plt


if __name__ == '__main__':
    A = np.array([[1, 10, 10], [0, 2.1, 4.2], [0, 0.1, 0.2], [0, 0.1, 0.2]])
    u, s, v = np.linalg.svd(A)
    print(s)
    u, s, v = np.linalg.svd(A.T)
    print(s)
    # A = A[:3, :]
    # A = A[:, :2]

    print("Condition Number of A: {}".format(cond(A)))
    npts = 100
    xmin, xmax = -1.0, 3.5
    ymin, ymax = -1.5, 1.5
    # x = np.arange(xmin, xmax, (xmax-xmin) / (npts-1))
    # y = np.arange(ymin, ymax, (ymax-ymin) / (npts-1))
    # X, Y = np.meshgrid(x, y)
    X, Y = np.meshgrid(np.linspace(xmin, xmax, npts),
                       np.linspace(ymin, ymax, npts))

    spectra, s_max = psa(A, X, Y, method='svd')

    plt.figure()
    # circles = np.logspace(np.log10(10e-5), np.log10(1), 10)
    circles = np.logspace(np.log10(10e-4), np.log10(1.5), 20)[:-3]
    print(circles)
    CS = plt.contour(X, Y, spectra+1e-20, levels=circles)
    # CS = plt.contour(X, Y, np.log10(spectra+1e-20))
    plt.clabel(CS, inline=1, fontsize=10)
    plt.show()
