def solve(n, nums):
    nums = sorted(nums)
    blast_radius = 1
    count_and_index = [0, -float('inf')]
    exploded = []
    for i in range(len(nums)):
        temp_count_and_index = [0, []]
        for j in range(len(nums)):
            if i != j:
                if abs(nums[j] - nums[i]) <= blast_radius:
                    temp_count_and_index[0] += 1
                    temp_count_and_index[1].append(j)
        
        if temp_count_and_index[0] >= count_and_index[0] and len(temp_count_and_index[1]) >= count_and_index[1]:
            count_and_index = [temp_count_and_index[0], len(temp_count_and_index[1])]
            if exploded == [] or len(temp_count_and_index[1]) == len(exploded[-1]):
                exploded.append(temp_count_and_index[1])  
            if exploded == [] or len(temp_count_and_index[1]) > len(exploded[-1]):
                exploded = [temp_count_and_index[1]]
        # count_and_index = max(count_and_index[0], temp_count_and_index[0]), max(count_and_index[1], len(temp_count_and_index[1]))
    return exploded
    # return count_and_index

if __name__ == "__main__":
    with open(0) as f:
        n = int(f.readline().strip())
        nums = [int(f.readline().strip()) for i in range(n)]
    print(solve(n, nums))

