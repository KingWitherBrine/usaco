def solve_time(matrix): # gives the total time of a sorted matrix
    # max_num = 0
    # for i in range(len(matrix)-1):
    #     count = 0
    #     if matrix[i][1] in list(range(matrix[i+1][0], matrix[i+1][1])):
    #         combined = (matrix[i][0], matrix[i+1][1])
    #         count += (matrix[i+1][1] - matrix[i][0])
    #     else:
    #         count += (matrix[i][1] - matrix[i][0]) + (matrix[i+1][1] - matrix[i+1][0])
    #     if count > max_num:
    #         max_num = count
    # return max_num
    pass

if __name__ == "__main__":
    with open(0) as f:
        n = int(f.readline().strip())
        matrix = sorted([list(map(int, f.readline().strip().split())) for i in range(n)])
    print(solve_time(matrix))