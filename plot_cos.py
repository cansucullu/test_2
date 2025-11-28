import numpy as np
import matplotlib.pyplot as plt

in_array = np.linspace(-np.pi*3, np.pi*3, 120)
out_array = np.cos(in_array)

print("in_array : ", in_array)
print("\nout_array : ", out_array)

# blue for numpy.cos()
plt.plot(in_array, out_array, color = 'blue', marker = "o")
plt.title("numpy.cos()")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
