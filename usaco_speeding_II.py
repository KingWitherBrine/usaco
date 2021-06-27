import copy

def solve(road_matrix, bessie_matrix):
    road_count = 0
    bessie_count = 0
    new_road_matrix = copy.deepcopy(road_matrix)
    new_bessie_matrix = copy.deepcopy(bessie_matrix)
    for i in range(len(new_road_matrix)):
        new_road_matrix[i][0] = road_count
        road_count += road_matrix[i][0]
    for i in range(len(new_bessie_matrix)):
        new_bessie_matrix[i][0] = bessie_count
        bessie_count += bessie_matrix[i][0]
    for i in range(len(new_bessie_matrix))
    return new_road_matrix, road_count, new_bessie_matrix, bessie_count

if __name__ == "__main__":
    with open(0) as f:
        road, bessie = map(int, f.readline().strip().split())
        road_matrix = [list(map(int, f.readline().strip().split())) for i in range(road)]
        bessie_matrix = [list(map(int, f.readline().strip().split())) for i in range(road)]
    print(solve(road_matrix, bessie_matrix))