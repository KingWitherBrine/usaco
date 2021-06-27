def solve(n, m, spotty_list, not_spotty_list):
    new_spotty_list, new_not_spotty_list = [[] for i in range(m)], [[] for i in range(m)]
    for i in range(n):
        for j in range(m):
            new_spotty_list[j] = [spotty_list[i][j]]
            new_not_spotty_list[j] = [not_spotty_list[i][j]]
    
    return new_spotty_list, new_not_spotty_list

    # for i in range(n):
        # for j in range(m):
            # if spotty_list[i][j] != not_spotty_list[i][j]:
                

if __name__ == "__main__":
    with open(0) as f:
        n, m = map(int, f.readline().strip().split())
        spotty_list = [list(f.readline().strip()) for i in range(n)]
        not_spotty_list = [list(f.readline().strip()) for i in range(n)]
    print(solve(n, m, spotty_list, not_spotty_list))