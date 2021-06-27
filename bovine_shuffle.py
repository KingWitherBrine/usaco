def cow_dance(pos, ids):
  pos.insert(0, 0)
  ids.insert(0, 0)
  result = [0] * len(pos)
  for i in range(1, len(pos)):
    index = pos.index(pos.index(pos.index(i)))
    result[index] = ids[i]
  return result[1:]
if __name__ == "__main__":
  with open(0) as f:
    num = int(f.readline())
    positions, ids = [list(map(int, line.strip().split())) for line in f]
  print(*cow_dance(positions, ids), sep="\n")