def solve(n, k, words):
    lst = [[] for _ in range(n)]
    count = 0
    current_index = 0
    for i in range(len(words)):
        if count+len(words[i]) <= k:
            lst[current_index].append(words[i])
            count += len(words[i])
        else:
            count = 0
            current_index += 1
            lst[current_index].append(words[i])
            count += len(words[i])
    return lst


if __name__ == "__main__":
    # with open(0) as f:
    #     n, k = map(int, f.readline().strip().split())
    #     words = f.readline().strip().split()
    with open('word.in') as f:
        n, k = map(int, f.readline().strip().split())
        words = f.readline().strip().split()
    with open('word.out', 'w') as f:
        for i in solve(n, k, words):
            if i != []:
                print(*i, file=f)