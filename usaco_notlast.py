def solve(n, matrix):
    # find total production of cows
    logs = {}
    for cow, value in matrix:
        logs[cow] = logs.get(cow, 0) + value
    min_cows = []
    # find the minimum cows so that we can later see the second least
    for i in logs:
        if logs[i] == min(logs.values()):
            min_cows.append(i)
    # find second least cow
    second_min_cows = [None]
    second_min_val = float("inf")
    for i in logs:
        if i not in min_cows:
            if logs[i] - logs[min_cows[0]] < second_min_val:
                second_min_cows = [i]
                second_min_val = logs[i] - logs[min_cows[0]]
            if logs[i] - logs[min_cows[0]] == second_min_val:
                second_min_cows.append(i)
                second_min_val = logs[i] - logs[min_cows[0]]
    # see if special case, in which they all are the same
    if len(set(logs.values())) == 1:
        if n != 1:
            return "Tie"
        return matrix[0][0]
    if len(second_min_cows) > 1:
        return "Tie"
    return second_min_cows[0]

if __name__ == "__main__":
    # with open(0) as f:
    #     n = int(f.readline().strip())
    #     matrix = [list(f.readline().strip().split()) for i in range(n)]
    #     for i in matrix:
    #         i[1] = int(i[1])
    # print(solve(n, matrix))
    with open('notlast.in') as f:
        n = int(f.readline().strip())
        matrix = [list(f.readline().strip().split()) for i in range(n)]
        for i in matrix:
            i[1] = int(i[1])
    with open('notlast.out', 'w') as f:
        print(solve(n, matrix), file=f)