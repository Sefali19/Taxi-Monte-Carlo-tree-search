# Monte Carlo Tree Search (MCTS) for Taxi-v3 Environment

This project implements the Monte Carlo Tree Search (MCTS) algorithm for solving the Taxi-v3 environment from OpenAI Gym.

## Description

MCTS is a heuristic search algorithm for decision processes, notably used in game play. This implementation applies MCTS to the Taxi-v3 problem, a grid-world environment where a taxi needs to pick up and drop off passengers at specific locations.

Key features:
- Implementation of MCTS algorithm
- Application to the Taxi-v3 environment
- Visualization of the environment during execution

## Requirements

- Python 3.x
- NumPy
- OpenAI Gym

## Installation

Clone the repository and install the required packages:

```bash
git clone https://github.com/your-username/mcts-taxi-v3.git
cd mcts-taxi-v3
pip install numpy gym
```

## Usage

Run the main script to execute the MCTS algorithm:

```bash
python mcts_taxi.py
```

## Implementation Details

- `Node`: Represents a node in the MCTS tree
- `rollout`: Performs a random rollout from a given state
- `mcts`: Implements the core MCTS algorithm
- `main`: Runs multiple episodes of the algorithm and reports results

## Parameters

- Number of iterations for MCTS: 500
- Number of episodes: 10
- Epsilon for exploration: 0.5

## Results

The script outputs the reward for each run and the mean reward across all runs.

## Visualization

The environment is rendered after each action. You can see the taxi moving in the grid world.

## License

[MIT License](https://opensource.org/licenses/MIT)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgments

This project uses the Taxi-v3 environment from OpenAI Gym and implements MCTS as described in reinforcement learning literature.
```
