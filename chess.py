import math

E = "."
W_P = "P"
W_B = "B"
W_N = "N"
W_R = "R"
W_Q = "Q"
W_K = "K"
W = [W_P, W_B, W_N, W_R, W_Q, W_K]
B_P = "p"
B_B = "b"
B_N = "n"
B_R = "r"
B_Q = "q"
B_K = "k"
B = [B_P, B_B, B_N, B_R, B_Q, B_K]


def print_board(board):
    new_board = ""
    for i in range(8):
        for j in range(8):
            new_board += str(board[i][j]) + "  "
        new_board += "\n"
    return new_board.replace("\'", "").replace(",", "").replace("[", "").replace("]", "")


def initial_state():
    return [[B_R, E, B_B, B_Q, B_K, B_B, E, B_R],
            [B_P, B_P, B_P, B_P, E, B_P, B_P, B_P],
            [E, E, B_N, E, E, B_N, E, E],
            [E, E, E, E, B_P, E, E, E],
            [E, E, W_B, E, W_P, E, E, E],
            [E, E, E, E, E, W_N, E, E],
            [W_P, W_P, W_P, W_P, E, W_P, W_P, W_P],
            [W_R, W_N, W_B, W_Q, W_K, W_B, E, W_R]]


def check(board, player):
    if player == W:
        non_player = B
    else:
        non_player = W
    for i in range(8):
        for j in range(8):
            if board[i][j] in player and board[i][j] == W_K or board[i][j] in player and board[i][j] == B_K:
                for action in actions(board, non_player, 0, []):
                    try:
                        if action[1] == (i, j):
                            return False
                    except IndexError:
                        pass
                return True
    return True


def ai_castle(moves, player):
    king_side_castle = True
    queen_side_castle = True
    if player == W:
        for move in moves:
            if (7, 4) == move[0]:
                king_side_castle = False
                queen_side_castle = False
            elif (7, 0) == move[0]:
                queen_side_castle = False
            elif (7, 7) == move[0]:
                king_side_castle = False
    else:
        for move in moves:
            if (0, 4) == move[0]:
                king_side_castle = False
                queen_side_castle = False
            elif (0, 0) == move[0]:
                queen_side_castle = False
            elif (0, 7) == move[0]:
                king_side_castle = False
    return [queen_side_castle, king_side_castle]


def actions(board, player, depth, moves):

    def line(board, i, j, k, l, player):
        line_action = []
        if player == W:
            non_player = B
        else:
            non_player = W

        try:
            while True:
                if board[i+k][j+l] == E and i+k > -1 and j+l > -1:
                    line_action += [[(i, j), (i+k, j+l)]]
                    if k > 0:
                        k += 1
                    elif k < 0:
                        k -= 1
                    if l > 0:
                        l += 1
                    elif l < 0:
                        l -= 1
                elif board[i+k][j+l] in non_player and i+k > -1 and j+1 > -1:
                    line_action += [[(i, j), (i+k, j+l)]]
                    break
                else:
                    break
        except IndexError:
            pass
        return line_action

    actions = []

    if player == W:
        non_player = B
    else:
        non_player = W

    queen_side_castle = True
    king_side_castle = True
    for move in moves:
        if player == W:
            if move[0] == (7, 4):
                queen_side_castle = False
                king_side_castle = False
            elif move[0] == (7, 0):
                queen_side_castle = False
            elif move[0] == (7, 7):
                king_side_castle = False
        else:
            if move[0] == (0, 4):
                queen_side_castle = False
                king_side_castle = False
            elif move[0] == (0, 0):
                queen_side_castle = False
            elif move[0] == (0, 7):
                king_side_castle = False

    if player == W and board[7][4] == W_K and depth == 1 and (queen_side_castle or king_side_castle):
        if check(board, W):
            if board[7][0] == W_R and board[7][1] == board[7][2] == board[7][3] == E and queen_side_castle:
                if check(result(board, [(7, 4), (7, 3)]), W) and check(result(board, [(7, 4), (7, 2)]), W):
                    actions += [[(7, 4), (7, 2)]]
            if board[7][7] == W_R and board[7][5] == board[7][6] == E and king_side_castle:
                if check(result(board, [(7, 4), (7, 5)]), W) and check(result(board, [(7, 4), (7, 6)]), W):
                    actions += [[(7, 4), (7, 6)]]
    elif player == B and board[0][4] == B_K and depth == 1 and (queen_side_castle or king_side_castle):
        if check(board, B):
            if board[0][0] == B_R and board[0][1] == board[0][2] == board[0][3] == E and queen_side_castle:
                if check(result(board, [(0, 4), (0, 3)]), B) and check(result(board, [(0, 4), (0, 2)]), B):
                    actions += [[(0, 4), (0, 2)]]
            if board[0][7] == B_R and board[0][5] == board[0][6] == E and king_side_castle:
                if check(result(board, [(0, 4), (0, 5)]), B) and check(result(board, [(0, 4), (0, 6)]), B):
                    actions += [[(0, 4), (0, 6)]]

    for i in range(8):
        for j in range(8):
            if board[i][j] not in non_player and board[i][j] != E:
                if board[i][j] in player and board[i][j] == W_R or board[i][j] == B_R:
                    for action_line in line(board, i, j, -1, 0, player), line(board, i, j, 1, 0, player), line(board, i, j, 0, 1, player), line(board, i, j, 0, -1, player):
                        if action_line:
                            for action in action_line:
                                if depth == 1:
                                    if check(result(board, action), player):
                                        actions += [action]
                                else:
                                    actions += [action]

                if board[i][j] in player and board[i][j] == W_B or board[i][j] == B_B:
                    for action_line in line(board, i, j, -1, -1, player), line(board, i, j, 1, 1, player), line(board, i, j, -1, 1, player), line(board, i, j, 1, -1, player):
                        if action_line:
                            for action in action_line:
                                if depth == 1:
                                    if check(result(board, action), player):
                                        actions += [action]
                                else:
                                    actions += [action]

                if board[i][j] in player and board[i][j] == W_P:
                    try:
                        if i == 6:
                            if board[5][j] == E:
                                if board[4][j] == E:
                                    if depth == 1:
                                        if check(result(board, [(i, j), (4, j)]), W):
                                            actions += [[(i, j), (4, j)]]
                                    else:
                                        actions += [[(i, j), (4, j)]]
                    except IndexError:
                        pass
                    try:
                        if j - 1 > -1:
                            if board[i - 1][j - 1] in B:
                                if depth == 1:
                                    if check(result(board, [(i, j), (i - 1, j - 1)]), W):
                                        actions += [[(i, j), (i - 1, j - 1)]]
                                else:
                                    actions += [[(i, j), (i - 1, j - 1)]]
                    except IndexError:
                        pass
                    try:
                        if j + 1 < 8:
                            if board[i - 1][j + 1] in B:
                                if depth == 1:
                                    if check(result(board, [(i, j), (i - 1, j + 1)]), W):
                                        actions += [[(i, j), (i - 1, j + 1)]]
                                else:
                                    actions += [[(i, j), (i - 1, j + 1)]]
                    except IndexError:
                        pass
                    try:
                        if board[i - 1][j] == E:
                            if depth == 1:
                                if check(result(board, [(i, j), (i - 1, j)]), W):
                                    actions += [[(i, j), (i - 1, j)]]
                            else:
                                actions += [[(i, j), (i - 1, j)]]
                    except IndexError:
                        pass

                if board[i][j] in player and board[i][j] == B_P:
                    try:
                        if i == 1:
                            if board[2][j] == E:
                                if board[3][j] == E:
                                    if depth == 1:
                                        if check(result(board, [(i, j), (3, j)]), B):
                                            actions += [[(i, j), (3, j)]]
                                    else:
                                        actions += [[(i, j), (3, j)]]
                    except IndexError:
                        pass
                    try:
                        if j - 1 > -1:
                            if board[i + 1][j - 1] in W:
                                if depth == 1:
                                    if check(result(board, [(i, j), (i + 1, j - 1)]), B):
                                        actions += [[(i, j), (i + 1, j - 1)]]
                                else:
                                    actions += [[(i, j), (i + 1, j - 1)]]
                    except IndexError:
                        pass
                    try:
                        if j + 1 < 8:
                            if board[i + 1][j + 1] in W:
                                if depth == 1:
                                    if check(result(board, [(i, j), (i + 1, j + 1)]), B):
                                        actions += [[(i, j), (i + 1, j + 1)]]
                                else:
                                    actions += [[(i, j), (i + 1, j + 1)]]
                    except IndexError:
                        pass
                    try:
                        if board[i + 1][j] == E:
                            if depth == 1:
                                if check(result(board, [(i, j), (i + 1, j)]), B):
                                    actions += [[(i, j), (i + 1, j)]]
                            else:
                                actions += [[(i, j), (i + 1, j)]]
                    except IndexError:
                        pass

                if board[i][j] in player and board[i][j] == W_N or board[i][j] == B_N:
                    for action in [(i-2, j-1), (i-2, j+1), (i+2, j-1), (i+2, j+1), (i-1, j-2), (i-1, j+2), (i+1, j-2), (i+1, j+2)]:
                        if -1 < action[0] < 8 and -1 < action[1] < 8:
                            if board[action[0]][action[1]] not in player:
                                if depth == 1:
                                    if check(result(board, [(i, j), action]), player):
                                        actions += [[(i, j), action]]
                                else:
                                    actions += [[(i, j), action]]

                if board[i][j] in player and board[i][j] == W_Q or board[i][j] == B_Q:
                    for action_line in line(board, i, j, -1, 0, player), line(board, i, j, 1, 0, player), line(board, i, j, 0, 1, player), line(board, i, j, 0, -1, player), line(board, i, j, -1, -1, player), line(board, i, j, 1, 1, player), line(board, i, j, -1, 1, player), line(board, i, j, 1, -1, player):
                        if action_line:
                            for action in action_line:
                                if depth == 1:
                                    if check(result(board, action), player):
                                        actions += [action]
                                else:
                                    actions += [action]

                if board[i][j] in player and board[i][j] == W_K or board[i][j] == B_K:
                    for k in range(3):
                        for l in range(3):
                            try:
                                if board[i + k - 1][j + l - 1] not in player and i+k-1 > -1 and j+l-1 > -1:
                                    if depth == 1:
                                        if check(result(board, [(i, j), (i+k-1, j+l-1)]), player):
                                            actions += [[(i, j), (i+k-1, j+l-1)]]
                                    else:
                                        actions += [[(i, j), (i + k - 1, j + l - 1)]]
                            except IndexError:
                                pass
    return actions


def result(board, action):
    final_result = []

    for i in range(8):
        row_result = []
        for j in range(8):
            if i != action[0][0] or j != action[0][1]:
                if i != action[1][0] or j != action[1][1]:
                    if board[action[0][0]][action[0][1]] in [W_K, B_K] and abs(action[0][1] - action[1][1]) == 2 and i == action[0][0] and j in [0, 3, 5, 7]:
                        if action[1][1] == 2 and j == 0:
                            row_result += E
                        elif action[1][1] == 2 and j == 3:
                            if action[0][0] == 7:
                                row_result += W_R
                            else:
                                row_result += B_R
                        elif action[1][1] == 6 and j == 5:
                            if action[0][0] == 7:
                                row_result += W_R
                            else:
                                row_result += B_R
                        elif action[1][1] == 6 and j == 7:
                            row_result += E
                        else:
                            row_result += [board[i][j]]
                    else:
                        row_result += [board[i][j]]  # every other space stays the same
                else:
                    row_result += [board[action[0][0]][action[0][1]]]  # replaces new piece's space with original space
            else:
                row_result += [E]  # replaces original piece's space with an empty space
            if j == 7:
                final_result += [row_result]

    return final_result


def utility(board):
    if not actions(board, B, 1, []):
        if not check(board, B):
            return math.inf
        else:
            return 0
    elif not actions(board, W, 1, []):
        if not check(board, W):
            return -math.inf
        else:
            return 0
    W_Points = 0
    B_Points = 0

    for i in range(8):
        for j in range(8):
            if W_K in [board[7][2], board[7][6]] and i == 7 and j == 2:
                W_Points += 0.75
            if board[i][j] == W_P:
                W_Points += [[0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
                             [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
                             [0.5, 0.5, 0.75, 1, 1, 0.75, 0.5, 0.5],
                             [0.5, 0.5, 0.75, 1, 1, 0.75, 0.5, 0.5],
                             [0.5, 0.5, 0.75, 1, 1, 0.75, 0.5, 0.5],
                             [0.5, 0.75, 0.5, 0.5, 0.5, 0.5, 0.75, 0.5],
                             [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
                             [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]][i][j]
            if board[i][j] == W_N:
                W_Points += [[2.5, 3, 3, 3, 3, 3, 3, 2.5],
                             [2.5, 3, 3, 3, 3, 3, 3, 2.5],
                             [2.5, 3, 3, 3, 3, 3, 3, 2.5],
                             [2.5, 3, 3, 3, 3, 3, 3, 2.5],
                             [2.5, 3, 3, 3, 3, 3, 3, 2.5],
                             [2.5, 3, 3.25, 3, 3, 3.25, 3, 2.5],
                             [2.5, 3, 3, 3, 3, 3, 3, 2.5],
                             [2.5, 3, 3, 3, 3, 3, 3, 2.5]][i][j]
            if board[i][j] == W_B:
                W_Points += [[3, 3, 3, 3, 3, 3, 3, 3],
                             [3, 3, 3, 3, 3, 3, 3, 3],
                             [3, 3, 3, 3, 3, 3, 3, 3],
                             [3, 3, 3, 3, 3, 3, 3, 3],
                             [3, 3, 3, 3, 3, 3, 3, 3],
                             [3, 3, 3, 3, 3, 3, 3, 3],
                             [3, 3.75, 3, 3, 3, 3, 3.75, 3],
                             [3, 3, 3, 3, 3, 3, 3, 3]][i][j]
            if board[i][j] == W_R:
                W_Points += 5
            if board[i][j] == W_Q:
                W_Points += 9
            if B_K in [board[0][2], board[0][6]] and i == 0 and j == 2:
                B_Points += 0.75
            if board[i][j] == B_P:
                B_Points += [[0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
                             [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
                             [0.5, 0.75, 0.5, 0.5, 0.5, 0.5, 0.75, 0.5],
                             [0.5, 0.5, 0.75, 1, 1, 0.75, 0.5, 0.5],
                             [0.5, 0.5, 0.75, 1, 1, 0.75, 0.5, 0.5],
                             [0.5, 0.5, 0.75, 1, 1, 0.75, 0.5, 0.5],
                             [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
                             [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]][i][j]
            if board[i][j] == B_N:
                B_Points += [[2.5, 3, 3, 3, 3, 3, 3, 2.5],
                             [2.5, 3, 3, 3, 3, 3, 3, 2.5],
                             [2.5, 3, 3.25, 3, 3, 3.25, 3, 2.5],
                             [2.5, 3, 3, 3, 3, 3, 3, 2.5],
                             [2.5, 3, 3, 3, 3, 3, 3, 2.5],
                             [2.5, 3, 3, 3, 3, 3, 3, 2.5],
                             [2.5, 3, 3, 3, 3, 3, 3, 2.5],
                             [2.5, 3, 3, 3, 3, 3, 3, 2.5]][i][j]
            if board[i][j] == B_B:
                B_Points += [[3, 3, 3, 3, 3, 3, 3, 3],
                             [3, 3.75, 3, 3, 3, 3, 3.75, 3],
                             [3, 3, 3, 3, 3, 3, 3, 3],
                             [3, 3, 3, 3, 3, 3, 3, 3],
                             [3, 3, 3, 3, 3, 3, 3, 3],
                             [3, 3, 3, 3, 3, 3, 3, 3],
                             [3, 3, 3, 3, 3, 3, 3, 3],
                             [3, 3, 3, 3, 3, 3, 3, 3]][i][j]
            if board[i][j] == B_R:
                B_Points += 5
            if board[i][j] == B_Q:
                B_Points += 9
    # Returns a positive number if white is winning, negative number if black is winning in terms of pieces
    return W_Points - B_Points


def terminal(board, player):
    if not actions(board, player, 1, []):
        return True
    return False


def minimax(board, depth, alpha, beta, player, player_moves, non_player_moves):

    def negamax(board, depth, alpha, beta, player, non_player, player_moves, non_player_moves):
        if depth == 0 or terminal(board, player):
            if player == W:
                return utility(board)
            else:
                #print(print_board(board))
                #print(-utility(board))
                return -utility(board)

        value = -math.inf
        for action in actions(board, player, 1, player_moves):
            new_player_moves = player_moves + [action]
            value = max(value, -negamax(result(board, action), depth-1, -beta, -alpha, non_player, player, non_player_moves, new_player_moves))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value

    if player == W:
        non_player = B
    else:
        non_player = W

    negamax_value = negamax(board, depth, alpha, beta, player, non_player, player_moves, non_player_moves)
    #print(negamax_value)
    for action in actions(board, player, 1, player_moves):
        new_player_moves = player_moves + [action]
        if -negamax(result(board, action), depth-1, -beta, -alpha, non_player, player, non_player_moves, new_player_moves) == negamax_value:
            return action
