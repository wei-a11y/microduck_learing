import numpy as np
theta = np.array([5.0,5.0])
learning_rate = 0.1

for step in range(20):
    x, y =theta
    loss = x**2 + 3 * y**2
    gradient = np.array(
            [
                2 * x,
                6 * y,
                ])
    theta = theta - learning_rate * gradient
    print(
            f"step={step:02d}, "
            f"theta={theta}, "
            f"loss={loss:.6f}, "
            f"gradient={gradient}"
            )
