# adapted from https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill_between_demo.html#example-confidence-bands

from best import x_data, y_data
import matplotlib.pyplot as plt
import numpy as np
import os

x = np.array(list(map(lambda l: l[0], x_data)))
y = np.array(y_data)

# fit a linear curve and estimate its y-values and their error.
a, b = np.polyfit(x, y, deg=1)
y_est = a * x + b
y_err = x.std() * np.sqrt(1/len(x) +
                          (x - x.mean())**2 / np.sum((x - x.mean())**2))

fig, ax = plt.subplots()
ax.plot(x, y_est, '-')
ax.fill_between(x, y_est - y_err, y_est + y_err, alpha=0.2)
ax.plot(x, y, 'o', color='tab:red')
ax.set_xlabel('Age')
ax.set_ylabel('Proficiency')

plt.savefig(os.path.join("..", "frontend", "public", "fig-3.png"))