import sys
sys.path.append("../")
from SearchProblems.SearchProblemSolver import SearchProblemSolver, State
sys.path.pop()
from copy import deepcopy

# a)    
#       Representation: ([[int]], (X0, Y0))
#       Initial State: ([[int]] shuffled, (X0, Y0))
#       Final States: [[1,2,3,...],[...],...,[..., 0]]
#
#       Operators           Pre-conditions      Effects
#       Move UP             Y > 0               0 goes up
#       Move DOWN           Y < SIZE-1          0 goes down
#       Move LEFT           X > 0               0 goes left
#       Move RIGHT          X < SIZE-1          0 goes right

class NPuzzleState(State):
    def __init__(self, zero, board):
        self.zero = zero
        self.board = board
    
    def __str__(self):
        return str(self.board)
    
    def __eq__(self, other):
        return self.board == other.board


class NPuzzleSolver(SearchProblemSolver):
    def __init__(self, initial_state):
        self.side = len(initial_state.board)
        self.solution = [[i*self.side+j+1 for j in range(self.side)] for i in range(self.side)]
        self.solution[self.side-1][self.side-1] = 0
        super().__init__(initial_state)
    
    def H1(self, state):
        result = 0
        for i in range(self.side):
            for j in range(self.side):
                if state.board[i][j] != self.solution[i][j]:
                    result += 1
        return result

    def heuristic(self, state):
        return self.H1(state)

    def operators(self, state):
        new_states = []
        (x, y) = state.zero

        if y > 0:
            new_board = deepcopy(state.board)
            new_board[y][x] = new_board[y-1][x]
            new_board[y-1][x] = 0
            new_states.append(NPuzzleState((x, y-1), new_board))
        if y < self.side-1:
            new_board = deepcopy(state.board)
            new_board[y][x] = new_board[y+1][x]
            new_board[y+1][x] = 0
            new_states.append(NPuzzleState((x, y+1), new_board))
        if x > 0:
            new_board = deepcopy(state.board)
            new_board[y][x] = new_board[y][x-1]
            new_board[y][x-1] = 0
            new_states.append(NPuzzleState((x-1, y), new_board))
        if x < self.side-1:
            new_board = deepcopy(state.board)
            new_board[y][x] = new_board[y][x+1]
            new_board[y][x+1] = 0
            new_states.append(NPuzzleState((x+1, y), new_board))
        return new_states
    
    def is_final_state(self, state):
        return state.board == self.solution

def main():
    problems = [
        ((1,1), [[1,2,3],[5,0,6],[4,7,8]]),
        #((2,1), [[1,3,6],[5,2,0],[4,7,8]]),
        #((0,2), [[1,6,2],[5,7,3],[0,4,8]]),
        #((1,1), [[5,1,3,4],[2,0,7,8],[10,6,11,12],[9,13,14,15]])
    ]

    for i, (pos, board) in enumerate(problems):
        print("Problem", i+1)
        initial_state = NPuzzleState(pos, board)
        solver = NPuzzleSolver(initial_state)

        solutions = [
            solver.breath_first_search(10),
            solver.depth_first_search(10),
            solver.iterative_deepening_search(20),
            solver.uniform_cost_search(10),
            solver.greedy_search(10),
            solver.A_star_search(10),
        ]

        for (path, cost) in solutions:
            print("Cost:", cost)
            if path == []:
                print("Solution not found.")
            else:
                print("Path:", SearchProblemSolver.path_to_string(path))
                print("Number of Operations:", len(path)-1)
            print("")

if __name__ == "__main__":
    main()