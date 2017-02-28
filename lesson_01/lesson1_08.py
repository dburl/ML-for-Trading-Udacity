import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as spo


def f(x):
    y = (x-1.5)**2+0.5
    print("X={}, Y={}".format(x, y))
    return y


def optimizer():
    Xguess = 2.0
    min_result = spo.minimize(f, Xguess, method='SLSQp',
                              options={'disp': True})
    print("Minima found at:")
    print("X={}, Y={}".format(min_result.x, min_result.fun))

    # Plot function
    x_plot= np.linspace(0.5, 2.5, 21)
    y_plot = f(x_plot)
    plt.plot(x_plot, y_plot)
    plt.plot(min_result.x, min_result.fun, 'ro')
    plt.title('Minima of an objective function')
    plt.show()


def error(line, data):
    return np.sum((data[:, 1]-(line[0]*data[:, 0]+line[1]))**2)


def fit_line(data, error_func):
    l = np.float32([0, np.mean(data[:, 1])])
    x_ends = np.float32([-5, 5])
    plt.plot(x_ends, l[0]*x_ends+l[1], 'm--', linewidth=2.0,
             label="Initial guess")
    result = spo.minimize(error_func, l, args=(data,), method='SLSQP',
                        options={'disp':True})
    return result.x


def fit_line_exe():
    l_orig = np.float32([4, 2])
    print("Original line: C0={}, C1={}".format(l_orig[0], l_orig[1]))
    x_orig = np.linspace(0, 10, 21)
    y_orig = l_orig[0] * x_orig + l_orig[1]
    plt.plot(x_orig, y_orig, 'b--', linewidth=2.0, label='Original Line')
    # generate noise data points

    noise_sigma = 3.0
    noise = np.random.normal(0, noise_sigma, y_orig.shape)
    data = np.asarray([x_orig, y_orig + noise]).T
    plt.plot(data[:, 0], data[:, 1], 'go', label='Data points')
    # Fit the line to this data
    l_fit = fit_line(data, error)
    print("Fitted line: C0={}, C1={}".format(l_fit[0], l_fit[1]))
    plt.plot(data[:, 0], l_fit[0]*data[:, 0]+l_fit[1], 'r--', linewidth=2.0)
    plt.show()


def error_poly(C, data):
    return np.sum((data[:, 1]-np.polyval(C, data[:, 0]) )**2)


def fit_poly_exe(degree=3):
    Cguess = np.poly1d(np.ones(degree+1, dtype=np.float32))
    x_orig = np.linspace(-5, 5, 21)
    y_orig = np.polyval(Cguess, x_orig)
    plt.plot(x_orig, y_orig, 'b--', linewidth=2.0, label='Original Line')
    # generate noise data points
    noise_sigma = 10.0
    noise = np.random.normal(0, noise_sigma, y_orig.shape)
    data = np.asarray([x_orig, y_orig + noise]).T
    plt.plot(data[:, 0], data[:, 1], 'go', label='Data points')
    # Fit the poly to this data
    result = spo.minimize(error_poly, Cguess, args=(data,), method='SLSQP',
                        options={'disp':True})
    plt.plot(data[:, 0], np.polyval(result.x, data[:, 0]), 'r--', linewidth=2.0)
    plt.show()
