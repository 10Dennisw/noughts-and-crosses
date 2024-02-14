import random # the random module is imported

class noughts_and_cross_player:
    def __init__(self,):
        # the init function will generate the possible moves
        self.possible_moves = [i for i in range(1, 10)]

    def switching_player(self, current_player):
        '''
        This function will change the player
        :param current_player: the current player is inserted
        :return: the current player is returned. The current player will change.
        '''
        if current_player == 1:
            current_player = 2
        else:
            current_player = 1
        return current_player

    def removing_move(self, move):
        '''
        This function will remove the move from the class attribute possible moves
        :param move: the chosen move
        :return: nothing is returned from this function
        '''
        self.possible_moves.remove(move)

    def reset(self):
        # This function will reset the number of possible moves
        self.possible_moves = [i for i in range(1, 10)]

class UserPlayer(noughts_and_cross_player):
    def user_move(self):
        '''
        This function will ask the user to generate a move.
        The function will then check that the input is valid and the move is available
        :return: A valid user move is returned
        '''

        invalid_move = True

        while invalid_move:
            user_move = input("Please input a move: ")

            try:
                user_move = int(user_move)
                if user_move in self.possible_moves:
                    self.possible_moves.remove(user_move)
                    invalid_move = False
                else:
                    print("That appears not to be a valid move ...")
                    print("The square has already been taken")
                    print("Please input an integer, in the range 1-9 from a square that is not already taken")
            except:
                print("That appears not to be a valid move ...")
                print("Please input an integer, in the range 1-9 from a square that is not already taken")
        return user_move

class ComputerPlayer(noughts_and_cross_player):
    def random_computer_move(self):
        '''
        This function will generate and return a random possible move using the random module
        :return: the computer move will be returned
        '''
        computer_move = random.choice(self.possible_moves)
        self.possible_moves.remove(computer_move)
        return computer_move

    def evaluate(self, moves_player_1, moves_player_2, depth):
        '''
        This function will evaluate the move
        :param moves_player_1: This parameter holds the moves played by player 1
        :param moves_player_2: This parameter holds the moves played by player 2
        :param depth: The depth is used to ensure that winning the game quicker is rewarded
        :return: the score is of the move and a binary value if the user is the winner is returned
        '''

        # Define the winning combinations
        winning_combos = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
            [1, 5, 9],
            [3, 5, 7]
        ]
        for combo in winning_combos:
            if all(pos in moves_player_1 for pos in combo):
                return 10 - depth, True
            elif all(pos in moves_player_2 for pos in combo):
                return -10 + depth, True
        return 0, False

    def minimax(self, depth, isMax, moves_player_1, moves_player_2):
        '''
        This function performs the minmax algorithm to make sure that the the computer makes an intelligent move
        :param depth: This parameter is the depth/ number of the iterations that the algorithm performs
        :param isMax: This parameter is determines whether the player should maximise or minimise the score
        :param moves_player_1: This parameter holds the moves played by player 1
        :param moves_player_2: This parameter holds the moves played by player 2
        :return: The algorithm returns the score/ evaluation of the move and the best move for the respective player
        '''
        score, game_winner = self.evaluate(moves_player_1, moves_player_2, depth)

        # If the game has ended, return the evaluation score
        if game_winner is True or depth == 0:
            return score, None

        # If it's the maximizer's turn
        if isMax:
            best_move = None
            maxEval = float('-inf')
            for move in list(self.possible_moves):  # Create a copy of the list for iteration
                moves_player_1.append(move)
                self.possible_moves.remove(move)
                eval = self.minimax(depth - 1, False, moves_player_1, moves_player_2)[0]
                moves_player_1.remove(move)
                self.possible_moves.append(move)
                maxEval = max(maxEval, eval)
                if maxEval == eval:
                    best_move = move
            return maxEval, best_move

        # If it's the minimizer's turn
        else:
            best_move = None
            minEval = float('inf')
            for move in list(self.possible_moves):
                moves_player_2.append(move)
                self.possible_moves.remove(move)
                eval = self.minimax(depth - 1, True, moves_player_1, moves_player_2)[0]
                moves_player_2.remove(move)
                self.possible_moves.append(move)
                minEval = min(minEval, eval)
                if minEval == eval:
                    best_move = move
            return minEval, best_move