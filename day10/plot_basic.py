import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100)
y = np.sin(x)
f = np.cos(x)

fig, ax = plt.subplots(figsize=(10,4))

ax.plot(x,y,color = "blue",linewidth = 2,label = "sin")
ax.plot(x,f,color = "red",linewidth = 3,label = "cos")
ax.set_title("sine wave")
ax.set_xlabel("x")
ax.set_ylabel("sin(x) and cos(x)")
ax.legend()

plt.savefig("sin_cos.png",dpi = 150)
plt.show()
