def solve_time(matrix): # gives the total time of a sorted matrix
    count = 0
    temp_tup = (matrix[0][0], matrix[0][1])
    for i in range(len(matrix)-1):
        if temp_tup[1] in range(matrix[i+1][0], matrix[i+1][1]+1):
            temp_tup = (temp_tup[0], matrix[i+1][1])
        else:
            count += temp_tup[1] - temp_tup[0]
            temp_tup = (matrix[i+1][0], matrix[i+1][1])
    count += temp_tup[1] - temp_tup[0]
    return count

def solve(matrix): # removes an item from each iteration and puts it into solve_time
    max_count = 0
    for i in range(len(matrix)):
        new_matrix = matrix[:]
        new_matrix.pop(i)
        count = solve_time(new_matrix)
        if count > max_count:
            max_count = count
    return max_count

if __name__ == "__main__":
    with open(0) as f:
        n = int(f.readline().strip())
        matrix = sorted([list(map(int, f.readline().strip().split())) for i in range(n)])
    print(solve_time(matrix))