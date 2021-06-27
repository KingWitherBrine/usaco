def solve(n, matrix):
    max_count = 0
    new_matrix = [[1, 2, 3]]
    for i in range(len(matrix)):
        a = matrix[i][0]
        b = matrix[i][1]
        c = a
        a = b
        b = c
        new_matrix.append([a, b, matrix[i][2]])
    return new_matrix

if __name__ == "__main__":
    with open(0) as f:
        n = int(f.readline().strip())
        matrix = [list(map(int, f.readline().strip().split())) for i in range(n)]
    print(solve(n, matrix))