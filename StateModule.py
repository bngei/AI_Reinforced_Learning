"""
 Here we receive info about the environment state and the functions here do things like 
 set the position of the female agent, male agent and check whether the position is a 
 drop off or pickup. We also update the environment state according to whatever move is made. 
 This interacts with the Environment Module. 
"""

import EnvironmentModule

class State:
  def __init__(self, biggerEnv):
    self.biggerEnv = biggerEnv
    self.representation = {'malePosition': {}, 'femalePosition': {}, 'maleCarrying': False, 'femaleCarrying': False, 'pickupCellBlocks': {}, 'dropoffCellBlocks': {}}
    self.setStateEnvironment()
    self.setMalePos()
    self.setFemalePos()
    self.setPUBlocks() #pick up cells
    self.setDOBlocks() #drop off cells
    
  # setStateEnvironment sets the environment of the state
  def setStateEnvironment(self):
    self.environment = self.biggerEnv.environment
  
  # setFemalePos sets the female agent's position in the state
  def setFemalePos(self):
    for x in range(3):
      for y in range(3):
        for z in range(3):
          if self.environment[x][y][z]['occupiedBy'] == 'f':
            self.representation['femalePosition']['coordinates'] = [x, y, z]
            self.representation['femalePosition']['cellType'] = self.environment[x][y][z]['type']
  
  # setMalePos sets the male agent's position in the state
  def setMalePos(self):
    for x in range(3):
      for y in range(3):
        for z in range(3):
          if self.environment[x][y][z]['occupiedBy'] == 'm':
            self.representation['malePosition']['coordinates'] = [x, y, z]
            self.representation['malePosition']['cellType'] = self.environment[x][y][z]['type']
            

            
  # changeFemCarry sets the female agent's carrying status in the state
  def changeFemCarry(self):
    self.representation['femaleCarrying'] = not self.representation['femaleCarrying']
    
  # changeMaleCarry sets the male agent's carrying status in the state
  def changeMaleCarry(self):
    self.representation['maleCarrying'] = not self.representation['maleCarrying']

  # setPUBlocks sets the number of blocks in the pickup cells in the state
  def setPUBlocks(self):
    for x in range(3):
      for y in range(3):
        for z in range(3):
          if self.environment[x][y][z]['type'] == 'pickup':
            self.representation['pickupCellBlocks'][(x, y, z)] = self.environment[x][y][z]['blockCount']
 

  # setDOBlocks sets the number of blocks in the dropoff cells in the state
  def setDOBlocks(self):
    for x in range(3):
      for y in range(3):
        for z in range(3):
          if self.environment[x][y][z]['type'] == 'dropoff':
            self.representation['dropoffCellBlocks'][(x, y, z)] = self.environment[x][y][z]['blockCount']
        
  
  # updateEnvironmentAndState updates the environment and state after an action is taken
  def updateEnvironmentState(self, prevLocation, action, agent, yesCarry, newLocation):
    pickedUpOrDroppedOff = self.biggerEnv.moveAgent(prevLocation, action, agent, yesCarry)
    if agent == 'f':
      self.setFemalePos()
    else:
      self.setMalePos()
    if pickedUpOrDroppedOff:
      if newLocation == 'pickup' and yesCarry == False:
        self.setPUBlocks()
      else:
        self.setDOBlocks()
      if agent == 'm':
        self.changeMaleCarry
      else:
        self.changeFemCarry
    self.setStateEnvironment()
    return pickedUpOrDroppedOff
    

# findPossibleCells returns the possible cells for the agent
def findPotentialCells(state, agent, actions):
  potentialCells = {}
  if agent == 'f':
    potentialCells = EnvironmentModule.getType(state.environment, state.representation['femalePosition']['coordinates'], actions)
  else:
    potentialCells = EnvironmentModule.getType(state.environment, state.representation['malePosition']['coordinates'], actions)

  return potentialCells


# findNextPositionPossibleCells returns the possible cells for the agent in the next position
def findNextPotentialLocation(state, coordinates, actions):
  possibleCells = EnvironmentModule.getType(state.environment, coordinates, actions)
  return possibleCells