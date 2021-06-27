def solve(info):
    for i in range(len(info)):
        for j in range(len(info)):
            if info[i][0][j] == "B":
               b_i, b_j = i, j
            if info[i][0][j] == "R":
                r_i, r_j = i, j
            if info[i][0][j] == "L":
                l_i, l_j = i, j
    distance_br = abs(b_i - r_i) + abs(b_j - r_j)
    distance_bl = abs(b_i - l_i) + abs(b_j - l_j)
    distance_rl = abs(l_i - r_i) + abs(l_j - r_j)
    if (b_i == l_i or b_j == l_j) and distance_bl == distance_br + distance_rl:
        return distance_bl+1
    return distance_bl-1
    # return distance_br, distance_bl, distance_rl
    # return f"b_i is {b_i}, b_j is {b_j}, r_i is {r_i}, r_j is {r_j}, l_i is {l_i}, l_j is {l_j}"

if __name__ == "__main__":
    # with open(0) as f:
    #     info = [f.readline().strip().split() for i in range(10)]
    with open('buckets.in') as f:
        info = [f.readline().strip().split() for i in range(10)]
    with open('buckets.out', 'w') as f:
        print(solve(info), file=f)