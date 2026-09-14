# Knowledge Checklist

Last updated: 2026-09-14

## Rating Standard

能力等级：

- 0：未接触
- 1：看过 / 能识别术语
- 2：能用自己的话解释基本概念
- 3：能计算、写简单代码并解决基础问题
- 4：能用于实际项目，并能回答进一步追问

原则：

- “看过视频”不能作为完成证据。
- “代码成功运行”不能单独作为掌握证据。
- Evidence 应尽量记录可验证成果。
- 与 Microduck 相关的 Level 4 通常要求能够定位源码或解释实际数据流。

---

# 1. Mathematics

| Topic | Target | Current | Evidence |
|---|---:|---:|---|
| Scalar | 3 | 1 | |
| Vector | 3 | 1 | |
| Matrix | 3 | 1 | |
| Matrix multiplication | 3 | 1 | |
| Transpose | 3 | 1 | |
| Dot product | 3 | 0 | |
| Norm | 3 | 0 | |
| Linear transformation | 3 | 0 | |
| Rank | 2 | 0 | |
| Eigenvalue | 3 | 1 | 曾接触 LQR |
| Eigenvector | 3 | 1 | 曾接触 LQR |
| Positive definite matrix | 3 | 1 | 曾接触 LQR |
| Function | 3 | 2 | |
| Derivative | 3 | 2 | |
| Partial derivative | 3 | 1 | |
| Gradient | 4 | 1 | |
| Chain rule | 3 | 1 | |
| Random variable | 3 | 0 | |
| Probability distribution | 3 | 0 | |
| Expectation | 4 | 0 | |
| Variance | 3 | 0 | |
| Gaussian distribution | 3 | 0 | |
| Sampling | 3 | 0 | |

---

# 2. Deep Learning / PyTorch

| Topic | Target | Current | Evidence |
|---|---:|---:|---|
| Tensor | 4 | 0 | |
| Tensor shape | 4 | 0 | |
| Linear layer | 4 | 0 | |
| Activation function | 3 | 0 | |
| ReLU | 3 | 0 | |
| Tanh | 3 | 0 | |
| MLP | 4 | 0 | |
| Loss function | 3 | 0 | |
| Gradient descent | 4 | 1 | |
| Backpropagation | 4 | 0 | |
| Batch | 3 | 0 | |
| Epoch | 3 | 0 | |
| Adam | 3 | 0 | |
| nn.Module | 4 | 0 | |
| forward() | 4 | 0 | |
| loss.backward() | 4 | 0 | |
| optimizer.step() | 4 | 0 | |
| Model save/load | 3 | 0 | |

---

# 3. Reinforcement Learning Fundamentals

| Topic | Target | Current | Evidence |
|---|---:|---:|---|
| Agent | 4 | 1 | |
| Environment | 4 | 1 | |
| State | 4 | 1 | |
| Observation | 4 | 1 | |
| State vs Observation | 4 | 0 | |
| Action | 4 | 1 | |
| Reward | 4 | 1 | |
| Transition | 3 | 0 | |
| Episode | 3 | 0 | |
| MDP | 4 | 0 | |
| Discount factor γ | 4 | 0 | |
| Return | 4 | 0 | |
| Value V(s) | 4 | 0 | |
| Q(s,a) | 4 | 0 | |
| Bellman equation | 3 | 0 | |
| Policy | 4 | 0 | |
| Deterministic policy | 3 | 0 | |
| Stochastic policy | 4 | 0 | |
| Gaussian policy | 4 | 0 | |
| Log probability | 3 | 0 | |

---

# 4. Policy Gradient / PPO

| Topic | Target | Current | Evidence |
|---|---:|---:|---|
| Policy Gradient | 4 | 0 | |
| Objective J(theta) | 4 | 0 | |
| Actor | 4 | 0 | |
| Critic | 4 | 0 | |
| Actor-Critic | 4 | 0 | |
| Advantage | 4 | 0 | |
| Baseline | 3 | 0 | |
| GAE | 3 | 0 | |
| On-policy | 4 | 0 | |
| Off-policy | 3 | 0 | |
| PPO probability ratio | 4 | 0 | |
| PPO clipping | 4 | 0 | |
| PPO surrogate objective | 4 | 0 | |
| Entropy bonus | 3 | 0 | |
| Value loss | 3 | 0 | |
| PPO mini-batch update | 3 | 0 | |

---

# 5. Other RL Algorithms

| Topic | Target | Current | Evidence |
|---|---:|---:|---|
| DDPG | 2 | 0 | |
| TD3 | 2 | 0 | |
| SAC | 3 | 0 | |
| Replay Buffer | 3 | 0 | |
| Model-free RL | 4 | 0 | |
| Model-based RL | 3 | 0 | |
| Sample efficiency | 3 | 0 | |

---

# 6. Classical / Optimal Control

| Topic | Target | Current | Evidence |
|---|---:|---:|---|
| State Space | 4 | 2 | 有 LQR 接触经验 |
| State x | 4 | 2 | |
| A / B matrices | 4 | 2 | |
| Controllability | 3 | 1 | |
| Observability | 3 | 1 | |
| State feedback | 4 | 2 | |
| Pole placement | 3 | 1 | |
| LQR | 4 | 2 | 路径规划实习中调试过 |
| Q / R matrices | 4 | 2 | |
| Riccati equation | 2 | 1 | |
| LQR vs RL | 4 | 0 | |

---

# 7. Robot Kinematics & Dynamics

| Topic | Target | Current | Evidence |
|---|---:|---:|---|
| Joint space | 4 | 1 | |
| Task space | 4 | 1 | |
| Forward Kinematics | 3 | 1 | |
| Inverse Kinematics | 3 | 1 | |
| Jacobian | 4 | 1 | |
| Singularities | 2 | 0 | |
| Robot dynamics equation | 4 | 0 | |
| M(q) | 4 | 0 | |
| C(q,q_dot) | 3 | 0 | |
| g(q) | 4 | 0 | |
| Joint torque τ | 4 | 1 | |

---

# 8. Robot Control

| Topic | Target | Current | Evidence |
|---|---:|---:|---|
| P control | 4 | 2 | |
| PID | 4 | 2 | |
| Joint PD | 4 | 1 | |
| Gravity compensation | 3 | 0 | |
| Computed Torque | 3 | 0 | |
| Inverse Dynamics Control | 3 | 0 | |
| Impedance Control | 3 | 0 | |
| Position control vs Torque control | 4 | 1 | |

---

# 9. Microduck / Robot RL

| Topic | Target | Current | Evidence |
|---|---:|---:|---|
| Repository structure | 4 | 0 | |
| Training entry point | 4 | 0 | |
| Observation structure | 4 | 0 | |
| Action structure | 4 | 0 | |
| Command structure | 4 | 0 | |
| Reward structure | 4 | 0 | |
| Termination | 3 | 0 | |
| Events | 3 | 0 | |
| Actuator model | 4 | 0 | |
| PPO training flow | 4 | 0 | |
| ONNX export | 3 | 0 | |
| CPU inference | 3 | 0 | |
| Reward shaping | 4 | 0 | |
| Reward hacking | 4 | 0 | |
| Ablation experiment | 4 | 0 | |
| Locomotion | 4 | 0 | |

---

# 10. Sim2Real

| Topic | Target | Current | Evidence |
|---|---:|---:|---|
| Sim2Real gap | 4 | 0 | |
| Domain Randomization | 4 | 0 | |
| Friction randomization | 3 | 0 | |
| Mass randomization | 3 | 0 | |
| Sensor noise | 3 | 0 | |
| Control delay | 3 | 0 | |
| Actuator variation | 4 | 0 | |
| Backlash | 4 | 0 | |
| Robustness evaluation | 3 | 0 | |

---

# 11. Tools

| Topic | Target | Current | Evidence |
|---|---:|---:|---|
| Python | 4 | 2 | |
| NumPy | 4 | 2 | |
| PyTorch | 4 | 0 | |
| Git | 4 | 2 | 已使用 branch/commit |
| Linux | 4 | 3 | Ubuntu 使用经验 |
| ROS2 | 4 | 3 | 有项目经验 |
| MuJoCo | 4 | 0 | |
| WandB | 3 | 0 | |
| ONNX | 3 | 0 | |
| Isaac Lab | 2 | 0 | |

---

# 12. Internship Readiness

| Capability | Target | Current | Evidence |
|---|---:|---:|---|
| 5 min explanation of PPO | 4 | 0 | |
| 10 min Microduck project explanation | 4 | 0 | |
| Explain PPO vs SAC | 3 | 0 | |
| Explain LQR vs PPO | 4 | 0 | |
| Explain reward design | 4 | 0 | |
| Explain Sim2Real | 4 | 0 | |
| Explain failed experiment | 4 | 0 | |
| Read unfamiliar RL code | 3 | 0 | |
| Debug training problem | 3 | 0 | |
| Present experiment results | 4 | 0 | |

---

# Evidence Format

推荐使用如下形式记录 Evidence：

- `docs/math/vector.md`
- `docs/rl/ppo.md`
- `EXP-003`
- `commit abc123`
- `baseline locomotion training completed`
- `Passed Stage 4 verbal gate`
- `Implemented PyTorch MLP without copying tutorial`

不要只写：

- “学过”
- “看过”
- “懂了”