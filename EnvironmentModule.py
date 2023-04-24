"""
 Here we define the environment class which initializes the types of cells, 
 rewards for each cell, position of each agent, and uses a dictionary to create the environment. 
 The moveAgent function performs actions. Before making a move, we also check the type of cell 
 the agent is in (pickup, dropoff) and act accordingly. This interacts with the Agent and State Modules. 
"""

class Environment:
  def __init__(self):
    layerOne = [
      [
        {'type': 'normal', 'occupiedBy': 'f'},
        {'type': 'normal', 'occupiedBy': ''},
        {'type': 'dropoff', 'occupiedBy': '', 'blockCount': 0}
      ],
      [
        {'type': 'normal', 'occupiedBy': ''},
        {'type': 'pickup', 'occupiedBy': '', 'blockCount': 10},
        {'type': 'risky', 'occupiedBy': ''}
      ],
      [
        {'type': 'normal', 'occupiedBy': ''},
        {'type': 'normal', 'occupiedBy': ''},
        {'type': 'normal', 'occupiedBy': ''}
      ]
    ]
    layerTwo = [
      [
        {'type': 'dropoff', 'occupiedBy': '', 'blockCount': 0},
        {'type': 'normal', 'occupiedBy': ''},
        {'type': 'normal', 'occupiedBy': ''}
      ],
      [
        {'type': 'normal', 'occupiedBy': ''},
        {'type': 'risky', 'occupiedBy': ''},
        {'type': 'normal', 'occupiedBy': ''}
      ],
      [
        {'type': 'normal', 'occupiedBy': ''},
        {'type': 'normal', 'occupiedBy': ''},
        {'type': 'pickup', 'occupiedBy': '', 'blockCount': 10}
      ]
    ]
    layerThree = [
      [
        {'type': 'dropoff', 'occupiedBy': '', 'blockCount': 0},
        {'type': 'normal', 'occupiedBy': ''},
        {'type': 'normal', 'occupiedBy': ''}
      ],
      [
        {'type': 'normal', 'occupiedBy': ''},
        {'type': 'normal', 'occupiedBy': ''},
        {'type': 'dropoff', 'occupiedBy': 'm', 'blockCount': 0}
      ],
      [
        {'type': 'normal', 'occupiedBy': ''},
        {'type': 'normal', 'occupiedBy': ''},
        {'type': 'normal', 'occupiedBy': ''}
      ]
    ]
    self.environment = [layerOne, layerTwo, layerThree]
    

  # moveAgent is called by the agent to move the agent
  def moveAgent(self, prevLocation, action, agent, carrying):
    #print('move agent: oldCoordinates ', oldCoordinates, 'action ', action)
    self.environment[prevLocation[0]][prevLocation[1]][prevLocation[2]]['occupiedBy'] = ''
    newLocations = []
    match action:
      case 'up':
        self.environment[prevLocation[0] + 1][prevLocation[1]][prevLocation[2]]['occupiedBy'] = agent
        newLocations = [prevLocation[0] + 1, prevLocation[1], prevLocation[2]]
      case 'down':
        self.environment[prevLocation[0] - 1][prevLocation[1]][prevLocation[2]]['occupiedBy'] = agent
        newLocations = [prevLocation[0] - 1, prevLocation[1], prevLocation[2]]
      case 'south':
        self.environment[prevLocation[0]][prevLocation[1] + 1][prevLocation[2]]['occupiedBy'] = agent
        newLocations = [prevLocation[0], prevLocation[1] + 1, prevLocation[2]]
      case 'north':
        self.environment[prevLocation[0]][prevLocation[1] - 1][prevLocation[2]]['occupiedBy'] = agent
        newLocations = [prevLocation[0], prevLocation[1] - 1, prevLocation[2]]
      case 'east':
        self.environment[prevLocation[0]][prevLocation[1]][prevLocation[2] + 1]['occupiedBy'] = agent
        newLocations = [prevLocation[0], prevLocation[1], prevLocation[2] + 1]
      case 'west':
        self.environment[prevLocation[0]][prevLocation[1]][prevLocation[2] - 1]['occupiedBy'] = agent
        newLocations = [prevLocation[0], prevLocation[1], prevLocation[2] - 1]
    match self.environment[newLocations[0]][newLocations[1]][newLocations[2]]['type']:
      case 'pickup':
        if carrying == False:
          return self.removePUBlock(newLocations)
      case 'dropoff':
        if carrying:
          return self.addDOBlock(newLocations)
      case 'normal':
        return False
      case 'risky':
        return False
        

  # removePUBlock is called by moveAgent to remove a block from a pickup cell
  def removePUBlock(self, location):
    if(self.environment[location[0]][location[1]][location[2]]['blockCount'] > 0):
      self.environment[location[0]][location[1]][location[2]]['blockCount'] -= 1
      return True
    else:
      return False
      

  # addDOBlock is called by moveAgent to add a block to a dropoff cell
  def addDOBlock(self, location):
    if(self.environment[location[0]][location[1]][location[2]]['blockCount'] < 5):
      self.environment[location[0]][location[1]][location[2]]['blockCount'] += 1
      return True
    else:
      return False
      

# getType is called by the agent to get the type of a cell
def getType(env, starting, moves):
  cells = {}
  for i in moves:
    match i:
      case 'up':
        cells[i] = {}
        cells[i]['type'] = env[starting[0] + 1][starting[1]][starting[2]]['type']
        cells[i]['coordinates'] = [starting[0] + 1, starting[1], starting[2]]
      case 'down':
        cells[i] = {}
        cells[i]['type'] = env[starting[0] - 1][starting[1]][starting[2]]['type']
        cells[i]['coordinates'] = [starting[0] - 1, starting[1], starting[2]]
      case 'south':
        cells[i] = {}
        cells[i]['type'] = env[starting[0]][starting[1] + 1][starting[2]]['type']
        cells[i]['coordinates'] = [starting[0], starting[1] + 1, starting[2]]
      case 'north':
        cells[i] = {}
        cells[i]['type'] = env[starting[0]][starting[1] - 1][starting[2]]['type']
        cells[i]['coordinates'] = [starting[0], starting[1] - 1, starting[2]]
      case 'east':
        cells[i] = {}
        cells[i]['type'] = env[starting[0]][starting[1]][starting[2] + 1]['type']
        cells[i]['coordinates'] = [starting[0], starting[1], starting[2] + 1]
      case 'west':
        cells[i] = {}
        cells[i]['type'] = env[starting[0]][starting[1]][starting[2] - 1]['type']
        cells[i]['coordinates'] = [starting[0], starting[1], starting[2] - 1]
    coordinates = cells[i]['coordinates']
    if cells[i]['type'] == 'pickup':
      if env[coordinates[0]][coordinates[1]][coordinates[2]]['blockCount'] > 0:
        cells[i]['isEmpty'] = False
      else:
        cells[i]['isEmpty'] = True
    elif cells[i]['type'] == 'dropoff':
      if env[coordinates[0]][coordinates[1]][coordinates[2]]['blockCount'] < 5:
        cells[i]['isFull'] = False
      else:
        cells[i]['isFull'] = True
  return cells