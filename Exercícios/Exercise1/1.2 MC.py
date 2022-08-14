import sys
sys.path.append("../")
from SearchProblems.SearchProblemSolver import SearchProblemSolver, State
sys.path.pop()

# a)    
#       Representation: [M, C, B] (missionaries and cannibals in the initial side and the side of the boat)
#       Initial State: [3, 3, 0]
#       Final States: [0, 0, _]
#
#       SAFE_STATE: (M == 1 OR M == 2) => M == C, WHICH IS EQUIVALENT TO: (M != 1 AND M != 2) OR M == C
#
#       Operators           Pre-conditions                              Effects
#       Move 2 M to 1       B = 0 AND SAFE_STATE AND M >= 2             M -= 2; B = 1
#       Move 2 C to 1       B = 0 AND SAFE_STATE AND C >= 2             C -= 2; B = 1
#       Move 1 M 1 C to 1   B = 0 AND SAFE_STATE AND C >= 1 AND M >= 1  M -= 1; C -= 1; B = 1;
#       Move 1 M to 1       B = 0 AND SAFE_STATE AND M >= 1             M -= 1; B = 1
#       Move 1 C to 1       B = 0 AND SAFE_STATE AND C >= 1             C -= 1; B = 1
#
#       Move 2 M to 0       B = 1 AND SAFE_STATE AND M <= 1             M += 2; B = 0
#       Move 2 C to 0       B = 1 AND SAFE_STATE AND C <= 1             C += 2; B = 0
#       Move 1 M 1 C to 0   B = 1 AND SAFE_STATE AND C <= 2 AND M <= 2  M += 1; C += 1; B = 0;
#       Move 1 M to 0       B = 1 AND SAFE_STATE AND M <= 2             M += 1; B = 0
#       Move 1 C to 0       B = 1 AND SAFE_STATE AND C <= 2             C += 1; B = 0

class MCState(State):
    def __init__(self, m, c, b):
        self.m = m
        self.c = c
        self.b = b

    def __str__(self):
        return "({}|{}|{})".format(self.m, self.c, self.b)
    
    def __eq__(self, other):
        if isinstance(other, MCState):
            return self.m == other.m and self.c == other.c and self.b == other.b
        return False

class MCSolver(SearchProblemSolver):
    def __init__(self):
        super().__init__(MCState(3, 3, 0))
    
    def operators(self, state):
        new_states = []

        if state.b == 0:
            if state.m >= 1:
                new_states.append(MCState(state.m-1, state.c, 1))
                if state.m >= 2:
                    new_states.append(MCState(state.m-2, state.c, 1))
            if state.c >= 1:
                new_states.append(MCState(state.m, state.c-1, 1))
                if state.c >= 2:
                    new_states.append(MCState(state.m, state.c-2, 1))
            if state.c >= 1 and state.m >= 1:
                new_states.append(MCState(state.m-1, state.c-1, 1))
        else:
            if state.m <= 2:
                new_states.append(MCState(state.m+1, state.c, 0))
                if state.m <= 1:
                    new_states.append(MCState(state.m+2, state.c, 0))
            if state.c <= 2:
                new_states.append(MCState(state.m, state.c+1, 0))
                if state.c <= 1:
                    new_states.append(MCState(state.m, state.c+2, 0))
            if state.c <= 2 and state.m <= 2:
                new_states.append(MCState(state.m+1, state.c+1, 0))
        
        # Filter safe states
        iterator = filter(MCSolver.is_safe_state, new_states)

        return list(iterator)
    
    def is_final_state(self, state):
        return state.m == 0 and state.c == 0
    
    def is_safe_state(state):
        return (state.m != 1 and state.m != 2) or state.m == state.c

def main():
    solver = MCSolver()

    solutions = [
        solver.breath_first_search(),           # c1) Breath first search
        solver.depth_first_search(11),          # c2) Deapth first search
        solver.iterative_deepening_search(20)   # c3) Iterative deepening
    ]

    for (path, n_nodes) in solutions:
        print("Visited Nodes:", n_nodes)
        if path == []:
            print("Solution not found.")
        else:
            print("Path:", SearchProblemSolver.path_to_string(path))
            print("Number of Operations:", len(path)-1)
        print("")

if __name__ == "__main__":
    main()