
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 10)

y = np.sin(x) 

print(x)
print(y)

plt.xlabel("x")
plt.ylabel("sin(x)")
plt.title("y = sin(x)")
plt.plot(x, y)
