# a) [S_i belongs to [1; N_slots]] for i in [1; N_disciplines]]

import math
from random import randint, random


class TimetablingProblem:
    def __init__(self, slots, disciplines, students, enrollments):
        self.slots = slots
        self.disciplines = disciplines
        self.students = students
        self.enrollments = enrollments
    
    def incompatibilities_table(self):
        table = [[0 for j in range(self.disciplines)] for i in range(self.disciplines)]
        for d1 in range(self.disciplines):
            s1 = set(self.enrollments[d1])
            for d2 in range(d1+1, self.disciplines):
                s2 = set(self.enrollments[d2])
                both = s1.intersection(s2)
                size = len(both)
                table[d1][d2], table[d2][d1] = size, size
        return table


    
    def from_input_file(path):
        input_file = open(path, 'r')
        data = [i.split(' ') for i in input_file.read().split('\n')]
        header = data[0]
        slots = int(header[0])
        disciplines = int(header[1])
        students = int(header[2])
        enrollments = []
        for i in range(1, disciplines+1):
            enrollments.append([int(i) for i in data[i]])
        
        return TimetablingProblem(slots, disciplines, students, enrollments)

class TimetablingProblemSolver:
    def __init__(self, tt):
        self.tt = tt
        self.itable = tt.incompatibilities_table()

    def random_solution(self):
        return [randint(1, self.tt.slots) for d in range(self.tt.disciplines)]
    
    def evaluate_solution(self, solution):
        result = 0
        for d1 in range(self.tt.disciplines-1):
            for d2 in range(d1+1, self.tt.disciplines):
                if solution[d1] == solution[d2]:
                    result += self.itable[d1][d2]
        return result
    
    def neighbours(self, solution):
        results = []
        for d in range(self.tt.disciplines):
            for s in range(1, self.tt.slots):
                if s != solution[d]:
                    l = solution.copy()
                    l[d] = s
                    results.append(l)
        return results
    
    def best_neighbour(self, neighbours):
        result = None
        best = math.inf
        for n in neighbours:
            v = self.evaluate_solution(n)
            if v < best:
                result = n
                best = v
        return result, best
    
    def hill_climbing(self, initial):
        current = initial
        c_value = self.evaluate_solution(initial)
        while 1:
            neighbour, n_value = self.best_neighbour(self.neighbours(current))
            if n_value >= c_value:
                return current
            print(n_value)
            current = neighbour
            c_value = n_value

def main():
    tt = TimetablingProblem.from_input_file("./input.txt")
    solver = TimetablingProblemSolver(tt)
    print(solver.hill_climbing(solver.random_solution()))

if __name__ == "__main__":
    main()