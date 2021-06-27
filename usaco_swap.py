def solve(n, k, swap_info):
    cows = list(range(1, n+1))
    for i in range(k):
        for j in swap_info:
            temp_cows = cows[j[0]-1:j[1]]
            temp_cows.reverse()
            cows[j[0]-1:j[1]] = temp_cows
    return cows

if __name__ == "__main__":
    # with open(0) as f:
    #     n, k = map(int, f.readline().strip().split())
    #     swap_info = [list(map(int, f.readline().strip().split())) for i in range(2)]
    # for i in solve(n, k, swap_info):
    #     print(i)
    with open('swap.in') as f:
        n, k = map(int, f.readline().strip().split())
        swap_info = [list(map(int, f.readline().strip().split())) for i in range(2)]
    with open('swap.out', 'w') as f:
        for i in solve(n, k, swap_info):
            print(i, file=f)