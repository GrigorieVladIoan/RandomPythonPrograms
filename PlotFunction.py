import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate



def grafic(x, y, color):

    #>:)

    x = np.array(x)
    y = np.array(y)

    t, c, k = scipy.interpolate.splrep(x, y, s=100, k=3)

    xx = np.linspace(x.min(), x.max(), 300)
    spline = scipy.interpolate.BSpline(t, c, k, extrapolate=False)

    style = color + "o"

    plt.plot(x, y, style, markersize=3, label='Original points')
    plt.plot(xx, spline(xx), color)

    plt.grid()

