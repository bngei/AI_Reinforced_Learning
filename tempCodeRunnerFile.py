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