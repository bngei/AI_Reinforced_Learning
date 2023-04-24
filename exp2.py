import EnvironmentModule
import StateModule
import AgentModule
import TableModule

# experiment2 runs the second experiment
def experiment2(rlMethod1, rlMethod2, policy1, policy2, env, worldState, qTable, maleAgent, femaleAgent, alpha, gamma):
  firstDropoffCellFIlled = False
  firstTerminalStateReached = False
  for i in range(10000):
    chosenRLMethod = ''
    chosenPolicy = ''
    chosenAgent = None
    notChosenAgent = None
    if i < 500:
      chosenRLMethod = rlMethod1
      chosenPolicy = policy1
    else:
      chosenRLMethod = rlMethod2
      chosenPolicy = policy2
    if i % 2 != 0:
      chosenAgent = maleAgent
      notChosenAgent = femaleAgent
    else:
      chosenAgent = femaleAgent
      notChosenAgent = maleAgent
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
    if (chosenRLMethod == 'sarsa'):
      futureCarrying = AgentModule.determineFutureCarrying(chosenAgent, cells, chosenAction)
    qTable.changeQTable(worldState.representation['malePosition']['cellType'], chosenAction, layer, cells[chosenAction]['type'], nextPositionActions, alpha, gamma, chosenRLMethod, chosenPolicy, futureCarrying, nextPositionCells)
    pickedUpOrDroppedOff = False
    if chosenAgent.type == 'm':
      pickedUpOrDroppedOff = worldState.updateEnvironmentState(worldState.representation['malePosition']['coordinates'], chosenAction, chosenAgent.type, chosenAgent.yesCarry, cells[chosenAction]['type'])
    else:
      pickedUpOrDroppedOff = worldState.updateEnvironmentState(worldState.representation['femalePosition']['coordinates'], chosenAction, chosenAgent.type, chosenAgent.yesCarry, cells[chosenAction]['type'])
    if pickedUpOrDroppedOff:
      if cells[chosenAction]['type'] == 'pickup' or cells[chosenAction]['type'] == 'dropoff':
        AgentModule.pickupOrDropoff(chosenAgent, cells[chosenAction]['type'])

    if firstDropoffCellFIlled == False:
      for cell in worldState.representation['dropoffCellBlocks']:
        if worldState.representation['dropoffCellBlocks'][cell] == 5:
          firstDropoffCellFIlled = True
          print('first dropoff cell filled at iteration', cell)
          print('qTable: ')
          for layer in ['carrying', 'notCarrying']:
            print(layer)
            print('{:^10}'.format(' '), '{:^15}'.format('up'), '{:^15}'.format('down'), '{:^15}'.format('west'), '{:^15}'.format('east'), '{:^15}'.format('north'), '{:^15}'.format('south'))
            for position in ['normal', 'risky', 'pickup', 'dropoff']:
              print('{:^10}'.format(position), '{:^15}'.format(qTable.table[layer][position]['up']), '{:^15}'.format(qTable.table[layer][position]['down']), '{:^15}'.format(qTable.table[layer][position]['west']), '{:^15}'.format(qTable.table[layer][position]['east']), '{:^15}'.format(qTable.table[layer][position]['north']), '{:^15}'.format(qTable.table[layer][position]['south']))
            print()
          print()
          break
    
    terminalStateReached = True
    for cell in worldState.representation['dropoffCellBlocks']:
      if worldState.representation['dropoffCellBlocks'][cell] < 5:
        terminal_state_reached = False
    if terminal_state_reached:
      if first_terminal_state_reached == False:
        first_terminal_state_reached = True
        print('first terminal state reached')
        print('qTable:')
        for layer in ['carrying', 'notCarrying']:
          print(layer)
          print('{:^10}'.format(' '), '{:^15}'.format('up'), '{:^15}'.format('down'), '{:^15}'.format('west'), '{:^15}'.format('east'), '{:^15}'.format('north'), '{:^15}'.format('south'))
          for position in ['normal', 'risky', 'pickup', 'dropoffCellBlocks']:
            print('{:^10}'.format(position), '{:^15}'.format(qTable.table[layer][position]['up']), '{:^15}'.format(qTable.table[layer][position]['down']), '{:^15}'.format(qTable.table[layer][position]['west']), '{:^15}'.format(qTable.table[layer][position]['east']), '{:^15}'.format(qTable.table[layer][position]['north']), '{:^15}'.format(qTable.table[layer][position]['south']))
          print()
        print()
      env = EnvironmentModule.Environment()
      worldState = StateModule.State(env)
  print('final environment')
  print(chosenAgent.type, 'is carrying: ', chosenAgent.yesCarry)
  print(notChosenAgent.type, 'is carrying: ', notChosenAgent.yesCarry)
  for x in range(2, -1, -1):
    print('Level', x + 1)
    for y in range(2, -1, -1):
      print('{:^60}'.format(str(worldState.environment[x][y][0])), '{:^60}'.format(str(worldState.environment[x][y][1])), '{:^60}'.format(str(worldState.environment[x][y][2])))
  print()
  print('final q-table')
  for layer in ['carrying', 'notCarrying']:
    print(layer)
    print('{:^10}'.format(' '), '{:^15}'.format('up'), '{:^15}'.format('down'), '{:^15}'.format('west'), '{:^15}'.format('east'), '{:^15}'.format('north'), '{:^15}'.format('south'))
    for position in ['normal', 'risky', 'pickup', 'dropoff']:
      print('{:^10}'.format(position), '{:^15}'.format(qTable.table[layer][position]['up']), '{:^15}'.format(qTable.table[layer][position]['down']), '{:^15}'.format(qTable.table[layer][position]['west']), '{:^15}'.format(qTable.table[layer][position]['east']), '{:^15}'.format(qTable.table[layer][position]['north']), '{:^15}'.format(qTable.table[layer][position]['south']))
    print()
  print()


def main():
  rlMethod1 = 'qLearning'
  rlMethod2 = 'sarsa'
  policy1 = 'pRandom'
  policy2 = 'pExploit'
  env = EnvironmentModule.Environment()
  worldState = StateModule.State(env)
  qTable = TableModule.Qtable()
  maleAgent = AgentModule.Agent('m')
  femaleAgent = AgentModule.Agent('f')
  alpha = 0.3
  gamma = 0.5
  print('experiment 2 environment and q-table:')
  experiment2(rlMethod1, rlMethod2, policy1, policy2, env, worldState, qTable, maleAgent, femaleAgent, alpha, gamma)
  
if __name__ == "__main__" :
    main();