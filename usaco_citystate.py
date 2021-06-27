def solve(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(1, len(matrix)):
            if matrix[j][1] == matrix[i][0][:2] and matrix[i][1] == matrix[j][0][:2]:
                count += 1
    return count

if __name__ == "__main__":
    # with open(0) as f:
    #     n = int(f.readline().strip())
    #     matrix = [f.readline().strip().split() for i in range(n)]
    # print(solve(matrix))
    with open('citystate.in') as f:
        n = int(f.readline().strip())
        matrix = [f.readline().strip().split() for i in range(n)]
    with open('citystate.out', 'w') as f:
        print(solve(matrix), file=f)