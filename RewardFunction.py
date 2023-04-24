"""
Here we keep track of the rewards for each cell. 
This module interacts with the Table Modules. 
"""

# getReward returns the reward for a given cell
def calculateReward(cell):
  reward = 0
  match cell:
    case 'pickup':
      reward = 14
    case 'dropoff':
      reward = 14
    case 'normal':
      reward = -1
    case 'risky':
      reward = -2
    
  return reward