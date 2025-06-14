from ortools.linear_solver import pywraplp


def main():
    N, M, K = map(int, input().split())
    a, b, c, d, e, f = map(int, input().split())
    s = [list(map(int, input().split())) for _ in range(N)]
    g = [list(map(int, input().split())) for _ in range(N)]
    t = list(map(int, input().split()))

    t = [x - 1 for x in t]

    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        print("Solver not available")
        return

    x = {}
    for i in range(N):
        for k in range(K):
            x[i, k] = solver.IntVar(0, 1, f'x_{i}_{k}')

    y = {}
    for j in range(M):
        for k in range(K):
            y[j, k] = solver.IntVar(0, 1, f'y_{j}_{k}')

    z1 = {}
    for i1 in range(N):
        for i2 in range(i1 + 1, N):
            for k in range(K):
                z1[i1, i2, k] = solver.IntVar(0, 1, f'z1_{i1}_{i2}_{k}')

                solver.Add(z1[i1, i2, k] <= x[i1, k])
                solver.Add(z1[i1, i2, k] <= x[i2, k])
                solver.Add(z1[i1, i2, k] >= x[i1, k] + x[i2, k] - 1)

    z2 = {}
    for i in range(N):
        for j in range(M):
            for k in range(K):
                z2[i, j, k] = solver.IntVar(0, 1, f'z2_{i}_{j}_{k}')

                solver.Add(z2[i, j, k] <= x[i, k])
                solver.Add(z2[i, j, k] <= y[j, k])
                solver.Add(z2[i, j, k] >= x[i, k] + y[j, k] - 1)

    for i in range(N):
        solver.Add(sum(x[i, k] for k in range(K)) == 1)

    for j in range(M):
        solver.Add(sum(y[j, k] for k in range(K)) == 1)

    for k in range(K):
        solver.Add(sum(x[i, k] for i in range(N)) >= a)
        solver.Add(sum(x[i, k] for i in range(N)) <= b)

    for k in range(K):
        solver.Add(sum(y[j, k] for j in range(M)) >= c)
        solver.Add(sum(y[j, k] for j in range(M)) <= d)

    for i in range(N):
        supervisor = t[i]
        for k in range(K):
            solver.Add(x[i, k] + y[supervisor, k] <= 1)

    for i1 in range(N):
        for i2 in range(i1 + 1, N):
            if s[i1][i2] < e:

                for k in range(K):
                    solver.Add(x[i1, k] + x[i2, k] <= 1)

    for i in range(N):
        for j in range(M):
            if g[i][j] < f:

                for k in range(K):
                    solver.Add(x[i, k] + y[j, k] <= 1)

    objective_terms = []

    for i1 in range(N):
        for i2 in range(i1 + 1, N):
            for k in range(K):
                if s[i1][i2] >= e:
                    objective_terms.append(s[i1][i2] * z1[i1, i2, k])

    for i in range(N):
        for j in range(M):
            for k in range(K):
                if g[i][j] >= f:
                    objective_terms.append(g[i][j] * z2[i, j, k])

    if objective_terms:
        solver.Maximize(sum(objective_terms))

    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:

        project_assignments = []
        teacher_assignments = []

        for i in range(N):
            for k in range(K):
                if x[i, k].solution_value() > 0.5:
                    project_assignments.append(k + 1)
                    break

        for j in range(M):
            for k in range(K):
                if y[j, k].solution_value() > 0.5:
                    teacher_assignments.append(k + 1)
                    break

        print(N)
        print(' '.join(map(str, project_assignments)))
        print(M)
        print(' '.join(map(str, teacher_assignments)))

    else:
        print("No optimal solution found")


if __name__ == '__main__':
    main()
