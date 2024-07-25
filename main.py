import gym
import numpy as np
from node import Node
from mcts import mcts

def main():
    env = gym.make("Taxi-v3")
    env.seed(0)  # Use seed to make results better comparable
    rewards = []
    for i in range(10):
        env.reset()
        terminal = False
        root = Node()  # Initialize empty tree
        sum_reward = 0.
        while not terminal:
            env.render()
            mcts(env, root)  # Expand tree from root node using mcts
            values = [c.sum_value/c.visits for c in root.children]  # Calculate values for child actions
            bestchild = root.children[np.argmax(values)]  # Select the best child
            _, reward, terminal, _ = env.step(bestchild.action)  # Perform action for child
            root = bestchild  # Use the best child as next root
            root.parent = None
            sum_reward += reward
        rewards.append(sum_reward)
        print("Finished run " + str(i+1) + " with reward: " + str(sum_reward))
    print("Mean reward: ", np.mean(rewards))

if __name__ == "__main__":
    main()
