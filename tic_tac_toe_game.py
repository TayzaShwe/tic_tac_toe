from curses.panel import bottom_panel
from random import randint
import math

class tic_tac_toe_game:

    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.player2_type = "bot"
        self.bot_difficulty = "easy"

    # printing the tic tac toe board
    def print_board(self):
        print("")
        print(f"  {self.board[0][0]}  |  {self.board[0][1]}  |  {self.board[0][2]}  ")
        print("-----------------")
        print(f"  {self.board[1][0]}  |  {self.board[1][1]}  |  {self.board[1][2]}  ")
        print("-----------------")
        print(f"  {self.board[2][0]}  |  {self.board[2][1]}  |  {self.board[2][2]}  ")
        print("")

    # reads user input. If invalid, asks again. If valid, places the move on the board. 
    def player_input(self, player, symbol):
        print(f"{player}'s move (Enter a number between 1-9):")
        move = int(input())-1
        move_row = move//3
        move_col = move%3
        while (((move<0) and (move>8)) or (self.board[move_row][move_col] != " ")):
            print("Your input is invalid. Enter another number:")
            move = int(input())-1
            move_row = move//3
            move_col = move%3   
        self.board[move_row][move_col] = symbol

    # function for main player's input
    def player1_input(self):
        self.player_input("Player 1", "X")
    
    # function for other player/bot's move
    def player2_move(self):
        if (self.player2_type == "player"):
            self.player_input("Player 2", "O")
        elif (self.bot_difficulty == "easy"):
            bot_move = randint(0, 8)
            bot_move_row = bot_move//3
            bot_move_col = bot_move%3
            while (((bot_move<0) and (bot_move>8)) or (self.board[bot_move_row][bot_move_col] != " ")):
                bot_move = randint(0, 8)
                bot_move_row = bot_move//3
                bot_move_col = bot_move%3
            self.board[bot_move_row][bot_move_col] = "O"
        elif (self.bot_difficulty == "hard"):
            bot_move_row, bot_move_col = self.bot_ai()
            self.board[bot_move_row][bot_move_col] = "O"

    # bot difficulty hard ai function. Uses the minmax algorithm. If bot's turn, maximizes. If player's turn, minimizes. 
    def bot_ai(self):
        def min_max(board, symbol):
            best_info = [(-math.inf if symbol=="O" else math.inf), 0, 0]
            for row in range(3):
                for col in range(3):
                    if (board[row][col] == " "):
                        board_copy = board[:]
                        board_copy[row][col] = symbol
                        game_status = self.check_board(board_copy)
                        if (game_status == "You win!"):
                            cur_info =  [-1, row, col]
                        elif (game_status == "You lose :("):
                            cur_info = [1, row, col]
                        elif (game_status == "Draw"):
                            cur_info = [0, row, col]
                        else:
                            next_symbol = "X" if symbol=="O" else "O"
                            cur_info = min_max(board_copy, next_symbol)
                        if symbol == "O":
                            if (max(cur_info[0], best_info[0]) == cur_info[0]):
                                best_info = cur_info[:]
                        else:
                            if (min(cur_info[0], best_info[0]) == cur_info[0]):
                                best_info = cur_info[:]

    # checks the status of the game
    def check_board(self, board):

        # checks for player1 win! 
        for row in range(3):
            if ((board[row][0] == "X") and (board[row][1] == "X") and (board[row][2] == "X")):
                return "You win!"
        for col in range(3):
            if ((board[0][col] == "X") and (board[1][col] == "X") and (board[2][col] == "X")):
                return "You win!"
        if ((board[0][0] == "X") and (board[1][1] == "X") and (board[2][2] == "X")):
            return "You win!"
        if ((board[0][2] == "X") and (board[1][1] == "X") and (board[2][0] == "X")):
            return "You win!"

        # checks for player1 lost :(
        for row in range(3):
            if ((board[row][0] == "O") and (board[row][1] == "O") and (board[row][2] == "O")):
                return "You lost :("
        for col in range(3):
            if ((board[0][col] == "O") and (board[1][col] == "O") and (board[2][col] == "O")):
                return "You lost :("
        if ((board[0][0] == "O") and (board[1][1] == "O") and (board[2][2] == "O")):
            return "You lost :("
        if ((board[0][2] == "O") and (board[1][1] == "O") and (board[2][0] == "O")):
            return "You lost :("

        # checks for draw
        symbol_count = 0
        for col in range(3):
            for row in range(3):
                if (self.board[col][row] != " "):
                    symbol_count += 1
        if (symbol_count == 9):
            return "Draw"

        # no win or loss or draw
        return "nothing"

    # gets player2 type
    def get_player2_type(self):
        print("Do you want to play against a bot or a player? (bot/player):")
        choice = input().lower()
        while ((choice != "bot") and (choice != "player")):
            print("Your input is invalid. Enter 'bot' or 'player:")
            choice = input().lower()
        self.player2_type = choice
        if (self.player2_type == "bot"):
            print("Enter bot difficulty (easy/hard):")
            dif = input().lower()
            while ((dif != "easy") and (dif != "hard")):
                print("Your input is invalid. Enter 'easy' or 'hard:")
                dif = input().lower()
            self.bot_difficulty = dif

    # game driver 
    def start_game(self):
        self.get_player2_type()
        self.player1_input()
        self.print_board()
        game_status = self.check_board(self.board)
        while (game_status == "nothing"):
            self.player2_move()
            self.print_board()
            game_status = self.check_board(self.board)
            if (game_status != "nothing"):
                print(game_status)
                return           
            self.player1_input()
            self.print_board()
            game_status = self.check_board(self.board)
        print(game_status)

game = tic_tac_toe_game()
game.start_game()


