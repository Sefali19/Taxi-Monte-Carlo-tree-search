import copy
import random
import numpy as np
from node.py import Node
from rollout import rollout

def mcts(env, root, maxiter=500):
    """ Use this function as a starting point for implementing Monte Carlo Tree Search """
    root.children = [Node(root, a) for a in range(env.action_space.n)]

    for i in range(maxiter):
        state = copy.deepcopy(env)
        G = 0.

        # Epsilon greedy tree policy
        epsilon = 0.5
        greedy = np.random.choice([True, False], p=[epsilon, 1-epsilon])
        if greedy:
            values = [c.sum_value for c in root.children]
            node = root.children[np.argmax(values)]
        else:
            node = random.choice(root.children)
        _, reward, terminal, _ = state.step(node.action)
        G += reward

        # Expansion of tree
        node.children = [Node(node, a) for a in range(env.action_space.n)]

        # Rollout (Simulation)
        if not terminal:
            G += rollout(state)

        # Update all visited nodes in the tree
        while node.parent is not None:
            node.visits += 1
            node.sum_value += G
            node = node.parent
