import random # imports the random library to generate a random player

# imports the two classes from the two seperate python files

from player_inheritance import UserPlayer, ComputerPlayer
from board import Board

# creating the instances for the two classes
user = UserPlayer()
computer = ComputerPlayer()
board = Board()

# defining variable which will allow the game to continue, this variable will be false if the user wishes to quit
continue_playing = True

# printing Noughts and Cross in ASCII art
print("""                                                                                                                                                                                                               
         ,--.                                                                                                                                                                                                  
       ,--.'|                                    ,---,       ___                                                                     ,----..                                                                   
   ,--,:  : |                                  ,--.' |     ,--.'|_                                                    ,---,         /   /   \                                                                  
,`--.'`|  ' :   ,---.           ,--,           |  |  :     |  | :,'                                       ,---,     ,---.'|        |   :     :  __  ,-.   ,---.                                                
|   :  :  | |  '   ,'\        ,'_ /|  ,----._,.:  :  :     :  : ' :  .--.--.                          ,-+-. /  |    |   | :        .   |  ;. /,' ,'/ /|  '   ,'\   .--.--.    .--.--.               .--.--.    
:   |   \ | : /   /   |  .--. |  | : /   /  ' /:  |  |,--.;__,'  /  /  /    '             ,--.--.    ,--.'|'   |    |   | |        .   ; /--` '  | |' | /   /   | /  /    '  /  /    '     ,---.   /  /    '   
|   : '  '; |.   ; ,. :,'_ /| :  . ||   :     ||  :  '   |  |   |  |  :  /`./            /       \  |   |  ,"' |  ,--.__| |        ;   | ;    |  |   ,'.   ; ,. :|  :  /`./ |  :  /`./    /     \ |  :  /`./   
'   ' ;.    ;'   | |: :|  ' | |  . .|   | .\  .|  |   /' :__,'| :  |  :  ;_             .--.  .-. | |   | /  | | /   ,'   |        |   : |    '  :  /  '   | |: :|  :  ;_   |  :  ;_     /    /  ||  :  ;_     
|   | | \   |'   | .; :|  | ' |  | |.   ; ';  |'  :  | | | '  : |__ \  \    `.           \__\/: . . |   | |  | |.   '  /  |        .   | '___ |  | '   '   | .; : \  \    `. \  \    `. .    ' / | \  \    `.  
'   : |  ; .'|   :    |:  | : ;  ; |'   .   . ||  |  ' | : |  | '.'| `----.   \          ," .--.; | |   | |  |/ '   ; |:  |        '   ; : .'|;  : |   |   :    |  `----.   \ `----.   \'   ;   /|  `----.   \ 
|   | '`--'   \   \  / '  :  `--'   \`---`-'| ||  :  :_:,' ;  :    ;/  /`--'  /         /  /  ,.  | |   | |--'  |   | '/  '        '   | '/  :|  , ;    \   \  /  /  /`--'  //  /`--'  /'   |  / | /  /`--'  / 
'   : |        `----'  :  ,      .-./.'__/\_: ||  | ,'     |  ,   /'--'.     /         ;  :   .'   \|   |/      |   :    :|        |   :    /  ---'      `----'  '--'.     /'--'.     / |   :    |'--'.     /  
;   |.'                 `--`----'    |   :    :`--''        ---`-'   `--'---'          |  ,     .-./'---'        \   \  /           \   \ .'                       `--'---'   `--'---'   \   \  /   `--'---'   
'---'                                 \   \  /                                          `--`---'                  `----'             `---`                                                `----'               
""")

# printing instructions and waiting for the user to press enter until the game starts
print("--> The game is played on a grid that's 3 squares by 3 squares (3x3)")
print("--> This game allows the two players and the ability to play against the computer")
print("--> The marker for Player 1 is Noughts (O)")
print("--> The marker for Player 2 is Crosses (X)")
print("--> The first player to get 3 of their markers in a row (up, down, across or diagonal) is the winner")
print("--> When all nine squares are full, the game is over. If no player wins, it is a draw")
print()
input("Press enter to continue...")
print()

# While loop which will repeat until the user wants to quit
while continue_playing is True:

    # While loop which will until a valid response is created depending on the player wishes to play against another
    # player or computer
    human_or_computer = False
    while human_or_computer is False:
        answer_human_or_computer = input("Do you want to play against the Player or Computer (please enter \"p\" or \"c\"): ")
        if answer_human_or_computer == 'p' or answer_human_or_computer == 'c':
            human_or_computer = True
        else:
            print("It seems that isn't a valid answer ... (please enter \"p\" or \"c\")")
            print("P stands for Player")
            print("C stands for Computer")

    # While loop which will until a valid response is created depending on the difficulty of the computer
    if answer_human_or_computer == 'c':
        difficulty_invalid = True
        while difficulty_invalid is True:
            difficulty_invalid = True
            computer_difficulty = input("Please enter the difficulty of the computer (please enter \"1\", \"2\" or \"3\"): ")

            if computer_difficulty == '1' or computer_difficulty == '2' or computer_difficulty == '3':
                difficulty_invalid = False
            else:
                print("It seems that isn't a valid answer ... (please enter \"1\", \"2\" or \"3\")")
                print("1: Computer makes random moves")
                print("2: Computer makes intelligent moves")
                print("3: Computer makes the most intelligent moves")

    # resets and intialises the board and player class to ensure that the the respective attributes are reset
    board.initial()
    user.reset()
    computer.reset()

    # generating a random player which will start
    current_player = random.randint(1, 2)
    print("Player 1 will be noughts: \"0\" \nPlayer 2 will be crosses: \"X\"")
    print()
    print("--> Player", current_player, "will start")

    # generating empty move list
    moves_lst = []
    moves_lst_p1 = []
    moves_lst_p2 = []

    # For loop which will repeat 9 times, which is the total number of squares
    for _ in range(9):
        # This will print the current player apart from the first loop
        if _ == 0:
            pass
        else:
            print("--> It is player", current_player, "'s turn ...")

        # This will generate a computer move
        if current_player == 2 and answer_human_or_computer == 'c':
            # This will generate a random computer move
            if computer_difficulty == "1":
                move = computer.random_computer_move()
                moves_lst_p1, moves_lst_p2 = board.adding_move(move, current_player)

            # This will generate a smart computer move using the minimax algorithm
            elif computer_difficulty == "2":
                move = computer.minimax(2, False, moves_lst_p1, moves_lst_p2)[1]
                user.removing_move(move)
                computer.removing_move(move)

            # This will generate an intelligent computer move using the minimax algorithm using a bigger depth
            elif computer_difficulty == "3":
                move = computer.minimax(3, False, moves_lst_p1, moves_lst_p2)[1]
                user.removing_move(move)
                computer.removing_move(move)

            # These two statements will update the board and change the move list depending on the generated move
            moves_lst_p1, moves_lst_p2 = board.adding_move(move, current_player)
            board.changing_board(move, current_player)


        else:
            # This generate a user move and will update the move list and the board
            move = user.user_move()
            moves_lst_p1, moves_lst_p2 = board.adding_move(move, current_player)
            board.changing_board(move, current_player)

        # This show the current board
        board.current_board()

        # This checker if there is a winner, if a winner is find the code will break out of the loop
        # if no winner is found the current player will change
        winner = board.checking_winner()
        if winner[0] is True:
            break
        else:
            current_player = user.switching_player(current_player)

    # This if statement prints a different statement depending upon the result of the game
    if winner[0]:
        print("Player", winner[1], "has won")
        # if a winner is found and the player is a human player, then the below will print
        if winner[1] == 1 or answer_human_or_computer == 'p':
            print("""
 ██████╗ ██████╗ ███╗   ██╗ ██████╗ ██████╗  █████╗ ████████╗██╗   ██╗██╗      █████╗ ████████╗██╗ ██████╗ ███╗   ██╗███████╗██╗
██╔════╝██╔═══██╗████╗  ██║██╔════╝ ██╔══██╗██╔══██╗╚══██╔══╝██║   ██║██║     ██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝██║
██║     ██║   ██║██╔██╗ ██║██║  ███╗██████╔╝███████║   ██║   ██║   ██║██║     ███████║   ██║   ██║██║   ██║██╔██╗ ██║███████╗██║
██║     ██║   ██║██║╚██╗██║██║   ██║██╔══██╗██╔══██║   ██║   ██║   ██║██║     ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║╚════██║╚═╝
╚██████╗╚██████╔╝██║ ╚████║╚██████╔╝██║  ██║██║  ██║   ██║   ╚██████╔╝███████╗██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║███████║██╗
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝ 
            """)
        # if a winner is found and the player is a computer player, then the below will print
        else:
            print("""
████████╗██╗  ██╗███████╗     ██████╗ ██████╗ ███╗   ███╗██████╗ ██╗   ██╗████████╗███████╗ ██████╗     ██╗    ██╗██╗███╗   ██╗███████╗
   ██╔══╝██║  ██║██╔════╝    ██╔════╝██╔═══██╗████╗ ████║██╔══██╗██║   ██║╚══██╔══╝██╔════╝ ██╔══██╗    ██║    ██║██║████╗  ██║██╔════╝
   ██║   ███████║█████╗      ██║     ██║   ██║██╔████╔██║██████╔╝██║   ██║   ██║   █████╗   ██████╔╝    ██║ █╗ ██║██║██╔██╗ ██║███████╗
   ██║   ██╔══██║██╔══╝      ██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ██║   ██║   ██║   ██╔══╝   ██╔══██╗    ██║███╗██║██║██║╚██╗██║╚════██║
   ██║   ██║  ██║███████╗    ╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ╚██████╔╝   ██║   ███████╗ ██║  ██║    ╚███╔███╔╝██║██║ ╚████║███████║
   ╚═╝   ╚═╝  ╚═╝╚══════╝     ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝      ╚═════╝    ╚═╝   ╚══════╝ ╚═╝  ╚═╝     ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚══════╝
            """)
    # if a draw is reached then the below line will print
    else:
        print("It is a draw")
        print("""
██╗████████╗███████╗     █████╗     ██████╗ ██████╗  █████╗ ██╗    ██╗             
██║╚══██╔══╝██╔════╝    ██╔══██╗    ██╔══██╗██╔══██╗██╔══██╗██║    ██║             
██║   ██║   ███████╗    ███████║    ██║  ██║██████╔╝███████║██║ █╗ ██║             
██║   ██║   ╚════██║    ██╔══██║    ██║  ██║██╔══██╗██╔══██║██║███╗██║             
██║   ██║   ███████║    ██║  ██║    ██████╔╝██║  ██║██║  ██║╚███╔███╔╝    ██╗██╗██╗
╚═╝   ╚═╝   ╚══════╝    ╚═╝  ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝     ╚═╝╚═╝╚═╝                                                                               
        """)

    # The valid answer is set to false and then the while loop is reached until a valid answer is obtained
    # The while loop will obtain an answer if the user wishes to continue playing noughts and crosses
    valid_a = False
    while valid_a is False:
        answer = input("Do you want to continue playing (please enter \"y\" or \"n\"): ")
        if answer == "y":
            valid_a = True
        elif answer == "n":
            valid_a = True
            continue_playing = False
        else:
            print("It seems that isn't a valid answer ... (please enter \"y\" or \"n\")")
