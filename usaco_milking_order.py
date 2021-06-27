def solve(n, m, k, hierarchy_cows, position_cows):
    lineup = [0 for i in range(n)]
    for cow, index in position_cows:
        lineup[index-1] = cow
    for i in range(len(lineup)):
        for j in range(len(hierarchy_cows)):
            if lineup[i] in hierarchy_cows:
                lineup[i-(hierarchy_cows.index(lineup[i])-j)] = hierarchy_cows[j]
    for i in range(lineup.index(0)):
        for j in position_cows:
            if lineup[lineup.index(0)-i] == j[0]:
                return (lineup.index(0)-i)+2

if __name__ == "__main__":
    with open(0) as f:
        n, m, k = map(int, f.readline().strip().split())
        hierarchy_cows = list(map(int, f.readline().strip().split()))
        position_cows = [list(map(int, f.readline().strip().split())) for i in range(k)]
    print(solve(n, m, k, hierarchy_cows, position_cows))
    # with open('milkorder.in') as f:
    #     n, m, k = map(int, f.readline().strip().split())
    #     hierarchy_cows = list(map(int, f.readline().strip().split()))
    #     position_cows = [list(map(int, f.readline().strip().split())) for i in range(k)]
    # with open('milkorder.out', 'w') as f:
    #     print(solve(n, m, k, hierarchy_cows, position_cows), file=f)