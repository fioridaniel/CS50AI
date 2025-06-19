"""
Tic Tac Toe Player
"""

import copy
import math

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    num_x = num_o = 0

    for row in board:
        for cell in row:
            if cell == X:
                num_x += 1
            elif cell == O:
                num_o += 1
            
    if num_x <= num_o:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    possible_actions = set()

    for i in range(3):
        for j in range(3):
            if  board[i][j] == EMPTY:
                possible_actions.add((i, j))

    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    
    current_player = player(board)
    
    # se o jogo ja terminou, entao retorna o mesmo tabuleiro
    if current_player == None:
        return board
    
    board_copy = copy.deepcopy(board)
    board_copy[i][j] = current_player
    
    return board_copy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # linhas
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not EMPTY:
            return row[0]
    
    # colunas
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not EMPTY:
            return board[0][j]
    
    # diagonal principal
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    
    # diagonal secundaria
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]
    
    # nenhum vencedor
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for row in board:
        for cell in row:
            if  cell == EMPTY:
                return False
        
    return True   

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    player = winner(board)
    
    if player == X:
        return 1
    
    elif player == O:
        return -1
    
    return 0

def min_value_func(board):
    if terminal(board):
        return utility(board)
    
    v = math.inf

    all_actions = actions(board)
    for action in all_actions:
        v = min(v, max_value_func(result(board, action)))

    return v

def max_value_func(board):
    if terminal(board):
        return utility(board)
    
    v = -math.inf

    all_actions = actions(board)
    for action in all_actions:
        v = max(v, min_value_func(result(board, action)))

    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    current_player = player(board)
    
    if current_player == X:
        # X quer maximizar
        value = -math.inf
        best_action = None
        
        for action in actions(board):
            min_value = min_value_func(result(board, action))
            
            # pega a melhor escolha
            if min_value > value:
                value = min_value
                best_action = action
        
        return best_action
    
    else:
        # O quer minimizar
        value = math.inf
        best_action = None
        
        for action in actions(board):
            max_value = max_value_func(result(board, action))
            
            # pega a melhor escolha
            if max_value < value:
                value = max_value
                best_action = action
        
        return best_action
    