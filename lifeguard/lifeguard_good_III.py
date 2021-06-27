def solve_time(matrix): # gives the total time of a sorted matrix
    time = 0
    previous_s, previous_e = matrix[0]
    for i in range(1, len(matrix)):
        if previous_s < matrix[i][0] < previous_e:
            previous_e = max(matrix[i][1], previous_e)
        else:
            time += previous_e - previous_s
            previous_s, previous_e = matrix[i]
    time += previous_e - previous_s
    return time

def solve(matrix): # removes an item from each iteration and puts it into solve_time
    times = []
    for i in range(len(matrix)):
        new_matrix = matrix[:]
        new_matrix.remove(new_matrix[i])
        times.append(solve_time(new_matrix))
    return max(times)

if __name__ == "__main__":
    with open(0) as f:
        n = int(f.readline().strip())
        matrix = sorted([list(map(int, f.readline().strip().split())) for i in range(n)])
    print(solve(matrix))