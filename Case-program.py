import gym
from gym import wrappers

def create_env():
	env=gym.make('CartPole-v0')
	env=wrappers.Monitor(env, '/tmp/cartpole-exp-1',force=True)

def run(num_episodes, t_steps):
	#Run for num_episodes episodes
	for i_episode in range(num_episodes):
		# Get the initial observation
		observation = env.reset()
		# Run for at most t_steps time steps
		for t in range(t_steps):
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

def upload_n_close(key):
	gym.upload('/tmp/cartpole-exp-1', api_key=key)
	env.close()

if __name__ == '__main__:
	create_env()
	run(num_episodes=100, t_steps=1000)
	upload_n_close('sk_zuH9mPQ1RVavSFr9VT7JOQ') # My OpenAI Gym key, change it to your own
