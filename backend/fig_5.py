# adapted from https://aegis4048.github.io/mutiple_linear_regression_and_visualization_in_python

from best import x_data, y_data
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
import os
import subprocess
import glob

X = np.array(list(map(lambda l: [l[0], l[2]], x_data)))
Y = y_data

x = X[:, 0]
y = X[:, 1]
z = (list(map(lambda l: l[0], Y)))

x_pred = np.linspace(0, 70, 30)
y_pred = np.linspace(18, 60, 30)
xx_pred, yy_pred = np.meshgrid(x_pred, y_pred)
model_viz = np.array([xx_pred.flatten(), yy_pred.flatten()]).T

ols = linear_model.LinearRegression()
model = ols.fit(X, Y)
predicted = model.predict(model_viz)

r2 = model.score(X, Y)

plt.style.use('default')

# make still-image diagram rotated three different angles
fig = plt.figure(figsize=(12, 4))

ax1 = fig.add_subplot(131, projection='3d')
ax2 = fig.add_subplot(132, projection='3d')
ax3 = fig.add_subplot(133, projection='3d')

axes = [ax1, ax2, ax3]

for ax in axes:
  ax.plot(y, x, z, color="tab:red", zorder=15, linestyle='none', marker='o', alpha=0.5)
  ax.scatter(xx_pred.flatten(), yy_pred.flatten(), predicted, color="blue", s=20, edgecolor='#70b3f0')
  ax.set_xlabel('English Exposure', fontsize=12)
  ax.set_ylabel('Age', fontsize=12)
  ax.set_zlabel('Proficiency', fontsize=12)
  ax.locator_params(nbins=4, axis='x')
  ax.locator_params(nbins=10, axis='x')

ax1.view_init(elev=16, azim=120)
ax2.view_init(elev=16, azim=85)
ax3.view_init(elev=16, azim=210)

fig.suptitle('$R^2 = %.2f$' % r2, fontsize=20)

fig.tight_layout()
fig.savefig(os.path.join("..", "frontend", "public", "fig-5.png"))

anim_fig = plt.figure()

ax = anim_fig.add_subplot(111, projection='3d')
ax.plot(y, x, z, color="tab:red", zorder=15, linestyle='none', marker='o', alpha=0.5)
ax.scatter(xx_pred.flatten(), yy_pred.flatten(), predicted, color="blue", s=20, edgecolor='#70b3f0')
ax.set_xlabel('English Exposure', fontsize=12)
ax.set_ylabel('Age', fontsize=12)
ax.set_zlabel('Proficiency', fontsize=12)
ax.locator_params(nbins=4, axis='x')
ax.locator_params(nbins=10, axis='x')

ax.view_init(elev=18, azim=10)

anim_fig.tight_layout()
anim_fig.set_frameon(True)
# anim_fig.suptitle('$R^2 = %.2f$' % r2, fontsize=20)

os.mkdir("gif")
for ii in np.arange(0, 360, 1):
  ax.view_init(elev=32, azim=ii)
  anim_fig.savefig(os.path.join("gif", "gif_image%d.png" % ii))

# convert the png files of the different angles to a gif file
gif_files = glob.glob(os.path.join("gif", "*"))
for f in gif_files:
  # remove alpha background, doesn't seem to help the issue with strange yellow on ffmpeg gif
  subprocess.call(["convert", f, "-background", "white", "-alpha", "remove", "-flatten", "-alpha", "off", f])
subprocess.call(['ffmpeg', '-y', '-i', os.path.join("gif", "gif_image%d.png"), os.path.join("..", "frontend", "public", "fig_5.gif")])
files = glob.glob(os.path.join("gif", "*"))
for f in files:
    os.remove(f)
os.rmdir("gif")