def swap(string):
    return string[2:] + string[:2] 

def solve(matrix):
    """same thing as swap"""
    for i in range(len(matrix)):
        matrix[i] = f"{matrix[i][0][:2]}{matrix[i][1]}"
    """wrong solution"""
    # for i in range(len(matrix)):
        # if matrix[i][2:] + matrix[i][:2] in matrix and matrix[i] != matrix[i][2:] + matrix[i][:2]:
        #     count += 1
    
    # count = 0
    # return count//2
    # new_matrix = list(map(swap, matrix))
    # count += len(set(new_matrix).intersection(set(matrix)))
    # return count
    matrix = list(map(sorted, matrix))
    matrix = ["".join(sorted(i)) for i in matrix]
    return len(matrix) - len(set(matrix))
    # return len(matrix) - len(set(matrix))

if __name__ == "__main__":
    with open(0) as f:
        n = int(f.readline().strip())
        matrix = [f.readline().strip().split() for i in range(n)]
    print(solve(matrix))
    # with open('citystate.in') as f:
    #     n = int(f.readline().strip())
    #     matrix = [f.readline().strip().split() for i in range(n)]
    # with open('citystate.out', 'w') as f:
    #     print(solve(matrix), file=f)