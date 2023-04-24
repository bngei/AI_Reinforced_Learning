import EnvironmentModule
import StateModule
import AgentModule
import TableModule

# experiment1 runs the first experiment
def experiment1(rlMethod, policy1, policy2, env, worldState, qTable, maleAgent, femaleAgent, alpha, gamma):
  for i in range(10000):
    chosenPolicy = ''
    chosenAgent = None
    if i < 500:
      chosenPolicy = policy1
    else:
      chosenPolicy = policy2
    if i % 2 != 0:
      chosenAgent = maleAgent
    else:
      chosenAgent = femaleAgent
    layer = ''
    match chosenAgent.yesCarry:
      case True:
        layer = 'carrying'
      case False:
        layer = 'notCarrying'
    actions = AgentModule.setPotentialActions(worldState, chosenAgent.type)
    cells = AgentModule.setPossibleCells(worldState, chosenAgent.type, actions)
    qValues = AgentModule.setPossibleActionQValues(worldState, chosenAgent.type, qTable, actions, layer)
    chosenAction = AgentModule.chooseAction(chosenAgent, cells, qValues, chosenPolicy)
    nextPositionActions = AgentModule.setNextPositionPossibleActions(worldState, chosenAgent.type, chosenAction)
    nextPositionCells = AgentModule.setNextPositionPossibleCells(worldState, cells[chosenAction]['coordinates'], nextPositionActions)
    futureCarrying = False
    if (rlMethod == 'sarsa'):
      futureCarrying = AgentModule.determineFutureCarrying(chosenAgent, cells, chosenAction)
    qTable.changeQTable(worldState.representation['malePosition']['cellType'], chosenAction, layer, cells[chosenAction]['type'], nextPositionActions, alpha, gamma, rlMethod, chosenPolicy, futureCarrying, nextPositionCells)
    pickedUpOrDroppedOff = False
    if chosenAgent.type == 'm':
      pickedUpOrDroppedOff = worldState.updateEnvironmentState(worldState.representation['malePosition']['coordinates'], chosenAction, chosenAgent.type, chosenAgent.yesCarry, cells[chosenAction]['type'])
    if pickedUpOrDroppedOff:
      if cells[chosenAction]['type'] == 'pickup' or cells[chosenAction]['type'] == 'dropoff':
        AgentModule.pickupOrDropoff(chosenAgent, cells[chosenAction]['type'])
    if cells[chosenAction]['type'] == 'pickup' or cells[chosenAction]['type'] == 'dropoff':
      AgentModule.pickupOrDropoff(chosenAgent, cells[chosenAction]['type'])


    terminalStateReached = True
    for cell in worldState.representation['dropoffCellBlocks']:
      if worldState.representation['dropoffCellBlocks'][cell] < 5:
        terminalStateReached = False
    if terminalStateReached:
      env = EnvironmentModule.Environment()
      worldState = StateModule.State(env)


  print('final environment:')
  for x in range(2, -1, -1):
    print('Level', x + 1)
    for y in range(2, -1, -1):
      print('{:^60}'.format(str(worldState.environment[x][y][0])), '{:^60}'.format(str(worldState.environment[x][y][1])), '{:^60}'.format(str(worldState.environment[x][y][2])))
  print()
  for layer in ['carrying', 'notCarrying']:
    print(layer)
    print('{:^10}'.format(' '), '{:^15}'.format('up'), '{:^15}'.format('down'), '{:^15}'.format('west'), '{:^15}'.format('east'), '{:^15}'.format('north'), '{:^15}'.format('south'))
    for position in ['normal', 'risky', 'pickup', 'dropoff']:
      print('{:^10}'.format(position), '{:^15}'.format(qTable.table[layer][position]['up']), '{:^15}'.format(qTable.table[layer][position]['down']), '{:^15}'.format(qTable.table[layer][position]['west']), '{:^15}'.format(qTable.table[layer][position]['east']), '{:^15}'.format(qTable.table[layer][position]['north']), '{:^15}'.format(qTable.table[layer][position]['south']))
      print()
  print()
    
    
def main():
  rlMethod = 'qLearning'
  policy1 = 'pRandom'
  policy2 = 'pGreedy'
  policy3 = 'pExploit'
  env = EnvironmentModule.Environment()
  worldState = StateModule.State(env)
  qTable = TableModule.Qtable()
  maleAgent = AgentModule.Agent('m')
  femaleAgent = AgentModule.Agent('f')
  alpha = 0.3
  gamma = 0.5
  print('experiment 1a environment and q-table:')
  experiment1(rlMethod, policy1, policy1, env, worldState, qTable, maleAgent, femaleAgent, alpha, gamma)
  print('experiment 1b environment and q-table:')
  experiment1(rlMethod, policy1, policy2, env, worldState, qTable, maleAgent, femaleAgent, alpha, gamma)
  print('experiment 1c environment and q-table:')
  experiment1(rlMethod, policy1, policy3, env, worldState, qTable, maleAgent, femaleAgent, alpha, gamma)
  
if __name__ == "__main__" :
    main();