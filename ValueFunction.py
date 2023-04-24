"""
Here we calculate the estimated rewards of a future state or action. 
The 2 functions used here are the Q-learning function and the SARSA function.
"""

# qLearningValueFunction is a function that calculates the new Q value based on the Q-Learning method
def qLearningValueFunction(oldQValues, moveRewards, nextQValues, alpha, gamma):
  nextQValuesList = []
  for i in nextQValues:
    nextQValuesList.append(nextQValues[i])
  return oldQValues + alpha * (moveRewards + gamma * max(nextQValuesList) - oldQValues)


# sarsaValueFunction is a function that calculates the new Q value based on the SARSA method
def sarsaValueFunction(oldQValues, moveRewards, next_q_val, alpha, gamma):
  return oldQValues + alpha * (moveRewards + gamma * next_q_val - oldQValues)