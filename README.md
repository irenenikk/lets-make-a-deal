# Using reinforcement learning to solve the Monty Hall problem

[Here is a friendly Wikipedia link](https://en.wikipedia.org/wiki/Monty_Hall_problem) for those who are unfamiliar with the formulation.

This is a simple program to train an agent to switch doors in the Monty Hall problem using Q-learning.

Yes, this is a total overkill, absolutely no reinforcement learning is required to train an agent to play successfully. As there is only one state, the problem is effectively a repeated game, and the agent could just easily calculate how often it was a better idea to switch, because there is no need to take future states into account. I basically built this just to tinker around with Q learning a little in practice, and decided to start off easy.