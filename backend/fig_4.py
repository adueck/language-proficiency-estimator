# adapted from https://matplotlib.org/stable/gallery/statistics/boxplot_vs_violin.html#sphx-glr-gallery-statistics-boxplot-vs-violin-py

from best import x_data, y_data
import matplotlib.pyplot as plt
import numpy as np
import os.path as path

AGE = 1
EDUCATION = 3
PERCENT = 7
INTERVIEW = 13
START = 16
PICTURE_TEST = 19
LEXTALE = 22

all_data = [
  np.array([]), np.array([2]), np.array([]), np.array([]),
]

for i in range(0, len(y_data)):
  if x_data[i][2] == 10:
    all_data[0] = np.append(all_data[0], y_data[i])
  if x_data[i][2] == 20:
    all_data[1] = np.append(all_data[1], y_data[i])
  if x_data[i][2] == 30:
    all_data[2] = np.append(all_data[2], y_data[i])
  if x_data[i][2] == 40:
    all_data[3] = np.append(all_data[3], y_data[i])

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(9, 4))

# plot violin plot
axs[0].violinplot(all_data,
                  showmeans=False,
                  showmedians=True)
axs[0].set_title('Violin plot')

# plot box plot
axs[1].boxplot(all_data)
axs[1].set_title('Box plot')

# adding horizontal grid lines
for ax in axs:
    ax.yaxis.grid(True)
    ax.set_xticks([y + 1 for y in range(len(all_data))],
                  labels=['10%', '20%', '30%', '40%'])
    ax.set_xlabel('Percentage Exposed to English')
    ax.set_ylabel('Proficiency')

plt.savefig(path.join("..", "frontend", "public", "fig-4.png"))