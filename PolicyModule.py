import random

# pRandom returns a random action unless an agent is next to a pickup or dropoff cell
def pRandom(carrying, cells):
  for i in cells: 
    if (cells[i]['type']=="pickup" and carrying == False) or (cells[i]['type']=="dropoff" and carrying):
      return i
  position = random.randint(0, len(cells) - 1)
  action = (list(cells))[position]
  return action


# pGreedy returns the action with the highest Q-value unless an agent is next to a pickup or dropoff cell
def pGreedy(carrying, cells, qValues):
  maxQValues = float('-inf')
  maxActions = []
  for i in cells: 
    if (cells[i]['type']=="pickup" and carrying == False) or (cells[i]['type']=="dropoff" and carrying):
      return i
  for i in qValues:
    if (qValues[i] > maxQValues):
      maxActions.clear()
      maxQValues = qValues[i]
      maxActions.append(i)
    elif (qValues[i] == maxQValues):
      maxActions.append(i)
  position = random.randint(0, len(maxActions) - 1)
  actionChosen = maxActions[position]
  return actionChosen
    

# pExploit returns a random action with a 20% chance of choosing an action with a lower Q-value unless an agent is next to a pickup or dropoff cell
def pExploit(carrying, cells, qValues):
    maxQValues = float('-inf')
    maxActions = []
    for i in cells: 
      if (cells[i]['type']=="pickup" and carrying == False) or (cells[i]['type']=="dropoff" and carrying):
        return i
    for i in qValues:
      if (qValues[i] > maxQValues):
        maxActions.clear()
        maxQValues = qValues[i]
        maxActions.append(i)
      elif (qValues[i] == maxQValues):
        maxActions.append(i)

    nonMaxActions = []
    for i in cells:
      if (maxActions.count(i) == 0):
        nonMaxActions.append(i)
        
    if len(maxActions) == len(qValues):
      nonMaxActions = maxActions
    elif len(nonMaxActions) == len(qValues):
      maxActions = nonMaxActions
    
    actions = [{'list': 'maxActions'}, {'list': 'nonMaxActions'}]
    weight = [0.80, 0.20]
    choiceMade = random.choices(actions, k = 1, weights = weight)
    actionChosen = ''
    if (choiceMade[0]['list'] == 'maxActions'):
      position = random.randint(0, len(maxActions) - 1)
      actionChosen = maxActions[position]
    else:
      position = random.randint(0, len(nonMaxActions) - 1)
      actionChosen = nonMaxActions[position]
    return actionChosen