def area(nums):
  x1, y1, x2, y2 = nums
  return (x2 - x1) * (y2 - y1)

def intersect(num1, num2):
  x1, y1, x2, y2 = num1
  x3, y3, x4, y4 = num2
  a1, b1 = max(x1, x3), max(y1, y3)
  a2, b2 = min(x2, x4), min(y2, y4)
  return 0 if a2 < a1 or b2 < b1 else area([a1, b1, a2, b2])

def point_in_rect(a, b, barn):
  x1, y1, x2, y2 = barn
  return x2 > a > x1 and y2 > b > y1

def solve(b1, b2):
  x1, y1, x2, y2 = b1 # lawnmower ad
  x3, y3, x4, y4 = b2 # Cow food ad
  count = 0
  if point_in_rect(x1, y1, b2):
    count += 1
  if point_in_rect(x2, y1, b2):
    count += 1
  if point_in_rect(x2, y2, b2):
    count += 1
  if point_in_rect(x1, y2, b2):
    count += 1
  if count >= 2:
    return area(b1) - intersect(b1, b2)
  return area(b1)
if __name__ == "__main__":
  with open(0) as f:
    matrix = [list(map(int, line.strip().split())) for line in f]
  print(solve(matrix[0], matrix[1]))