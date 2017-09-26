# CartPole-Cases
## Controllers
We solve the `CartPole-v0 ` environment using two of the values of the observation we receive. We do this as a way to show how this strategy of solving Gym environments, while perfectly logical and basic, will not give us a general result when the action and state spaces grow in complexity.

We started by comparing a Random Agent with an agent that only controls the horizontal speed (Speed Control), that is:

```python
if observation[1]>0:
  action = 0
if observation[1]<0:
  action = 1
```

While an improvement (as we will verify in the following section), this also presented us some stability issues. Mainly, there is no account for what the agent should do if the pole starts to fall to any side. Thus, we introduce the second controller for the angle of the pole, Unstable Control:

```python
if observation[2]>0:
  action = 1
if observation[2]<0:
  action = 0
```

In other words, if the pole starts to fall to the right, then the agent should go to the right, and if the pole starts to fall to the left, then go left. However, this dd not improve that much our results, as we where obtaining only 2 points more for the final reward (in the mean). Thus, inspired by [JueZ's solution](https://gym.openai.com/evaluations/eval_auJ8CEB6RDSNlcWF7tL4Ng), we instead have a small threshold of speed where the agent should not take any action, and we name it Pole Control:

```python
if observation[2]>0.025:
  action = 1
if observation[2]<-0.025:
  action = 0
```

Combining our Pole Control with the Speed Control, we obtain a new controller, the Speed + Pole Control. With it, we find that the agent successfully solves the environment. We then try to add the same type of threshold for the horizontal speed, but found that it is unnecessary as the agent solve the environment with the same amount of mean reward. We try to add controllers on the other elements of the observation tuple, but these are somewhat unnecessary in the end as our agent has already successfully solved the environment.

## Results

We store the reward received in each episode by each of our different controllers: the Random Agent, Speed Control, Unstable Control, Pole Control and Speed + Pole Control. We plot this in the following figure:


![figure_1-3](https://user-images.githubusercontent.com/24496178/30865759-c1645ca6-a2d7-11e7-9e00-6547d587364e.png)


A more clearer picture is seen when we compute to what mean reward every controller tends to (akin to how we usually visualize the Law of Large Numbers, i.e., take increasingly larger samples of our episode runs and compute the mean of these samples). Thus, we see the following:


![figure_1-1](https://user-images.githubusercontent.com/24496178/30865711-a306f4f8-a2d7-11e7-8a4a-edda9e7e9991.png)


We resume the final (approximate) mean reward each controller obtains after 1000 episodes, in the following table: 


|      Controller      | Final Mean Reward |
| :------------------: | :---------------: |
|     Random Agent     |        23         | 
|     Pole Control     |        26         |
|    Speed Control     |        40         |
|   Unstable Control   |        42         |
| Speed + Pole Control |        200        |
