def solve(pair1, pair2):
    temp_matrix = list(min(pair1, pair2))
    a, b = pair1
    c, d = pair2
    count = 0
    if temp_matrix == pair1:
        if temp_matrix[0] <= c <= temp_matrix[1]:
            temp_matrix[1] = max(d, temp_matrix[1])
        else:
            count += temp_matrix[1] - temp_matrix[0]
            temp_matrix = pair2
    else:
        if temp_matrix[0] <= a <= temp_matrix[1]:
            temp_matrix[1] = max(b, temp_matrix[1])
        else:
            count += temp_matrix[1] - temp_matrix[0]
            temp_matrix = pair1
    count += temp_matrix[1] - temp_matrix[0]
    if not (temp_matrix[0] < a < temp_matrix[1] or temp_matrix[0] < c < temp_matrix[1]):
        return count
    return temp_matrix[1] - temp_matrix[0]

if __name__ == "__main__":
    with open('paint.in', 'r') as f:
        pair1 = list(map(int, f.readline().strip().split()))
        pair2 = list(map(int, f.readline().strip().split()))
    with open('paint.out', 'w') as f:
        print(solve(pair1, pair2), file=f)
    # with open(0) as f:
    #     pair1 = list(map(int, f.readline().strip().split()))
    #     pair2 = list(map(int, f.readline().strip().split()))
    # print(solve(pair1, pair2))