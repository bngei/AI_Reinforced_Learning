"""
 Here we define the agent class as well as create and initialize the agents.
We also call functions from the Action, Table, State, Environment, 
and Policy Modules in order to receive the current state, set possible actions,
positions, update policies, and account for pickup/dropoff cells. 

"""


import ActionModule
import StateModule
import PolicyModule

class Agent:
  def __init__(self, type, yesCarry = False):
    self.type = type
    self.yesCarry = yesCarry
  

  # changeCarry switches the carrying state of the agent
  def changeCarry(self):
    self.yesCarry = not self.yesCarry


# setPotentialActions returns a list of possible actions for the agent    
def setPotentialActions(state, agent):
  return ActionModule.returnAction(state, agent)


# getNewCoordinates returns the new coordinates of the agent after taking an action
def getNewCoordinates(state, agent, action):
  newLocation = []
  if agent == 'f':
    prevLocation = state.representation['femalePosition']['coordinates']
  else:
     prevLocation = state.representation['malePosition']['coordinates']
  match action:
    case 'up':
      newLocation = [prevLocation[0] + 1, prevLocation[1], prevLocation[2]]
    case 'down':
      newLocation = [prevLocation[0] - 1, prevLocation[1], prevLocation[2]]
    case 'south':
      newLocation = [prevLocation[0], prevLocation[1] + 1, prevLocation[2]]
    case 'north':
      newLocation = [prevLocation[0], prevLocation[1] - 1, prevLocation[2]]
    case 'east':
      newLocation = [prevLocation[0], prevLocation[1], prevLocation[2] + 1]
    case 'west':
      newLocation = [prevLocation[0], prevLocation[1], prevLocation[2] - 1]
  return newLocation

# setPossibleCells returns a list of possible cells for the agent
def setPossibleCells(world_state, agent, actions):
  return StateModule.findPotentialCells(world_state, agent, actions)

# setNextPositionPossibleActions returns a list of possible actions for the agent in the next position
def setNextPositionPossibleActions(state, agent, move):
  newCoordinates = getNewCoordinates(state, agent, move)
  return ActionModule.findNextPositionPossibleActions(newCoordinates)
  
# setPossibleActionQValues returns a list of the Q values for the agent based on the moves an agent can take
def setPossibleActionQValues(state, agent, table, actions, layer):
  if agent == 'f':
    return table.findQValues(state.representation['femalePosition']['cellType'], actions, layer)
  else:
     return table.findQValues(state.representation['malePosition']['cellType'], actions, layer)
    
# setNextPositionPossibleCells returns a list of possible cells for the agent in the next position
def setNextPositionPossibleCells(world_state, coordinates, actions):
  return StateModule.findNextPotentialLocation(world_state, coordinates, actions)
    
# pickupOrDropoff changes the carrying state of the agent if it is picking up or dropping off an object
def pickupOrDropoff(agent, position):
  if (position == 'pickup' and agent.yesCarry == False) or (position == 'dropoff' and agent.yesCarry == True):
    agent.changeCarry()

# chooseAction returns the action the agent will take based on the chosen policy
def chooseAction(agent, cells, q_vals, chosenPolicy = 'pRandom'):
  match chosenPolicy:
    case 'pRandom':
      return PolicyModule.pRandom(agent.yesCarry, cells)
    case 'pExploit':
      return PolicyModule.pExploit(agent.yesCarry, cells, q_vals)
    case 'pGreedy':
      return PolicyModule.pGreedy(agent.yesCarry, cells, q_vals)
    

# determineFutureCarrying determines if the agent will be carrying an object in the next position
def determineFutureCarrying(agent, cells, action):
  if (cells[action]['type'] == 'pickup' and cells[action]['isEmpty'] == False and agent.yesCarry == False) or (cells[action]['type'] != 'dropoff' and agent.yesCarry):
    return True
  return False