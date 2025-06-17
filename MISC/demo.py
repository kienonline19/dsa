import copy
import random


class ThesisAssignmentSolver:
    def __init__(self, N, M, K, a, b, c, d, e, f, s_matrix, g_matrix, supervisors):
        self.N = N
        self.M = M
        self.K = K
        self.a, self.b = a, b
        self.c, self.d = c, d
        self.e = e
        self.f = f
        self.s_matrix = s_matrix
        self.g_matrix = g_matrix
        self.supervisors = supervisors

    def calculate_objective(self, x, y):
        total_similarity = 0

        for i in range(self.N):
            for j in range(i + 1, self.N):
                if x[i] == x[j]:
                    total_similarity += self.s_matrix[i][j]

        for i in range(self.N):
            for j in range(self.M):
                if x[i] == y[j]:
                    total_similarity += self.g_matrix[i][j]

        return total_similarity

    def is_feasible(self, x, y):

        thesis_count = [0] * (self.K + 1)
        teacher_count = [0] * (self.K + 1)

        for i in range(self.N):
            thesis_count[x[i]] += 1

        for j in range(self.M):
            teacher_count[y[j]] += 1

        for k in range(1, self.K + 1):
            if thesis_count[k] < self.a or thesis_count[k] > self.b:
                return False
            if teacher_count[k] < self.c or teacher_count[k] > self.d:
                return False

        for i in range(self.N):
            supervisor = self.supervisors[i] - 1
            if x[i] == y[supervisor]:
                return False

        for k in range(1, self.K + 1):
            theses_in_council = [i for i in range(self.N) if x[i] == k]
            for i in range(len(theses_in_council)):
                for j in range(i + 1, len(theses_in_council)):
                    if self.s_matrix[theses_in_council[i]][theses_in_council[j]] < self.e:
                        return False

        for i in range(self.N):
            teachers_in_council = [j for j in range(self.M) if y[j] == x[i]]
            for j in teachers_in_council:
                if self.g_matrix[i][j] < self.f:
                    return False

        return True

    def greedy_initial_solution(self):
        x = [0] * self.N
        y = [0] * self.M

        for i in range(self.N):
            x[i] = random.randint(1, self.K)

        for j in range(self.M):
            y[j] = random.randint(1, self.K)

        self.balance_councils(x, y)

        return x, y

    def balance_councils(self, x, y):
        max_iterations = 1000
        iteration = 0

        while iteration < max_iterations:
            thesis_count = [0] * (self.K + 1)
            teacher_count = [0] * (self.K + 1)

            for i in range(self.N):
                thesis_count[x[i]] += 1

            for j in range(self.M):
                teacher_count[y[j]] += 1

            over_thesis = []
            under_thesis = []

            for k in range(1, self.K + 1):
                if thesis_count[k] > self.b:
                    over_thesis.extend([k] * (thesis_count[k] - self.b))
                elif thesis_count[k] < self.a:
                    under_thesis.extend([k] * (self.a - thesis_count[k]))

            if over_thesis and under_thesis:
                from_council = over_thesis[0]
                to_council = under_thesis[0]

                for i in range(self.N):
                    if x[i] == from_council:
                        x[i] = to_council
                        break

            over_teacher = []
            under_teacher = []

            for k in range(1, self.K + 1):
                if teacher_count[k] > self.d:
                    over_teacher.extend([k] * (teacher_count[k] - self.d))
                elif teacher_count[k] < self.c:
                    under_teacher.extend([k] * (self.c - teacher_count[k]))

            if over_teacher and under_teacher:
                from_council = over_teacher[0]
                to_council = under_teacher[0]

                for j in range(self.M):
                    if y[j] == from_council:
                        y[j] = to_council
                        break

            if not over_thesis and not under_thesis and not over_teacher and not under_teacher:
                break

            iteration += 1

    def local_search(self, x, y, max_iterations = 1000):
        best_x, best_y = copy.deepcopy(x), copy.deepcopy(y)
        best_obj = self.calculate_objective(best_x, best_y) if self.is_feasible(best_x,
                                                                                best_y) else -float(
            'inf')

        for iteration in range(max_iterations):
            improved = False

            for i in range(self.N):
                original_council = x[i]
                for new_council in range(1, self.K + 1):
                    if new_council != original_council:
                        x[i] = new_council
                        if self.is_feasible(x, y):
                            obj = self.calculate_objective(x, y)
                            if obj > best_obj:
                                best_x, best_y = copy.deepcopy(x), copy.deepcopy(y)
                                best_obj = obj
                                improved = True
                        x[i] = original_council

            for j in range(self.M):
                original_council = y[j]
                for new_council in range(1, self.K + 1):
                    if new_council != original_council:
                        y[j] = new_council
                        if self.is_feasible(x, y):
                            obj = self.calculate_objective(x, y)
                            if obj > best_obj:
                                best_x, best_y = copy.deepcopy(x), copy.deepcopy(y)
                                best_obj = obj
                                improved = True
                        y[j] = original_council

            if not improved:
                break

            x, y = copy.deepcopy(best_x), copy.deepcopy(best_y)

        return best_x, best_y, best_obj

    def solve(self):
        best_solution = None
        best_objective = -float('inf')

        for attempt in range(50):
            x, y = self.greedy_initial_solution()

            x, y, obj = self.local_search(x, y)

            if obj > best_objective:
                best_objective = obj
                best_solution = (x, y)

        return best_solution


def parse_input():

    N, M, K = map(int, input().split())

    a, b, c, d, e, f = map(int, input().split())

    s_matrix = []
    for i in range(N):
        row = list(map(int, input().split()))
        s_matrix.append(row)

    g_matrix = []
    for i in range(N):
        row = list(map(int, input().split()))
        g_matrix.append(row)

    supervisors = list(map(int, input().split()))

    return N, M, K, a, b, c, d, e, f, s_matrix, g_matrix, supervisors


def main():
    N, M, K, a, b, c, d, e, f, s_matrix, g_matrix, supervisors = parse_input()

    solver = ThesisAssignmentSolver(N, M, K, a, b, c, d, e, f, s_matrix, g_matrix, supervisors)

    solution = solver.solve()

    if solution:
        x, y = solution
        print(N)
        print(' '.join(map(str, x)))
        print(M)
        print(' '.join(map(str, y)))
    else:
        print("Không tìm thấy nghiệm khả thi")


if __name__ == "__main__":
    main()
