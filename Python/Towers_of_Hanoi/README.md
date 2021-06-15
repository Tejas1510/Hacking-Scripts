# Towers Of Hanoi Impementation using Python

## About

The Tower of Hanoi is a mathematical game or puzzle. It consists of three rods and a number of disks of different diameters, which can slide onto any rod.

The puzzle starts with the disks stacked on one rod in order of decreasing size, the smallest at the top, thus approximating a conical shape.

The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:

1. Only one disk can be moved at a time.
2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
3. No disk may be placed on top of a smaller disk.


## How to Play

The Following Steps help you in the setup and getting started with the script.

### Setup

* Download and install the latest version of [Python](https://www.python.org)
* Clone the repo using the following command and move into the following folder:

  ```bash
  git clone https://github.com/Tejas1510/Hacking-Scripts.git

  cd Hacking-Scripts/Python/Towers_of_Hanoi/
  ```
* Execute to following command to run the game:

  ```bash
  python main.py
  ```

### Playing the game

* After starting the game, we need to select the number of disks with which we want to play the game. The minimum is 3. After selecting the one number, the game starts and the disks on the current stack are visible like this.
  ! [ ](Python/Towers_of_Hanoi/assets/Game_start.png)
* We can use L,M,R commands to select the top-most element of left, middle and right stacks.
* We can use the same commands as above to select the stack to which we want to move the element. Here is how it looks.
  ! [ ](Python/Towers_of_Hanoi/assets/moving_elements.png)
* Selecting and moving from an empty stack results in an invalid move.


I hope you will enjoy this wonderful game!
