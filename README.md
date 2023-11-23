# AI_Reinforced_Learning

This repository contains modules and classes to simulate reinforcement learning agents in an environment. The code comprises multiple Python files that interact to simulate agents' actions and learning processes.

## Key Modules:
### ActionModule.py:
Defines possible actions for agents based on their positions and constraints within the environment.
Determines available moves for agents and possible actions in the next position.

### AgentModule.py:
Defines an Agent class, initializes agents, and manages their carrying status.
Sets potential actions, updates agents' positions, and handles carrying objects.

### EnvironmentModule.py:
Defines an Environment class that initializes the environment's cells and manages agent movement.
Handles agent movements, interactions with pickup/dropoff cells, and updates the environment state.

### StateModule.py:
Manages the state of the environment, positions of agents, and block counts in pickup/dropoff cells.
Updates the environment and state after an action and identifies possible cells for agents.

### QTableModule.py:
Implements a Q-table class that initializes and updates Q-values based on actions, rewards, and policies.
Utilizes Q-learning and SARSA functions to estimate future state/action rewards.

### RewardFunction.py:
Calculates estimated rewards for each cell based on its type.

### PolicyModule.py:
Implements policies for agent decision-making, such as random action selection, exploitation, and exploration.

### ValueFunction.py:
Contains functions for updating Q-values using Q-learning and SARSA methods.
These modules work together to simulate agent interactions in an environment and implement reinforcement learning algorithms for decision-making.
