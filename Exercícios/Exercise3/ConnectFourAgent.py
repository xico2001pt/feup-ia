import math

def nlines4(board, player):
    # TODO
    pass

def nlines3(board, player):
    # TODO
    pass

def central(board, player):
    # TODO
    pass

class State:
    def is_end_state(self):
        raise NotImplementedError()
    
    def evaluate(self):
        raise NotImplementedError()
    
    def valid_moves(self):
        raise NotImplementedError()

def minimax_alpha_beta(state : State, depth, maximize, alpha, beta):
    if depth <= 0 or state.is_end_state():
        return state.evaluate()
    
    if maximize:
        max_eval = -math.inf
        for move in state.valid_moves():
            evaluation = minimax_alpha_beta(move, depth-1, False, alpha, beta)
            max_eval = max(max_eval, evaluation)
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
        return max_eval
    
    else:
        min_eval = math.inf
        for move in state.valid_moves():
            evaluation = minimax_alpha_beta(move, depth-1, True, alpha, beta)
            min_eval = min(min_eval, evaluation)
            beta = min(beta, evaluation)
            if beta >= alpha:
                break
        return min_eval