class Board:
    def initial(self):
        '''
        This function generates the generates a moves list, and a empty list for the two player's move
        Furthermore, the function prints the grid and the respective number corresponding to each square in the grid
        '''
        self.moves_lst = [" "] * 9
        self.moves_player_1 = []
        self.moves_player_2 = []
        print()
        print("Please see the square and corresponding number below:")
        print()
        print(" ", 1, " | ", 2, " | ", 3)
        print("-"*17)
        print(" ", 4, " | ", 5, " | ", 6)
        print("-"*17)
        print(" ", 7, " | ", 8, " | ", 9)
        print()

    def current_board(self):
        '''
        This function prints the current board
        '''
        print()
        print(" ", self.moves_lst[0], " | ", self.moves_lst[1], " | ", self.moves_lst[2])
        print("------------------")
        print(" ", self.moves_lst[3], " | ", self.moves_lst[4], " | ", self.moves_lst[5])
        print("------------------")
        print(" ", self.moves_lst[6], " | ", self.moves_lst[7], " | ", self.moves_lst[8])
        print()


    def changing_board(self, user_move, player_num):
        '''
        The function will change the user board depending on the move and player number
        :param user_move: the move that the respective player has selected
        :param player_num: the player number of the player which has made the move.
        The move list is changed depending on the player number
        '''
        print(self.moves_lst[int(user_move)-1])
        if player_num == 1:
            self.moves_lst[user_move-1] = "O"
        else:
            self.moves_lst[user_move-1] = "X"

    def adding_move(self, user_move, player_num):
        '''
        The user move is appended to the move list for the respective player
        :param user_move: the move that the respective player has selected
        :param player_num: the player number of the player which has made the move.
        The moves for the respective player is adjusted
        '''
        if player_num == 1:
            self.moves_player_1.append(user_move)
        else:
            self.moves_player_2.append(user_move)

        return self.moves_player_1, self.moves_player_2

    def checking_winner(self):
        '''
        This function checks for if a player has won
        :return: a binary value is returned to determine whether a player has won, the player number is also returned
        '''
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

        for i in winning_combos:
            if all(j in self.moves_player_1 for j in i):
                return True, 1  # Player 1 wins
            if all(j in self.moves_player_2 for j in i):
                return True, 2  # Player 2 wins

        return False, 0  # No winner