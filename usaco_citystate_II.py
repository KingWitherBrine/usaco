def solve(matrix):
    d = {}
    for city, abrev in matrix:
        d[city] = abrev
    count = 0
    for i in d: 
        for j in d:
            if d[i] == j[:2] and d[j] == i[:2]:
                count += 1
    return count//2
    
if __name__ == "__main__":
    with open(0) as f:
        n = int(f.readline().strip())
        matrix = [f.readline().strip().split() for i in range(n)]
    print(solve(matrix))
    # with open('citystate.in') as f:
    #     n = int(f.readline().strip())
    #     matrix = [f.readline().strip().split() for i in range(n)]
    # with open('citystate.out', 'w') as f:
    #     print(solve(matrix), file=f)