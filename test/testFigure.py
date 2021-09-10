import matplotlib.pyplot as plt
import random

x = 5
y = 5
figure = plt.figure(figsize=(y, x), dpi=80)
data = [random.random() for i in range(10)]
figure.clear()
ax = figure.add_subplot(y, x, 1) # hauteur, largeur, position
ax1 = figure.add_subplot(y, x, 2)
ax2 = figure.add_subplot(y, x, 3)
ax3 = figure.add_subplot(y, x, 4)
ax4 = figure.add_subplot(y, x, 5)
ax5 = figure.add_subplot(y, x, 6)
ax.plot(data, "*-")
ax1.plot(data, "*-")
ax2.plot(data, "*-")
ax3.plot(data, "*-")
ax4.plot(data, "*-")
ax5.plot(data, "*-")
#plt.show()