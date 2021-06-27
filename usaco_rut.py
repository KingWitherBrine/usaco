def solve(n, matrix):
    output = [0] * n
    temp_matrix = list(matrix[:])
    for i in range(n):
        if matrix[i][0] == "N":
            temp_matrix[i].append(temp_matrix[i][-1][:2] + (" " + (str(int(temp_matrix[i][-1][-1])+1))).split())
        else:
            temp_matrix[i].append((temp_matrix[i][-1][0] + (" " + str(int(temp_matrix[i][-1][1])+1)) + " " + temp_matrix[i][-1][2]).split())
    print(temp_matrix)
    

if __name__ == "__main__":
    with open(0) as f:
        n = int(f.readline().strip())
        matrix = [[list(f.readline().strip().split())] for i in range(n)]
    print(solve(n, matrix))