def solve(n, a, b):
    different_breed_index = []
    count = 1
    for i in range(n):
        if a[i] != b[i]:
            different_breed_index.append(i)
    current_index = different_breed_index[0]
    for i in range(1, len(different_breed_index)):
        if different_breed_index[i] - 1 != different_breed_index[i-1]:
            count += 1
            current_index = different_breed_index[i]
    return count
    return different_breed_index

if __name__ == "__main__":
    # with open(0) as f:
    #     n = int(f.readline().strip())
    #     a = f.readline().strip()
    #     b = f.readline().strip()
    with open('breedflip.in') as f:
        n = int(f.readline().strip())
        a = f.readline().strip()
        b = f.readline().strip()
    with open('breedflip.out', 'w') as f:
        print(solve(n, a, b), file=f)