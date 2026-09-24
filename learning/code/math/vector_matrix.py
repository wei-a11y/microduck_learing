import numpy as np

#3D vector
x = np.array([1.0, 2.0, 3.0])

print("x =", x)
print("x shape =", x.shape)

# 2x3 matrix
A = np.array([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0]
])

print("A =")
print(A)
print("A shape =", A.shape)

# matrix-vector multiplication
y = A @ x

print("y =", y)
print("y shape =", y.shape)

observation = np.zeros(61)

w = np.random.randn(256, 61)

hidden = w @ observation

print("observation:", observation.shape)
print("w:", w.shape)
print("hidden:", hidden.shape)

w2 = np.random.randn(14, 256)
action = w2 @ hidden
print("action:", action.shape)