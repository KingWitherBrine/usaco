def solve(matrix):
    bucket_list = [0] * 1000
    for i in range(1000):
        for s, t, b in matrix:
            if i in range(s, t+1):
                bucket_list[i] += b
    return max(bucket_list)

if __name__ == "__main__":
    with open('blist.in', 'r') as f:
        n = int(f.readline().strip())
        matrix = [list(map(int, f.readline().strip().split())) for i in range(n)]
    with open('blist.out', 'w') as f:
        print(str(solve(matrix)), file=f)