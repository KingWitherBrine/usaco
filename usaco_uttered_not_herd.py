def solve(cowphabet, bessie_talk):
    count = 1
    slice_start = 0
    for i in range(len(bessie_talk)):
        if bessie_talk[i] not in cowphabet[slice_start+1:]:
            slice_start = cowphabet.index(bessie_talk[i])
            count += 1
            continue
        slice_start = cowphabet.index(bessie_talk[i])
    return count

if __name__ == "__main__":
    with open(0) as f:
        cowphabet = f.readline().strip()
        bessie_talk = f.readline().strip()
    print(solve(cowphabet, bessie_talk))