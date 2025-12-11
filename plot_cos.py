import numpy as np
import matplotlib.pyplot as plt

from plot_utils import multiple_formatter

in_array = np.linspace(-np.pi*3, np.pi*3, 12)
out_array = np.cos(in_array)

print("in_array : ", in_array)
print("\nout_array : ", out_array)

# blue for numpy.cos()
fig, ax = plt.subplots()
ax.plot(in_array, out_array, color = 'blue', marker = "o")
ax.set_title("numpy.cos()")
ax.set_xlabel("X")
ax.set_xlabel("Y")
ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi / 2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(np.pi / 12))
ax.xaxis.set_major_formatter(plt.FuncFormatter(multiple_formatter()))
plt.show()
