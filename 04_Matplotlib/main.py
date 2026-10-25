import matplotlib.pyplot as plt
import numpy as np

print("-- Працюємо із графіками --")

# набір величин - точок по x
x = np.linspace(0, 2 * np.pi, 200)

# знаходимо sin від x
y = np.sin(x)

# Створюємо фігуру для малювання
fig, ax = plt.subplots()  # Figure - усе вікно графіку

ax.plot(x, y)  # - звичайний лінійний графік
plt.show()  # відображаємо графік функції
