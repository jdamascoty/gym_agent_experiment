import gym
from gym import error, spaces, utils
from gym.utils import seeding

class agentExperimentEnv(gym.Env):
  metadata = {'render.modes': ['human']} 

  def __init__(self):
  	self.c1_placement = 0
  	self.c1_tireWear = 5
  	self.c2_placement = 0
  	self.c2_tireWear = 5
  	self.max_placement = 10
  	self.action_space = ["F1", "F2", "CT"]
  	self.possibleActions = {"F1": [1, 1], "F2": [2, 3], "CT": [0, 5]} # [0] - Movement, [1] - Tire Wear
  	self.reward = 0
  	self.isDone = False

  def step(self, action):
    #isInMaxPlacement(self.c2_placement): stop the episode
    if self.c1_tireWear == 0 or (self.c1_tireWear < 3 and action == "F2") :
    	action = "CT"

    resultingState = self.possibleActions[action]

    print("Car 1 Action: ", action)
    if resultingState[0] == 1:
    	self.c1_placement = agentExperimentEnv.moveForward(self, self.c1_placement, resultingState[0])
    	self.c1_tireWear = agentExperimentEnv.decrementTireWear(self, self.c1_tireWear, resultingState[1])
    elif resultingState[0] == 2:
    	self.c1_placement = agentExperimentEnv.moveForward(self, self.c1_placement, resultingState[0])
    	self.c1_tireWear = agentExperimentEnv.decrementTireWear(self, self.c1_tireWear, resultingState[1])
    elif resultingState[0] == 0:
   		self.c1_tireWear = agentExperimentEnv.resetTireWear(self, self.c1_tireWear)

    c2_tireWear_isWorn = agentExperimentEnv.isWorn(self, self.c2_tireWear)
    
    if c2_tireWear_isWorn: #change tire AND resetTireWear
       self.c2_tireWear = agentExperimentEnv.resetTireWear(self, self.c2_tireWear)
    if not c2_tireWear_isWorn: #move forward AND decrementTireWear
       self.c2_placement = agentExperimentEnv.moveForward(self, self.c2_placement, 1) 
       self.c2_tireWear = agentExperimentEnv.decrementTireWear(self, self.c2_tireWear, 1)

    reward = agentExperimentEnv.determineReward(self, self.c1_placement, self.c2_placement)
    isDone = agentExperimentEnv.isDone(self, self.c1_placement, self.c2_placement)

    return reward, isDone

  def isDone(self, c1_placement, c2_placement):
  	if c1_placement >= 10 or c2_placement >= 10:
  		return True
  	else:
  		return False

  def determineReward(self, c1_placement, c2_placement):
  	if c1_placement < c2_placement:
  		reward = c1_placement - c2_placement
  	elif c1_placement > c2_placement:
  		reward = 2*(c1_placement - c2_placement)
  	else:
  		reward = 0

  	return reward
    
  def isWorn(self, tireWear):
    if tireWear <= 0:
      return True
    else:
      return False
    
  def resetTireWear(self, tireWear):
    tireWear = 5
    return tireWear
    
  def decrementTireWear(self, tireWear, amountOfWear):
    tireWear -= amountOfWear
    return tireWear
  
  def isInMaxPlacement(self, placement):
    if placement == self.max_placement:
      return True
    else:
      return False
  
  def moveForward(self, placement, distance):
    placement += distance
    return placement
    
  def reset(self):
  	self.c1_placement = 0
  	self.c1_tireWear = 5
  	self.c2_placement = 0
  	self.c2_tireWear = 5
  	self.reward = 0
  	self.isDone = False
    
  def render(self, mode='human'):
    print("Car 1 placement: " , self.c1_placement, "Car 1 tire wear: " , self.c1_tireWear)
    print("Car 2 placement: " , self.c2_placement, "Car 2 tire wear: " , self.c2_tireWear)
 