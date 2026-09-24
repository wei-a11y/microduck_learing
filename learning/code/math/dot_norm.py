import numpy as np

x = np.array([1.0, 2.0, 3.0])
y = np.array([4.0, 5.0, 6.0])

#dot product
dot = x @ y
print("x dot y =", dot)

#L2 norm
norm_x = np.linalg.norm(x)
print("||x|| =", norm_x)

#squared norm
squared_norm = x @ x
print("||x||^2 =", squared_norm)
print("norm squared =", norm_x ** 2)