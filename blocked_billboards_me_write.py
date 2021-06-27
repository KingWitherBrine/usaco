def area(nums):
  x1, y1, x2, y2 = nums
  return abs(x2 - x1) * abs(y2 - y1)

def intersect(num1, num2):
  x1, y1, x2, y2 = num1
  x3, y3, x4, y4 = num2
  a1, b1 = max(x1, x3), max(y1, y3)
  a2, b2 = min(x2, x4), min(y2, y4)
  return 0 if a2 < a1 or b2 < b1 else area([a1, b1, a2, b2])

def solve(matrix):
  board1, board2, truck = matrix
  return area(board1) + area(board2) - intersect(board1, truck) - intersect(board2, truck)

if __name__ == '__main__':
  with open('billboard.in') as f:
    matrix = [list(map(int, line.split())) for line in f]
  result = solve(matrix)
  with open('billboard.out', 'w') as f:
    print(result, file=f)