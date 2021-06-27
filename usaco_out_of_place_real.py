def solve(n, nums):
    bessie_size = None
    bessie_index = None
    temp_set = set()
    lst = []
    new_nums = []
    
    for i in range(len(nums)):
        if i == n-1:
            bessie_index = i
            bessie_size = nums[i]
        if nums[i+1] < nums[i]:
            bessie_size = nums[i]
            bessie_index = i
    print(bessie_size)
    for i in nums:
        if i not in temp_set:
            new_nums.append(i)
            temp_set.add(i)
    print(bessie_size)
    temp_index = None
    for i in range(len(nums)-1):
        if nums[i] < bessie_index < nums[i+1]:
            temp_index = i+1
    return bessie_index - temp_index

if __name__ == "__main__":
    with open(0) as f:
        n = int(f.readline().strip())
        nums = [int(f.readline().strip()) for i in range(n)]
    print(solve(n, nums))