import gym
from gym import error, spaces, utils
from gym.utils import seeding

class agentExperimentEnv(gym.Env):
  metadata = {'render.modes': ['human']} 

  def __init__(self):
    self.c2_placement = 0
    self.c2_tireWear = 5
    self.max_placement = 10
    
  def step(self, action):
    #isInMaxPlacement(self.c2_placement): stop the episode
    
    if isWorn(self.c2_tireWear): #change tire AND resetTireWear
       self.c2_tireWear = resetTireWear(self.c2_tireWear)
    if not isWorn(self.c2_tireWear): #move forward AND decrementTireWear
       self.c2_placement = moveForward(self.c2_placement) 
       self.c2_tireWear = decrementTireWear(self.c2_tireWear)
    
  def isWorn(self, tireWear):
    if tireWear <= 0:
      return True
    else:
      return False
    
  def resetTireWear(self, tireWear):
    tireWear = 5
    return tireWear
    
  def decrementTireWear(self, tireWear):
    tireWear -= 1
    return tireWear
  
  def isInMaxPlacement(self, placement):
    if placement == self.max_placement:
      return True
    else:
      return False
  
  def moveForward(self, placement):
    placement += 1
    return placement
    
  def reset(self):
    self.c2_placement = 0
    self.c2_tireWear = 5
    
  def render(self, mode='human'):
    print("Car 2 placement: " , c2_placement)
    print("Car 2 tire wear: " , c2_tireWear)
    
  #def isEpisodeDone(self):
    
    
