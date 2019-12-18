import gym
import numpy as np
from agents import RandomAgent
env = gym.make('gym_agent_experiment:agent-experiment-v0')



agent = RandomAgent(env.action_space)

all_rewards = []

for episode in range(10):
	obs = env.reset()
	print ("NEW RACE", episode)
	while True:
		action = agent.choose_action(obs)
		reward, isDone = env.step(action)
		print("Reward of Car 1: ", reward)
		env.render()

		if isDone:
			print()
			all_rewards.append(reward)
			break

print("Average Reward: ", np.mean(all_rewards))
