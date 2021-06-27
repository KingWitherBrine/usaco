def solve(n, matrix):
    # find total production of cows
    logs = {}
    for cow, value in matrix:
        logs[cow] = logs.get(cow, 0) + value
    # find min values and change to inf
    min_val = logs[min(logs, key=lambda k: logs[k])]
    for cow, value in logs.items():
        if value == min_val:
            logs[cow] = float("inf")
    # find second smallest val and check for duplicates
    second_min_key = min(logs, key=lambda k: logs[k])
    for cow, value in logs.items():
        if value == logs[second_min_key] and cow != second_min_key:
            return "Tie"
    return second_min_key

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