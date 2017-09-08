# CartPole-Cases
We solve the `CartPole-v0 ` environment using two of the values of the observation we receive. We do this as a way to show how this strategy of solving Gym environments, while perfectly logical and basic, will not give us a general result when the action and state spaces grow in complexity.

We started by comparing a random agent with an agent that only controls the horizontal speed, that is:

```python
if observation[1]>0:
  action = 0
if observation[1]<0:
  action = 1
```

While an improvement (from a mean reward of 15 to a mean reward of 40, approximately), this also presented with some stability issues. Mainly, there is no account for what the agent should do if the pole starts to fall to any side. Thus, we introduce the second controller:

```python
if observation[2]>0:
  action = 1
if observation[2]<0:
  action = 0
```

In other words, if the pole starts to fall to the right, then the agent should go to the right, and if the pole starts to fall to the left, then go left. However, this dd not improve that much our results, as we where obtaining only 2 points more for the final reward (in the mean). Thus, inspired by [JueZ's solution](https://gym.openai.com/evaluations/eval_auJ8CEB6RDSNlcWF7tL4Ng), we instead have a small threshold of speed where the agent should not take any action, i.e.:

```python
if observation[2]>0.025:
  action = 1
if observation[2]<-0.025:
  action = 0
```

With this, we find that the agent successfully solves the environment. We then try to add the same type of threshold for the horizontal speed, but found that it is unnecessary as the agent solve the environment with the same amount of mean reward. We try to add controllers on the other elements of the observation tuple, but these are somewhat unnecessary in the end as our agent has already successfully solved the environment.
