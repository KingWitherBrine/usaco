def solve(s, t):
    while t in s:
        s = s.replace(t, "")
    return s

if __name__ == "__main__":
    with open(0) as f:
        s = f.readline().strip()
        t = f.readline().strip()
    print(solve(s, t))
    # with open("censor.in") as f:
    #     s = f.readline().strip()
    #     t = f.readline().strip()
    # with open("censor.out", 'w') as f:
    #     print(solve(s, t), file=f)