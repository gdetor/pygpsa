import numpy as np
import matplotlib.pylab as plt
from scipy.linalg import expm
from rectpsa import psa, cond


if __name__ == '__main__':
    np.random.seed(7)
    dt = 0.01
    tf = 100
    sim_time = int(tf / dt)

    A = np.array([[0, 1], [-2, -3]])
    print(np.linalg.eigvals(A))
    print(np.dot(A, A.T) - np.dot(A.T, A))

    B = np.random.uniform(-1, 1., (2, 2))
    # B = np.random.normal(0, 1, (2, 2))
    print(np.linalg.eigvals(B))
    print(np.dot(B, B.T) - np.dot(B.T, B))

    x = np.ones((sim_time, 2))
    x[0] = 0.5
    ref = 2

    tr_ = []
    for t in range(1, sim_time):
        u = 0.1 * (ref - x[t-1])
        # x[t] = x[t-1] + dt * (np.dot(A, x[t-1]))
        tr_.append(np.dot(B, u))
        x[t] = x[t-1] + dt * (np.dot(A, x[t-1]) + np.dot(B, u))

    plt.figure()
    plt.plot(x)

    plt.figure()
    plt.plot(tr_)

    t = np.linspace(0, 5, 50)

    norm_a, norm_b = [], []
    for i in t:
        norm_a.append(np.linalg.norm(expm(A * i)))
        norm_b.append(np.linalg.norm(expm(B * i)))

    plt.figure()
    plt.plot(norm_a, 'b')
    plt.plot(norm_b, 'k')

    npts = 100
    xmin, xmax = -1.0, 1.0
    ymin, ymax = -1.0, 1.0
    X, Y = np.meshgrid(np.linspace(xmin, xmax, npts),
                       np.linspace(ymin, ymax, npts))

    spectra, s_max = psa(B, X, Y, method='svd')

    plt.figure()
    # circles = np.logspace(np.log10(10e-5), np.log10(1), 10)
    circles = np.logspace(np.log10(10e-4), np.log10(1), 20)[:-3]
    CS = plt.contour(X, Y, spectra+1e-20, levels=circles)
    # CS = plt.contour(X, Y, np.log10(spectra+1e-20))
    plt.clabel(CS, inline=1, fontsize=10)
    plt.show()
