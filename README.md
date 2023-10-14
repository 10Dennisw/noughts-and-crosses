# Noughts & Crosses

The project is code to run a text-based game of noughts and cross (Tic-Tac-Toe). To create the game the scripts has used object-oriented programming (OOP). The GitHub repository contains three different python scripts. The name and a short summary can be found below:
- **‘board.py’**: this python scripts contains the board class which contains the attributes and methods of the board class. The board script will be further explored in paragraphs below.
- **‘player.py’**: this python scripts contains three different class. This includes a main player class, user player class and computer player class. Inheritance is used to make sure that the user player and computer player class inherit the methods from the main player class. The player script will be further explored in paragraphs below.
- **‘main.py’**: this python scripts imports the two classes from the other scripts and has the calls upon the methods to make sure that the game is ran correctly.

### Key Features:
- **Object-Oriented Programming**: is a concept which is based on creating ‘objects’ which contain data and code. The data in the form of attributes or properties. The code creates methods in the form of functions in python. The goal of object-orientated programming is to increase flexibility and maintainability of the code.
- **Inheritance**: is a mechanism where a new class inherits properties and behaviours from an existing class. Inheritance creates a parent and child class. The child class inherits the methods and attributes from the parent class. This promotes code reusability, and reduces redundant code.
- **Minimax Algorithm**: is a recursive algorithm which calls itself. The minimax algorithm assumes there are two players, which will make a move which optimises their utility/ score. By working out the respective score of each move, the algorithm can calculate the best move for the computer. 

## Board Script
As mentioned above the board script contains the board class. The board class contains the following methods:
- **Current_board**: this method will display the current board.
- **Changing_board**: the method will change the user board depending on the respective player and the move.
- **Adding_move**: the method adds the move to the move list for the respective player.
- **Checking_winner**: the method will check if a player has won. If so, it will return a binary variable if a player has won and which player has won.

## Player Script
As mentioned above the board script contains the main player, user, and computer class. The main player class contains the following methods:
- **Switching Player**: this method will change the player.
- **Removing Move**: this method will remove the move which is inputted from the possible move list.
- **Reset**: this method will reset the possible move list.

As mentioned, inheritance is used to ensure that the user and computer player classes extract. 

The user player class contains the following methods:
- **User Move**: this method will ask the user to input a grid for a possible move. The grid number which is inputted will be checked to determine if it is valid.
The computer player class contains the following methods:
- **Random Computer Move**: this method will generate a random available grid for the computer player. 
- **Evaluation**: this method will evaluate the current state of the board. Additionally, the evaluation method uses the depth of the minimax algorithm to incentivise the artificial intelligence to win the game quicker.
- **Minimax**: this method employs the minimax algorithm. The goal of the minimax algorithm is to find the best possible move. The minimax algorithm is a recursive algorithm which calls itself. The best possible move is calculated according to the logic that each player will play optimally. It does by assuming there are two different players. One player will aim to maximise the score. Whilst the other player will aim to minimise the score. It does this by exploring all possible moves, constructing a game tree of all possible moves. Where the player will select the move which is the best possible move for them.
