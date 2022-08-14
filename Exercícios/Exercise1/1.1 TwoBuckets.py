import sys
sys.path.append("../")
from SearchProblems.SearchProblemSolver import SearchProblemSolver, State
sys.path.pop()

# a)
#       Representation: [X, Y] (amount of water in each bucket)
#       Initial State: [0, 0]
#       Final States: [2, _]
#
#       Operators           Pre-conditions          Effects
#       Fill A              X < 4                   X = 4;
#       Fill B              Y < 3                   Y = 3;
#       Empty A             X > 0                   X = 0;
#       Empty B             Y > 0                   Y = 0;
#       Poor A-B / B full   X + Y >= 3 AND Y < 3    X = X - (3 - Y); Y = 3;
#       Poor A-B / A empty  X + Y < 3 AND X > 0     Y = Y + X; X = 0;
#       Poor B-A / A full   X + Y >= 4 AND X < 4    Y = Y - (4 - X); X = 4;
#       Poor B-A / B empty  X + Y < 4 AND Y > 0     X = X + Y; Y = 0;

class TwoBucketsState(State):
    def __init__(self, bucket1, bucket2):
        self.bucket1 = bucket1
        self.bucket2 = bucket2
    
    def __str__(self):
        return "({}|{})".format(self.bucket1, self.bucket2)
    
    def __eq__(self, other):
        if isinstance(other, TwoBucketsState):
            return self.bucket1 == other.bucket1 and self.bucket2 == other.bucket2
        return False

class TwoBucketsSolver(SearchProblemSolver):
    def __init__(self, capacity1, capacity2, goal):
        super().__init__(TwoBucketsState(0, 0))
        self.capacity1 = capacity1
        self.capacity2 = capacity2
        self.goal = goal
    
    def operators(self, state):
        new_states = []

        if state.bucket1 < self.capacity1:
            new_states.append(TwoBucketsState(self.capacity1, state.bucket2))
        if state.bucket2 < self.capacity2:
            new_states.append(TwoBucketsState(state.bucket1, self.capacity2))
        if state.bucket1 > 0:
            new_states.append(TwoBucketsState(0, state.bucket2))
        if state.bucket2 > 0:
            new_states.append(TwoBucketsState(state.bucket1, 0))
        if state.bucket1+state.bucket2 >= self.capacity2 and state.bucket2 < self.capacity2:
            new_states.append(TwoBucketsState(state.bucket1-(self.capacity2-state.bucket2), self.capacity2))
        if state.bucket1+state.bucket2 < self.capacity2 and state.bucket1 > 0:
            new_states.append(TwoBucketsState(0, state.bucket1+state.bucket2))
        if state.bucket1+state.bucket2 >= self.capacity1 and state.bucket1 < self.capacity1:
            new_states.append(TwoBucketsState(self.capacity1, state.bucket2-(self.capacity1-state.bucket1)))
        if state.bucket1+state.bucket2 < self.capacity1 and state.bucket2 > 0:
            new_states.append(TwoBucketsState(state.bucket1+state.bucket2, 0))
        
        return new_states
    
    def is_final_state(self, state):
        return state.bucket1 == self.goal

def main():
    solver = TwoBucketsSolver(4, 3, 2)

    solutions = [
        solver.breath_first_search(),           # c1) Breath first search
        solver.depth_first_search(6),           # c2) Deapth first search
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