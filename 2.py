import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def f(x):
    return x ** 2

a = 0  
b = 2  

n_points = 10000

x_random = np.random.uniform(a, b, n_points)
y_random = np.random.uniform(0, f(b), n_points)

under_curve = y_random < f(x_random)
area_estimate = (b - a) * f(b) * np.sum(under_curve) / n_points

result_quad, error = spi.quad(f, a, b)

print(f"Інтеграл методом Монте-Карло: {area_estimate}")
print(f"Інтеграл за допомогою quad: {result_quad}")
print(f"Абсолютна похибка: {abs(area_estimate - result_quad)}")

# Графік
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.scatter(x_random, y_random, color="blue", s=1, alpha=0.1)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
