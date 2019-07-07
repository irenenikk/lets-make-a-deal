import numpy as np
import random
from env import Env
from agent import Agent

if __name__ == "__main__":
    episodes = 10000
    agent_reward = 0
    random_agent_reward = 0
    agent = Agent()
    # use the greedy exploration policy
    threshold = 0.2
    for e in range(episodes):
        env = Env()
        # make less random decisions with more training
        if e % 100 == 0:
            threshold /= 2
        initial_door = agent.choose_initial_door()
        action = agent.choose_if_switch() if random.uniform(0, 1) > threshold else random.choice([0, 1])
        r = env.open_door(initial_door, action)
        agent.update_Q_table(action, r)
        agent_reward += r
        # see what randomly switching yields in comparison
        rand_r = env.open_door(initial_door, random.choice([0, 1]))
        random_agent_reward += rand_r
    print('Cumulative agent reward', agent_reward)
    print('Cumulative agent reward when switching randomly', random_agent_reward)
    print('Final Q value table:')    
    print('no switch =', agent.Q_table[0], ' switch =', agent.Q_table[1])