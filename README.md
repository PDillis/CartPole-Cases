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

![figure_1](https://user-images.githubusercontent.com/24496178/30891060-1afe1186-a331-11e7-8171-ffa6c731fc52.png)

A more clearer picture is seen when we compute to what mean reward every controller tends to (akin to how we usually visualize the Law of Large Numbers, i.e., take increasingly larger samples of our episode runs and compute the mean of these samples). Thus, we see the following:

![figure_1-2](https://user-images.githubusercontent.com/24496178/30891074-29ccae70-a331-11e7-9a3f-6d7684e25446.png)

Finally, wondering about stability for each controller (and more importantly, confirming that the name for 'Unstable Controller' is actually warranted), we calculate the variance of the same samples used in the last plot. We obtain the following:

![figure_1-4](https://user-images.githubusercontent.com/24496178/30891083-34d2cfa2-a331-11e7-9762-4137cf8daa66.png)

We resume the final (approximate) mean reward and variance in reward each controller obtains after 1000 episodes, in the following table: 


|      Controller      | Final Mean Reward | Final Variance |
| :------------------: | :---------------: | :------------: |
|     Random Agent     |        23         |       125      |
|     Pole Control     |        26         |       15       |
|    Speed Control     |        40         |       280      |
|   Unstable Control   |        42         |       75       |
| Speed + Pole Control |        200        |        1       |

Thus, we can conclude that, while controlling the horizontal speed of the cart brings a greater increase in reward per episode than just controlling the angle of the pole w.r.t. the vertical, the former is far more unstable than the latter, as we can see in the final plot. The Speed Control controller, however, has an exceedingly high variance, even higher than the Random Agent. 

Of course, a former statistical analysis is warranted here, but it is beyond the scope of the objective of this small project, which is to illustrate how incredibly hard it is to finetune each and every observation in order to obtain the highest reward. Indeed, it was through mere luck that we chose the two observations that, when controlled at the same time, yield the highest reward possible in the environment. Perhaps this was done through intuition, but still this will not be feasible when the observation (or state) of our agent has hundreds, thousands, millions or more parameters.
