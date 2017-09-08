import gym
from gym import wrappers

env=gym.make('CartPole-v0')
env=wrappers.Monitor(env, '/tmp/cartpole-exp-1',force=True)

#Run for 100 episodes
for i_episode in range(100):
	# Get the initial observation
	observation = env.reset()
	# Run for at most 1000 time steps
	for t in range(1000):
		# Choose actions depending on the state of the cartpole:
		# if it is traveling to the right, try to stop it by going to the left
		if observation[1] > 0:
			action = 0
		# if traveling to the left, try to stop it by going to the right
		if observation[1] < 0:
			action = 1
		# if the pole is falling to the right, try to stop it by going to the right
		if observation[2]>0.025:
			action = 1
		# if the pole is falling to the left, try to stop it by going to the left
		if observation[2]<-0.025:
			action = 0
		# perform the action and obtain new o, r, done, info
		observation, reward, done, info = env.step(action)
		if done:
			break

gym.upload('/tmp/cartpole-exp-1', api_key='sk_zuH9mPQ1RVavSFr9VT7JOQ')

env.close()
