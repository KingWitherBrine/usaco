def solve(n, matrix):
    max_count = 0
    for i,  in range(len(matrix)):
        for j in range(len(matrix)):


if __name__ == "__main__":
    with open(0) as f:
        n = int(f.readline().strip().split())
        matrix = [list(map(int, f.readline().strip().split())) for i in range(n)]
    print(solve(n, matrix))