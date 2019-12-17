# Gym Agent Experiment

This is a test environment created for OpenAI Gym that is created to practice creating OpenAI environments and, eventually, agents. This is used to learn reinforcement learning for future projects.

### Environment
The environment includes 2 cars racing. The first car (c1) is the agent that reinforcement learning will be applied to. The second car (c2) is a static agent that moves forward incrementally. The map used is a straight line with no pitstops. The placement of each car is indicated by an integer.

### Agent Actions
The agents can move:
 * 1 increment forward
 * 2 increments forward
 * Change tire (no increments forward, but resets tire wear)
 
 ### Agent Variables
 * Car placement: indicates placement of car.
 * Tire wear: indicates wear of tire. If tire wear is 0, the agent cannot move forward.
 
 ### Reward System
 * Positive: Each number of placements in front of the static car
 * Negative: Each number of placements behind the static car
