import chess
import math

board = chess.initial_state()

while True:
    user_player = input("White or Black? ")
    if user_player in ["White", "white", "Black", "black"]:
        break

if user_player == "White" or user_player == "white":
    user_player = chess.W
    ai_player = chess.B
elif user_player == "Black" or user_player == "black":
    user_player = chess.B
    ai_player = chess.W

while True:
    if user_player == chess.W:
        print(chess.print_board(board))
        while True:
            print(chess.actions(board, chess.W, 1))
            user_action_1 = input("Input move in form \"x_1, y_1\": ")
            user_action_2 = input("Input move in form \"x_2, y_2\": ")
            try:
                user_action = [(int(user_action_1.replace(",", "").replace(" ", "")[0]), int(user_action_1.replace(",", "").replace(" ", "")[1])), (int(user_action_2.replace(",", "").replace(" ", "")[0]), int(user_action_2.replace(",", "").replace(" ", "")[1]))]
                if user_action in chess.actions(board, chess.W, 1):
                    break
            except IndexError:
                pass
        board = chess.result(board, user_action)
        board = chess.result(board, chess.minimax(board, 2, -math.inf, math.inf, chess.B))
    if user_player == chess.B:
        board = chess.result(board, chess.minimax(board, 2, -math.inf, math.inf, chess.W))
        print(chess.print_board(board))
        while True:
            print(chess.actions(board, chess.B, 1))
            user_action_1 = input("Input move in form \"x_1, y_1\": ")
            user_action_2 = input("Input move in form \"x_2, y_2\": ")
            user_action = [(int(user_action_1.replace(",", "").replace(" ", "")[0]), int(user_action_1.replace(",", "").replace(" ", "")[1])), (int(user_action_2.replace(",", "").replace(" ", "")[0]), int(user_action_2.replace(",", "").replace(" ", "")[1]))]
            if user_action in chess.actions(board, chess.B, 1):
                break
        board = chess.result(board, user_action)
