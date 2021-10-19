# Game Of Greed

PR:https://github.com/moayadalhaj/Game-of-Greed/pull/5

This is the third version of game of greed

## functionality

up to now, we have three classes, GameLogic, Banker and Game.

GameLogic has two static methods, calculate_score: to calculate the score for the round, and roll_dice to return random numbers between 1 and 6, the amount of values in the tuple depends on the input number to the method

Banker has four methods:

1. init: for initializing an instance

2. shelf: for storing a value in a temporary position

3. bank: to save the value inside the accumulator

4. clear_shelf: to clear the temporary shelf

Game has five methods:

1. init: for initializing an instance

2. play: for starting the game

3. rolling: to continue roll the dice and and calculate the unbanked and banked points

4. cheat: to handle cheating scenarios

5. zilch: for no points in the round, and round is over
