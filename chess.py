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
    return [[B_R, B_N, B_B, B_Q, B_K, B_B, B_N, B_R],
            [B_P, B_P, B_P, B_P, B_P, B_P, B_P, B_P],
            [E, E, E, E, E, E, E, E],
            [E, E, E, E, E, E, E, E],
            [E, E, E, E, E, E, E, E],
            [E, E, E, E, E, E, E, E],
            [W_P, W_P, W_P, W_P, W_P, W_P, W_P, W_P],
            [W_R, W_N, W_B, W_Q, W_K, W_B, W_N, W_R]]


def check(board, player):
    if player == W:
        non_player = B
    else:
        non_player = W
    #print(actions(board, non_player, 0))
    for i in range(8):
        for j in range(8):
            if board[i][j] in player and board[i][j] == W_K or board[i][j] in player and board[i][j] == B_K:
                for action in actions(board, non_player, 0):
                    #print(action)
                    try:
                        #print(action)
                        if action[1] == (i, j):
                            return False
                    except IndexError:
                        pass
                return True
    return True


def actions(board, player, depth):

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
                    row_result += [board[i][j]]
                else:
                    row_result += [board[action[0][0]][action[0][1]]]
            else:
                row_result += [E]
            if j == 7:
                final_result += [row_result]

    return final_result


def utility(board, player):
    if not actions(board, B, 1):
        if not check(board, B):
            if player == W:
                return math.inf
            else:
                return -math.inf
        else:
            return 0
    elif not actions(board, W, 1):
        if not check(board, W):
            if player == W:
                return -math.inf
            else:
                return math.inf
        else:
            return 0
    W_Points = 0
    B_Points = 0

    for i in range(8):
        for j in range(8):
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
                W_Points += [[3, 3, 3, 3, 3, 3, 3, 3],
                             [3, 3, 3, 3, 3, 3, 3, 3],
                             [3, 3, 3, 3, 3, 3, 3, 3],
                             [3, 3, 3, 3, 3, 3, 3, 3],
                             [3, 3, 3, 3, 3, 3, 3, 3],
                             [3, 3, 3.25, 3, 3, 3.25, 3, 3],
                             [3, 3, 3, 3, 3, 3, 3, 3],
                             [3, 3, 3, 3, 3, 3, 3, 3]][i][j]
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
                B_Points += [[3, 3, 3, 3, 3, 3, 3, 3],
                             [3, 3, 3, 3, 3, 3, 3, 3],
                             [3, 3, 3.25, 3, 3, 3.25, 3, 3],
                             [3, 3, 3, 3, 3, 3, 3, 3],
                             [3, 3, 3, 3, 3, 3, 3, 3],
                             [3, 3, 3, 3, 3, 3, 3, 3],
                             [3, 3, 3, 3, 3, 3, 3, 3],
                             [3, 3, 3, 3, 3, 3, 3, 3]][i][j]
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
    if player == W:
        return W_Points - B_Points
    else:
        return B_Points - W_Points


def terminal(board, player):
    if not actions(board, player, 1):
        return True
    return False


def minimax(board, depth, alpha, beta, player):
    if player == W:
        non_player = B
    else:
        non_player = W

    def negamax(board, depth, alpha, beta, player, non_player):
        if depth == 0 or terminal(board, player):
            return utility(board, player)

        value = -math.inf
        for action in actions(board, player, 1):
            value = max(value, negamax(result(board, action), depth-1, -beta, -alpha, non_player, player))  # problem with -minimax(result(board, action), depth-1, -beta, -alpha, non_player) returns None

            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value

    negamax_value = (negamax(board, depth, alpha, beta, player, non_player))
    for i in range(depth):
        for action in actions(board, player, 1):
            if -negamax(result(board, action), i, alpha, beta, non_player, player) == negamax_value:
                return action

#print(minimax(initial_state(), 2, -math.inf, math.inf, B))