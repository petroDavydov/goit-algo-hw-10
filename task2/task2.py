import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi
from colorama import Fore, Style, init
init(autoreset=True)

# Визначення функції та межі інтегрування


def f(x):
    return x ** 2


a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)


# Monte-Carlo method

while True:
    try:
        N = int(input("Введіть кількість точок для Монте-Карло (N): "))
        if N > 0:
            break
        else:
            print("Помилка: N має бути додатним числом. Спробуйте ще раз")
    except ValueError:
        print("Помилка: введіть ціле число.")

x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, f(b), N)

points_under_curve = y_random <= f(x_random)
num_under_curve = np.sum(points_under_curve)

rect_area = (b - a) * f(b)

monte_carlo_area = (num_under_curve / N) * rect_area

print(f"{Fore.BLUE}Monte-Carlo area under curve: {monte_carlo_area}{Style.RESET_ALL}")


# use Scipy
result, error = spi.quad(f, a, b)

# use google for accuracy analysis Skipy
error_monte_carlo = abs(monte_carlo_area - result)


# Налаштування графіка
ax.set_xlim(x[0], x[-1])  # виправлено
ax.set_ylim(0, max(y) + 0.1)  # виправлено
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
ax.text(0.5, max(y) * 0.7,
        f'Monte-Carlo: {monte_carlo_area:.4f}\nQuad: {result:.4f}', fontsize=12, color='blue')

plt.show()


# Print result
print(f"{Fore.LIGHTCYAN_EX}Quad integration result: {result}{Style.RESET_ALL}")
print(f"{Fore.LIGHTGREEN_EX}Error from Quad: {error}{Style.RESET_ALL}")
print(f"{Fore.LIGHTRED_EX}Monte-Carlo Error: {error_monte_carlo}{Style.RESET_ALL}")
