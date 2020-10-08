import chess
import math

board = chess.initial_state()
depth = 2  # Change this number to increase/decrease how many moves ahead the ai looks
white_moves = []
black_moves = []

while True:
    user_player = input("White or Black? ")
    if user_player in ["White", "white"]:
        user_player = chess.W
        ai_player = chess.B
        break
    elif user_player in ["Black", "black"]:
        user_player = chess.B
        ai_player = chess.W
        break


while True:
    if user_player == chess.W:
        print(chess.print_board(board))
        possible_user_actions = chess.actions(board, chess.W, 1, white_moves, black_moves)
        if not possible_user_actions:
            if chess.utility(board, white_moves, black_moves) == 10000:
                print("White Wins!")
            elif chess.utility(board, white_moves, black_moves) == -10000:
                print("Black Wins!")
            else:
                print("Tie!")
            break
        while True:
            try:
                print(possible_user_actions)
                user_action_1 = input("Input move \"x_1 y_1\": ")
                user_action_2 = input("Input move \"x_2 y_2\": ")
                user_action = [(int(user_action_1.replace(",", "").replace(" ", "")[0]), int(user_action_1.replace(",", "").replace(" ", "")[1])), (int(user_action_2.replace(",", "").replace(" ", "")[0]), int(user_action_2.replace(",", "").replace(" ", "")[1]))]
                if user_action in chess.actions(board, chess.W, 1, white_moves, black_moves):
                    white_moves += [user_action]
                    break
            except (ValueError, IndexError) as Error:
                pass
        if board[user_action[0][0]][user_action[0][1]] == chess.W_P and user_action[1][0] == 0:
            while True:
                promotion = input("Knight, Bishop, Rook, or Queen? ")
                if promotion in ["Knight", "knight"]:
                    promotion = chess.W_N
                    break
                elif promotion in ["Bishop", "bishop"]:
                    promotion = chess.W_B
                    break
                elif promotion in ["Rook", "rook"]:
                    promotion = chess.W_R
                    break
                elif promotion in ["Queen", "queen"]:
                    promotion = chess.W_Q
                    break
            board = chess.result(board, user_action, promotion)
        else:
            board = chess.result(board, user_action, None)
        ai_action = chess.minimax(board, depth, -math.inf, math.inf, chess.B, black_moves, white_moves)
        if not ai_action:
            print(chess.print_board(board))
            if chess.utility(board, white_moves, black_moves) == 10000:
                print("White Wins!")
            elif chess.utility(board, white_moves, black_moves) == -10000:
                print("Black Wins!")
            else:
                print("Tie!")
            break
        black_moves += [ai_action]
        board = chess.result(board, ai_action[0], ai_action[1])

    if user_player == chess.B:
        ai_action = chess.minimax(board, depth, -math.inf, math.inf, chess.W, white_moves, black_moves)
        if not ai_action:
            print(chess.print_board(board))
            if chess.utility(board, white_moves, black_moves) == 10000:
                print("White Wins!")
            elif chess.utility(board, white_moves, black_moves) == -10000:
                print("Black Wins!")
            else:
                print("Tie!")
            break
        white_moves += [ai_action]
        board = chess.result(board, ai_action[0], ai_action[1])
        print(chess.print_board(board))
        possible_user_actions = chess.actions(board, chess.B, 1, black_moves, white_moves)
        if not possible_user_actions:
            if chess.utility(board, white_moves, black_moves) == 10000:
                print("White Wins!")
            elif chess.utility(board, white_moves, black_moves) == -10000:
                print("Black Wins!")
            else:
                print("Tie!")
            break
        while True:
            try:
                print(possible_user_actions)
                user_action_1 = input("Input move in form \"x_1, y_1\": ")
                user_action_2 = input("Input move in form \"x_2, y_2\": ")
                user_action = [(int(user_action_1.replace(",", "").replace(" ", "")[0]), int(user_action_1.replace(",", "").replace(" ", "")[1])), (int(user_action_2.replace(",", "").replace(" ", "")[0]), int(user_action_2.replace(",", "").replace(" ", "")[1]))]
                if user_action in chess.actions(board, chess.B, 1, black_moves, white_moves):
                    black_moves += [user_action]
                    break
            except (ValueError, IndexError) as Error:
                pass
        if board[user_action[0][0]][user_action[0][1]] == chess.B_P and user_action[1][0] == 7:
            while True:
                promotion = input("Knight, Bishop, Rook, or Queen? ")
                if promotion in ["Knight", "knight"]:
                    promotion = chess.B_N
                    break
                elif promotion in ["Bishop", "bishop"]:
                    promotion = chess.B_B
                    break
                elif promotion in ["Rook", "rook"]:
                    promotion = chess.B_R
                    break
                elif promotion in ["Queen", "queen"]:
                    promotion = chess.B_Q
                    break
            board = chess.result(board, user_action, promotion)
        else:
            board = chess.result(board, user_action, None)
