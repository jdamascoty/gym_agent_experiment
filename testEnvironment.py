import gym
import numpy as py
env = gym.make('gym_agent_experiment:agent-experiment-v0')

action = 0

for episode in range(10):
	env.reset()
	for x in range(11):
		env.step(action)
		env.render()


