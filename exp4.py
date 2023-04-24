import EnvironmentModule
import StateModule
import AgentModule
import TableModule

# experiment4 runs the experiment for the fourth experiment
def experiment4(rlMethod, policy1, policy2, env, worldState, qTable, maleAgent, femaleAgent, alpha, gamma):
  numberOfTerminalStates = 0
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
    chosenActions = AgentModule.chooseAction(chosenAgent, cells, qValues, chosenPolicy)
    nextPositionActions = AgentModule.setNextPositionPossibleActions(worldState, chosenAgent.type, chosenActions)
    nextPositionCells = AgentModule.setNextPositionPossibleCells(worldState, cells[chosenActions]['coordinates'], nextPositionActions)
    futureCarrying = False
    if (rlMethod == 'sarsa'):
      futureCarrying = AgentModule.determineFutureCarrying(chosenAgent, cells, chosenActions)
    qTable.changeQTable(worldState.representation['malePosition']['cellType'], chosenActions, layer, cells[chosenActions]['type'], nextPositionActions, alpha, gamma, rlMethod, chosenPolicy, futureCarrying, nextPositionCells)
    if chosenAgent.type == 'm':
      worldState.updateEnvironmentState(worldState.representation['malePosition']['coordinates'], chosenActions, chosenAgent.type, chosenAgent.yesCarry, cells[chosenActions]['type'])
    else:
      worldState.updateEnvironmentState(worldState.representation['femalePosition']['coordinates'], chosenActions, chosenAgent.type, chosenAgent.yesCarry, cells[chosenActions]['type'])
    if cells[chosenActions]['type'] == 'pickup' or cells[chosenActions]['type'] == 'dropoff':
      AgentModule.pickupOrDropoff(chosenAgent, cells[chosenActions]['type'])
    terminalStateReached = True
    for cell in worldState.representation['dropoffCellBlocks']:
      if worldState.representation['dropoffCellBlocks'][cell] < 5:
        terminalStateReached = False
    if terminalStateReached:
      numberOfTerminalStates += 1
      env = EnvironmentModule.Environment()
      if 3 <= numberOfTerminalStates <= 5:
        print('changing pickup cells')
        env.environment[0][1][1] = {'type': 'normal', 'occupiedBy': ''}
        env.environment[1][2][2] = {'type': 'normal', 'occupiedBy': ''}
        env.environment[2][2][1] = {'type': 'pickup', 'occupiedBy': '', 'blockCount': 10}
        env.environment[0][2][0] = {'type': 'pickup', 'occupiedBy': '', 'blockCount': 10}
      elif 6 <= numberOfTerminalStates:
        print('reverting pickup cells')
        env.environment[0][1][1] = {'type': 'pickup', 'occupiedBy': '', 'blockCount': 10}
        env.environment[1][2][2] = {'type': 'pickup', 'occupiedBy': '', 'blockCount': 10}
        env.environment[2][2][1] = {'type': 'normal', 'occupiedBy': ''}
        env.environment[0][2][0] = {'type': 'normal', 'occupiedBy': ''}
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
  policy2 = 'pExploit'
  env = EnvironmentModule.Environment()
  worldState = StateModule.State(env)
  qTable = TableModule.Qtable()
  maleAgent = AgentModule.Agent('m')
  femaleAgent = AgentModule.Agent('f')
  alpha = 0.3
  gamma = 0.5
  print('experiment 4 environment and q-table:')
  experiment4(rlMethod, policy1, policy2, env, worldState, qTable, maleAgent, femaleAgent, alpha, gamma)
  
if __name__ == "__main__" :
    main();