x = np.linspace( 0.1, 6.*np.pi, num=200)
y = np.sin(x) / x

plt.plot(x,y, 'r:', label='sin(x)/x')

plt.grid()
plt.legend()
