import scipy.integrate as integrate

def f(x):
        return np.exp(-x)

integrate.quad(f, 0, np.inf)
