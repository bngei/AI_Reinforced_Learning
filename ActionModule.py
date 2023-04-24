"""
Here we find the possible moves the agents can make. 
The functions take care of this by checking where the first agent is relative 
to the second agent and if the agent is within bounds of the environment. 
This is where our main 2 constraints are. This module works with the Environment Module.
"""
# returnPossibleActions returns a list of the possible moves an agent can make
def returnAction(state, agent):
  actions = ['up', 'down', 'west', 'east', 'north', 'south']
  firstAgentLocation = []
  secondAgentLocation = []

  if agent == 'f':
    firstAgentLocation = state.representation['femalePosition']['coordinates']
    secondAgentLocation = state.representation['malePosition']['coordinates']
  else:
    firstAgentLocation = state.representation['malePosition']['coordinates']
    secondAgentLocation = state.representation['femalePosition']['coordinates']
  
  if firstAgentLocation[0] - secondAgentLocation[0] == -1 and (firstAgentLocation[1] == secondAgentLocation[1] and firstAgentLocation[2] == secondAgentLocation[2]):
    if actions.count('up'):
      actions.remove('up')
  elif firstAgentLocation[1] - secondAgentLocation[1] == -1 and (firstAgentLocation[0] == secondAgentLocation[0] and firstAgentLocation[2] == secondAgentLocation[2]):
    if actions.count('south'):
      actions.remove('south')
  elif firstAgentLocation[2] - secondAgentLocation[2] == -1 and (firstAgentLocation[0] == secondAgentLocation[0] and firstAgentLocation[1] == secondAgentLocation[1]):
    if actions.count('east'):
      actions.remove('east')
  elif firstAgentLocation[0] - secondAgentLocation[0] == 1 and (firstAgentLocation[1] == secondAgentLocation[1] and firstAgentLocation[2] == secondAgentLocation[2]):
    if actions.count('down'):
      actions.remove('down')
  elif firstAgentLocation[2] - secondAgentLocation[2] == 1 and (firstAgentLocation[0] == secondAgentLocation[0] and firstAgentLocation[1] == secondAgentLocation[1]):
    if actions.count('west'):
      actions.remove('west')
  elif firstAgentLocation[1] - secondAgentLocation[1] == 1 and (firstAgentLocation[0] == secondAgentLocation[0] and firstAgentLocation[2] == secondAgentLocation[2]):
    if actions.count('north'):
      actions.remove('north')
  
  if firstAgentLocation[0] == 0:
    if actions.count('down'):
      actions.remove('down')
  elif firstAgentLocation[0] == 2:
    if actions.count('up'):
      actions.remove('up')
  if firstAgentLocation[1] == 0:
    if actions.count('north'):
      actions.remove('north')
  elif firstAgentLocation[1] == 2:
    if actions.count('south'):
      actions.remove('south')
  if firstAgentLocation[2] == 0:
    if actions.count('west'):
      actions.remove('west')
  elif firstAgentLocation[2] == 2:
    if actions.count('east'):
      actions.remove('east')
  
  return actions


# findNextPositionPossibleActions returns a list of the possible moves an agent can make in the next position
def findNextPositionPossibleActions(coordinates):
  actions = ['up', 'down', 'west', 'east', 'north', 'south']
  if coordinates[0] == 0:
    if actions.count('down'):
      actions.remove('down')
  elif coordinates[0] == 2:
    if actions.count('up'):
      actions.remove('up')
  if coordinates[1] == 0:
    if actions.count('north'):
      actions.remove('north')
  elif coordinates[1] == 2:
    if actions.count('south'):
      actions.remove('south')
  if coordinates[2] == 0:
    if actions.count('west'):
      actions.remove('west')
  elif coordinates[2] == 2:
    if actions.count('east'):
      actions.remove('east')
  return actions