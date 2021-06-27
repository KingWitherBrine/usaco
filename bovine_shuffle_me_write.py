def bovine_shuffle(positions, ids):
  initial_pos = [0] * len(positions) 
  for i in range(len(positions)):
    index = positions.index(positions.index(positions.index(i + 1) + 1) + 1)
    initial_pos[index] = ids[i]
  return initial_pos

if __name__ == '__main__':
  # with open('shuffle.in') as f:
  #     n = int(f.readline())
  #     positions, ids = [list(map(int, line.split())) for line in f]
  # with open('shuffle.out', 'w') as f:
  #     print(*bovine_shuffle(positions, ids), sep='\n', file=f)
  print(*bovine_shuffle([1, 3, 4, 5, 2], [1234567, 2222222, 3333333, 4444444, 5555555]), sep="\n")
  