import numpy as np
import random

class RandomAgent():
	def __init__(self,action_space):
		self.action_space = action_space
	
	def choose_action(self,observation):
		##Todo: Returns a random choice of the available actions
		return random.choice(self.action_space)