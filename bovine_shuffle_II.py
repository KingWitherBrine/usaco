def cow_dance(positions, ids):
    initial_pos = [0] * len(positions)
    for i in range(len(positions)):
        index = positions.index(positions.index(positions.index(i + 1) + 1) + 1)
        initial_pos[index] = ids[i]
    return initial_pos

if __name__ == "__main__":
    with open(0) as f:
        num = int(f.readline())
        positions, ids = [list(map(int, line.strip().split())) for line in f]
        print(*cow_dance(positions, ids), sep="\n")