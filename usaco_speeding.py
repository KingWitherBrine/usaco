def solve(n, m, n_info, m_info):
    max_overspeed = -float("inf")
    n_info, m_info = sorted(n_info), sorted(m_info)
    for i in range(len(m_info)-1):
        for j in range(len(n_info)-1):
            if m_info[i][0] < n_info[j][0] < m_info[i+1][0]:
                if m_info[i][1] > n_info[j][1]:
                    max_overspeed = max(max_overspeed, m_info[i][1] - n_info[j][1])
    return max_overspeed
if __name__ == "__main__":
    with open(0) as f:
        n, m = map(int, f.readline().strip().split())
        n_info = [f.readline().strip().split() for i in range(n)]
        m_info = [f.readline().strip().split() for i in range(m)]
    print(solve(n, m, n_info, m_info))
