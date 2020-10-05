import chess
import math

board = chess.initial_state()
white_moves = []
black_moves = []

while True:
    user_player = input("White or Black? ")
    if user_player in ["White", "white", "Black", "black"]:
        break

if user_player in ["White", "white"]:
    user_player = chess.W
    ai_player = chess.B
else:
    user_player = chess.B
    ai_player = chess.W

while True:
    if user_player == chess.W:
        print(chess.print_board(board))
        while True:
            print(chess.actions(board, chess.W, 1, white_moves))
            user_action_1 = input("Input move in form \"x_1, y_1\": ")
            user_action_2 = input("Input move in form \"x_2, y_2\": ")
            user_action = [(int(user_action_1.replace(",", "").replace(" ", "")[0]), int(user_action_1.replace(",", "").replace(" ", "")[1])), (int(user_action_2.replace(",", "").replace(" ", "")[0]), int(user_action_2.replace(",", "").replace(" ", "")[1]))]
            if user_action in chess.actions(board, chess.W, 1, white_moves):
                white_moves += [user_action]
                break
        board = chess.result(board, user_action)
        ai_action = chess.minimax(board, 2, -math.inf, math.inf, chess.B, black_moves, white_moves)
        black_moves += [ai_action]
        #print(ai_action)
        board = chess.result(board, ai_action)
    if user_player == chess.B:
        ai_action = chess.minimax(board, 2, -math.inf, math.inf, chess.W, white_moves, black_moves)
        white_moves += [ai_action]
        board = chess.result(board, ai_action)
        print(chess.print_board(board))
        while True:
            print(chess.actions(board, chess.B, 1, black_moves))
            user_action_1 = input("Input move in form \"x_1, y_1\": ")
            user_action_2 = input("Input move in form \"x_2, y_2\": ")
            user_action = [(int(user_action_1.replace(",", "").replace(" ", "")[0]), int(user_action_1.replace(",", "").replace(" ", "")[1])), (int(user_action_2.replace(",", "").replace(" ", "")[0]), int(user_action_2.replace(",", "").replace(" ", "")[1]))]
            if user_action in chess.actions(board, chess.B, 1, black_moves):
                black_moves += [user_action]
                break
        board = chess.result(board, user_action)
