# Robot Control & Reinforcement Learning Roadmap

## 1. Overall Goal

学习周期：

- Start: 2026-09-14
- End: 2026-10-31
- Internship applications begin: 2026-11

目标岗位：

- 机器人强化学习实习生
- 机器人 ROS / 运动控制实习生
- 强化学习运动控制 / Locomotion / Sim2Real 相关岗位

预计总学习时间：

- 普通学习日：约 3 h/day
- 中秋、国庆共约 10 天：8–10 h/day
- 总预算：约 190–210 h

---

# 2. Final Target

到 2026-10-31，应能够：

## Reinforcement Learning

- 理解 MDP、Return、Value、Q、Advantage
- 理解 Policy Gradient
- 理解 Actor-Critic
- 理解 GAE 的作用
- 重点掌握 PPO
- 能解释 PPO ratio 和 clipping
- 理解 On-policy / Off-policy
- 理解 PPO、SAC、DDPG、TD3 的主要区别

## Deep Learning

- 熟悉 PyTorch 基础
- 理解 MLP
- 理解 forward / backward
- 理解 gradient descent
- 理解常见 optimizer
- 能阅读机器人 RL policy 网络

## Robot Control

- 理解 State Space 基础
- 重新理解 LQR
- 理解机器人运动学基础
- 理解 Jacobian
- 理解机器人动力学方程

  M(q)q_ddot + C(q,q_dot)q_dot + g(q) = tau

- 理解 Joint PD
- 理解 Gravity Compensation
- 理解 Computed Torque
- 初步理解 Impedance Control

## Robot RL

- 能解释 observation / action / reward
- 能解释 locomotion RL 基本训练流程
- 能修改 reward
- 能开展 reward ablation
- 理解 domain randomization
- 理解 actuator model
- 理解 backlash
- 理解 Sim2Real gap

## Microduck

完成：

- Microduck RL 环境部署
- PPO locomotion baseline
- Policy playback
- ONNX export
- CPU inference
- Reward experiment
- Domain randomization experiment
- Actuator / Backlash experiment
- 实验结果分析

可选：

- Microduck 实机部署

---

# 3. Stage Definition

---

# Stage 0 — Project Initialization & Baseline

## Date

2026-09-14 ~ 2026-09-15

## Time Budget

约 6 h

## Goal

建立学习系统，并确认 Microduck 项目的基本软硬件环境。

## Tasks

### Project Management

- [ ] 创建 `learning/`
- [ ] 创建 `learning/AGENTS.md`
- [ ] 创建 `ROADMAP.md`
- [ ] 创建 `PROGRESS.md`
- [ ] 创建 `KNOWLEDGE_CHECKLIST.md`
- [ ] 创建 `EXPERIMENTS.md`

### Development Environment

确认：

- [ ] Ubuntu 正常
- [ ] NVIDIA Driver 正常
- [ ] `nvidia-smi` 正常
- [ ] Python / uv 可用
- [ ] Git 正常

### Microduck

- [ ] 阅读仓库根目录 `AGENTS.md`
- [ ] 阅读 `README.md`
- [ ] 确认 Microduck RL 的主要目录结构
- [ ] 理解训练环境的大致入口

## Expected Result

能够说明：

Microduck RL 的代码在哪里，
训练入口在哪里，
官方 AGENTS.md 与 learning/AGENTS.md 分别负责什么。

## Gate

必须能够回答：

1. 当前项目最终目标是什么？
2. 两个月为什么选择 Microduck 作为主项目？
3. 根目录 AGENTS.md 与 learning/AGENTS.md 有什么区别？
4. Microduck RL 使用什么模拟器？
5. 当前 NVIDIA / CUDA 环境是否正常？

通过后进入 Stage 1。

---

# Stage 1 — Minimum Mathematics for Control & RL

## Date

2026-09-16 ~ 2026-09-22

## Time Budget

约 21 h

## Goal

补齐理解神经网络、LQR、PPO 所需要的最低数学基础。

## Linear Algebra

学习：

- [ ] Scalar
- [ ] Vector
- [ ] Matrix
- [ ] Vector dimension
- [ ] Matrix dimension
- [ ] Matrix multiplication
- [ ] Transpose
- [ ] Dot product
- [ ] Norm
- [ ] Linear transformation

了解：

- [ ] Rank
- [ ] Eigenvalue
- [ ] Eigenvector
- [ ] Positive definite matrix

## Calculus

学习：

- [ ] Function
- [ ] Derivative
- [ ] Partial derivative
- [ ] Gradient
- [ ] Chain rule

了解：

- [ ] Multivariable function

## Probability

学习：

- [ ] Random variable
- [ ] Probability distribution
- [ ] Expectation
- [ ] Variance
- [ ] Gaussian distribution
- [ ] Sampling

## Practice

Python / NumPy：

- [ ] 创建向量和矩阵
- [ ] 实现矩阵乘法
- [ ] 计算 dot product
- [ ] 计算 norm
- [ ] 实现简单 gradient descent

## Robot Connection

能够理解：

- q ∈ R^14
- observation ∈ R^61
- x^T Q x
- y = Wx + b
- ||x - x_target||²
- ∂J / ∂θ

## Expected Ability

可以看到基本矩阵、梯度和概率公式而不产生阅读障碍。

## Gate

闭卷解释：

1. 向量和矩阵有什么区别？
2. `Wx+b` 在神经网络中意味着什么？
3. Dot product 是什么？
4. L2 norm 是什么？
5. 偏导和梯度是什么关系？
6. Chain rule 为什么与反向传播有关？
7. Expectation 是什么？
8. Gaussian distribution 为什么会用于连续动作策略？

实践：

- [ ] 自己写一个简单 gradient descent 示例
- [ ] 能判断常见矩阵表达式的维度

通过后进入 Stage 2。

---

# Stage 2 — Neural Networks & PyTorch

## Date

2026-09-23 ~ 2026-09-27

## Time Budget

约 30 h
（包含中秋集中学习时间）

## Goal

能够阅读和理解 RL 中使用的 MLP policy。

## Theory

学习：

- [ ] Neuron
- [ ] Linear layer
- [ ] Activation
- [ ] ReLU
- [ ] Tanh
- [ ] MLP
- [ ] Loss
- [ ] Gradient descent
- [ ] Backpropagation
- [ ] Batch
- [ ] Epoch
- [ ] Adam

## PyTorch

掌握：

- [ ] Tensor
- [ ] tensor shape
- [ ] `nn.Module`
- [ ] `nn.Linear`
- [ ] forward
- [ ] loss
- [ ] `loss.backward()`
- [ ] optimizer
- [ ] `optimizer.step()`
- [ ] save / load

## Practice

完成：

- [ ] 使用 PyTorch 拟合简单函数
- [ ] 自己构建一个 MLP
- [ ] 绘制训练 loss

## Robot Connection

理解：

observation
→ MLP
→ action

能够解释类似：

61
→ 256
→ 256
→ 14

代表什么。

## Gate

必须能够：

1. 用自己的话解释 MLP
2. 解释 forward
3. 解释 backward
4. 解释 optimizer 的作用
5. 解释为什么神经网络本质包含大量矩阵运算
6. 写一个简单 PyTorch MLP

通过后进入 Stage 3。

---

# Stage 3 — RL Fundamentals & Policy Gradient

## Date

2026-09-28 ~ 2026-10-03

## Time Budget

约 35 h

## Goal

理解 PPO 之前必须掌握的 RL 基础。

## RL Fundamentals

学习：

- [ ] Agent
- [ ] Environment
- [ ] State
- [ ] Observation
- [ ] Action
- [ ] Reward
- [ ] Transition
- [ ] Episode
- [ ] MDP
- [ ] Discount factor
- [ ] Return

## Value Functions

学习：

- [ ] V(s)
- [ ] Q(s,a)
- [ ] Bellman equation

## Policy

学习：

- [ ] Deterministic policy
- [ ] Stochastic policy
- [ ] Gaussian policy
- [ ] log probability

## Policy Gradient

理解：

- [ ] Objective J(θ)
- [ ] Policy Gradient 的基本思想
- [ ] 为什么提高好动作的概率
- [ ] 为什么降低坏动作的概率

## Actor-Critic

学习：

- [ ] Actor
- [ ] Critic
- [ ] Advantage
- [ ] Baseline
- [ ] GAE 基本思想

## Gate

必须能够解释：

1. MDP 是什么？
2. State 与 Observation 有什么区别？
3. Return 是什么？
4. γ 有什么作用？
5. V 和 Q 的区别？
6. Policy 是什么？
7. Actor 与 Critic 分别做什么？
8. Advantage 是什么？
9. 为什么 Policy Gradient 可以学习动作？

通过后进入 Stage 4。

---

# Stage 4 — PPO & Microduck Baseline

## Date

2026-10-04 ~ 2026-10-10

## Time Budget

约 45 h
（国庆集中学习阶段）

## Goal

理解 PPO，并完成 Microduck PPO locomotion baseline。

## PPO Theory

学习：

- [ ] Old policy / New policy
- [ ] Probability ratio
- [ ] PPO surrogate objective
- [ ] Clipping
- [ ] Entropy
- [ ] Value loss
- [ ] On-policy
- [ ] Mini-batch update

重点理解：

r_t(θ)

以及：

PPO clipped objective

## Microduck Code

阅读：

- [ ] robot constants
- [ ] environment config
- [ ] observation
- [ ] action
- [ ] command
- [ ] reward
- [ ] termination
- [ ] event
- [ ] actuator

画出：

command
→ observation
→ actor
→ action
→ actuator
→ MuJoCo
→ new state
→ reward
→ PPO update

## Training

完成：

- [ ] smoke test
- [ ] baseline training
- [ ] training curve observation
- [ ] policy playback
- [ ] ONNX export
- [ ] CPU inference

## Expected Result

拥有第一个完整 Microduck PPO locomotion demo。

## Gate

必须能够脱稿回答：

1. PPO 为什么属于 On-policy？
2. Probability ratio 是什么？
3. Clip 为什么存在？
4. Advantage 在 PPO 中做什么？
5. Critic 为什么必要？
6. Microduck observation 是什么？
7. Microduck action 是什么？
8. RL 输出是否直接等于电机 torque？
9. PPO 在整个训练链条中的位置是什么？

实践：

- [ ] baseline 能成功训练
- [ ] 能成功播放策略
- [ ] 能成功导出 ONNX

---

# Stage 5 — Reward Engineering & Locomotion Experiments

## Date

2026-10-11 ~ 2026-10-17

## Time Budget

约 21 h

## Goal

从“能训练”进入“能做实验”。

## Reward Analysis

整理所有主要 reward：

- [ ] velocity tracking
- [ ] angular velocity
- [ ] orientation
- [ ] joint related penalty
- [ ] action rate
- [ ] contact
- [ ] energy / torque related terms

## Experiments

至少完成：

### EXP-001

Baseline

### EXP-002

修改 velocity tracking reward

### EXP-003

修改 action rate penalty

### EXP-004

修改姿态或稳定性相关 reward

## 每个实验记录

- Hypothesis
- Modification
- Config
- Result
- Behavior
- Analysis
- Conclusion

## Concepts

理解：

- [ ] Reward shaping
- [ ] Reward tradeoff
- [ ] Reward hacking
- [ ] Ablation study

## Gate

必须能够：

1. 解释一个 locomotion reward 的组成
2. 预测某个 reward weight 增大后的潜在影响
3. 比较 baseline 与 modified policy
4. 根据行为和训练曲线分析结果
5. 解释为什么 reward 更高不一定意味着行为更好

---

# Stage 6 — Sim2Real + Robot Control Fundamentals

## Date

2026-10-18 ~ 2026-10-24

## Time Budget

约 21 h

## Goal

理解机器人 RL 与真实机器人控制之间的关系。

## Sim2Real

学习：

- [ ] Sim2Real gap
- [ ] Domain Randomization
- [ ] Actuator model
- [ ] Friction
- [ ] Mass variation
- [ ] Delay
- [ ] Noise
- [ ] Backlash
- [ ] Battery / actuator variation

## Experiments

完成：

- [ ] DR ON vs OFF
- [ ] ideal actuator vs realistic actuator
- [ ] normal vs backlash

## Control Theory

复习：

- [ ] State Space
- [ ] Controllability
- [ ] Observability
- [ ] State feedback
- [ ] LQR

理解：

- [ ] Forward Kinematics
- [ ] Inverse Kinematics
- [ ] Jacobian

机器人动力学：

- [ ] M(q)
- [ ] C(q,q_dot)
- [ ] g(q)
- [ ] tau

控制器：

- [ ] Joint PD
- [ ] Gravity Compensation
- [ ] Computed Torque
- [ ] Impedance Control 基础

## Optional Mini Project

2-DOF arm:

- [ ] PD
- [ ] PD + gravity compensation
- [ ] Computed Torque

## Gate

必须能够解释：

1. LQR 与 PPO 的区别
2. Model-based 与 Model-free 的区别
3. Sim2Real gap 的主要来源
4. Domain Randomization 为什么有效
5. Actuator model 为什么重要
6. Backlash 是什么
7. 机器人动力学方程每一项的意义
8. PD 与 Computed Torque 的区别

---

# Stage 7 — Algorithm Comparison & Job Preparation

## Date

2026-10-25 ~ 2026-10-31

## Time Budget

约 20 h

## Goal

完成岗位要求补缺、项目包装和面试准备。

## Additional RL Algorithms

理解：

- [ ] DDPG
- [ ] TD3
- [ ] SAC

重点比较：

- [ ] On-policy vs Off-policy
- [ ] Model-free vs Model-based
- [ ] Replay Buffer
- [ ] Deterministic policy
- [ ] Stochastic policy
- [ ] Sample efficiency

不要求完整实现。

## Isaac

至少：

- [ ] 了解 Isaac Sim / Isaac Lab
- [ ] 跑通一个官方 RL demo
- [ ] 理解其大规模并行环境结构

不要求移植 Microduck。

## Project Documentation

完成：

- [ ] Microduck project README
- [ ] Architecture diagram
- [ ] Reward table
- [ ] Experiment table
- [ ] Training curves
- [ ] Demo video / GIF
- [ ] Sim2Real analysis

## Resume

完成：

- [ ] Microduck 项目描述
- [ ] ROS2 / 路径规划经历整理
- [ ] LQR 经历整理
- [ ] 技术栈整理

## Interview

至少能够回答：

- [ ] MDP
- [ ] V / Q
- [ ] Actor-Critic
- [ ] Advantage
- [ ] GAE
- [ ] PPO Clip
- [ ] PPO vs SAC
- [ ] DDPG vs TD3
- [ ] Reward design
- [ ] Domain Randomization
- [ ] Sim2Real
- [ ] Actuator model
- [ ] LQR vs PPO
- [ ] Robot dynamics
- [ ] Joint PD
- [ ] Impedance control

## Final Gate

完成一次模拟面试。

要求：

- PPO 可连续讲解 5–10 分钟
- Microduck 项目可连续讲解 10–15 分钟
- 能回答实验结果的追问
- 能解释失败实验
- 能解释项目中至少一个技术 tradeoff

---

# 4. Priority Rules

如果进度落后，优先级：

1. PPO / RL fundamentals
2. Microduck baseline
3. Reward experiments
4. Sim2Real experiments
5. Robot control fundamentals
6. SAC / TD3 / DDPG
7. Isaac
8. Real robot deployment

禁止为了完成 optional 内容牺牲核心任务。

---

# 5. Real Robot Deployment

实机部署属于 Optional。

只有满足以下条件后再考虑：

- [ ] Microduck baseline 完成
- [ ] Reward experiment 完成
- [ ] Domain Randomization experiment 完成
- [ ] Backlash / actuator experiment 完成
- [ ] ONNX inference 完成
- [ ] 项目文档基本完成

如果在 2026-10-20 前完成以上项目，则考虑真实 Microduck 部署。

否则实机推迟到投递开始后继续。

---

# 6. Definition of Done

任何知识点不能因为“看过视频”而标记完成。

至少满足：

1. 能自己解释
2. 能回答基本追问
3. 能进行简单计算或编程
4. 知道它在机器人中的应用

Microduck 相关知识还需满足：

5. 能指出代码位置或数据流

实验完成必须存在：

- Hypothesis
- Config
- Result
- Analysis
- Conclusion

# Completed

## Stage 0&1 Completed

Date:
2026-09-28

Completed:
- Linear algebra basics
- LQR mathematical connection
- Derivative
- Gradient
- Chain rule
- Probability basics
- Gaussian policy basics

Next:
Stage 2 Neural Network & PyTorch