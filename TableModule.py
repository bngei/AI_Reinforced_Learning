"""
Here we create a class that initializes a 4 x 6 x 2 table called Q-table 
and we update it with the Q-values calculated after using a certain 
policy. These functions return the Q-values of the possible moves as 
a list.. This module interacts with the Reward, Value, and Policy Modules. 
"""

import RewardFunction
import ValueFunction
import PolicyModule

class Qtable:
  def __init__(self):
    self.table = {
      'carrying': {
        'normal': {
          'up': 0,
          'down': 0,
          'west': 0,
          'east': 0,
          'north': 0,
          'south': 0
        },
        'risky': {
            'up': 0,
            'down': 0,
            'west': 0,
            'east': 0,
            'north': 0,
            'south': 0
        },
        'pickup': {
            'up': 0,
            'down': 0,
            'west': 0,
            'east': 0,
            'north': 0,
            'south': 0
        },
        'dropoff': {
          'up': 0,
          'down': 0,
          'west': 0,
          'east': 0,
          'north': 0,
          'south': 0
        }
      },
      'notCarrying': {
        'normal': {
          'up': 0,
          'down': 0,
          'west': 0,
          'east': 0,
          'north': 0,
          'south': 0
        },
        'risky': {
            'up': 0,
            'down': 0,
            'west': 0,
            'east': 0,
            'north': 0,
            'south': 0
        },
        'pickup': {
            'up': 0,
            'down': 0,
            'west': 0,
            'east': 0,
            'north': 0,
            'south': 0
        },
        'dropoff': {
          'up': 0,
          'down': 0,
          'west': 0,
          'east': 0,
          'north': 0,
          'south': 0
        }
      }
    }
    
  
  # chooseNewQValue is a function that chooses the new Q value based on the RL method and policy
  def selectNewQValue(self, oldQValues, actionReward, nextQValues, rlMethod, chosenPolicy, carrying, nextPositionCell, alpha, gamma):
    if rlMethod == 'qLearning':
      return round(ValueFunction.qLearningValueFunction(oldQValues, actionReward, nextQValues, alpha, gamma), 2)
    else:
      chosenAction = ''
      match chosenPolicy:
        case 'pRandom':
          chosenAction = PolicyModule.pRandom(carrying, nextPositionCell)
        case 'pExploit':
          chosenAction = PolicyModule.pExploit(carrying, nextPositionCell, nextQValues)
        case 'pGreedy':
          chosenAction = PolicyModule.pGreedy(carrying, nextPositionCell, nextQValues)
      return round(ValueFunction.sarsaValueFunction(oldQValues, actionReward, nextQValues[chosenAction], alpha, gamma), 2)
    

  # changeQTable is a function that updates the Q table based on the RL method and policy
  def changeQTable(self, position, action, layer, nextCell, nextActions, alpha, gamma, rlMethod = 'qLearning', policy = 'pRandom', carrying = False, nextPositionCell = None):
    oldQValues = self.table[layer][position][action]
    actionReward = RewardFunction.calculateReward(position)
    nextQValues = self.findQValues(nextCell, nextActions, layer)
    newQValues = self.selectNewQValue(oldQValues, actionReward, nextQValues, rlMethod, policy, carrying, nextPositionCell, alpha, gamma)
    self.table[layer][position][action] = newQValues


  # findQValues is a function that finds the Q values for a given position and actions
  def findQValues(self, position, actions, carrying):
    qValues = {}
    for direction in actions:
      qValues[direction] = self.table[carrying][position][direction]
    return qValues