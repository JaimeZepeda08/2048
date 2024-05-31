# 2048

## Description

This is a Python implementation of the classic 2048 game using the Pygame library. The game involves sliding tiles on a grid to combine them and create a tile with the number 2048. The game also includes an AI that can automatically play the game.

## Installation

To run the 2048 game, you need to have both Python and Pygame installed on your computer.

1. **Install Python**: Download and install the latest version of Python from the official [Python website](https://www.python.org/downloads/).

2. **Install Pygame**: Use `pip` to install Pygame by running the following command in your terminal or command prompt:

```
pip install pygame
```

## Running the Game

1. **Clone the Repository**: clone this repository to your local machine using the following command:

```
git clone https://github.com/JaimeZepeda08/2048.git
```

> OR download the project files from my [website](https://jaimezepeda.vercel.app/projects)

2. **Navigate to the Directory**: change to the directory containing the game code:

```
cd 2048
```

3. **Run the Game**: execute the main python file to play the game:

```
python3 main.py
```

## Controls

`Up Arrow`: Slide tiles up

`Down Arrow`: Slide tiles down

`Left Arrow`: Slide tiles left

`Right Arrow`: Slide tiles right

`Spacebar`: Toggle AI mode

## Game Over

The game ends when there are no more valid moves available. This is checked by trying to move the tiles in all four directions. If none of the moves change the grid, it indicates that the grid is full and no more moves can be made.
