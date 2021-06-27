def solve(n, k, nums):
    nums = sorted(nums)
    count = 0
    for i in range(len(nums)):
        temp_count = 0
        for j in range(i+1, len(nums)):
            if (nums[j] - nums[i]) <= k:
                temp_count += 1
        count = max(count, temp_count)
    return count+1

if __name__ == "__main__":
    # with open(0) as f:
    #     n, k = map(int, f.readline().strip().split())
    #     nums = [int(f.readline().strip()) for i in range(n)]
    # print(solve(n, k, nums))
    with open('diamond.in') as f:
        n, k = map(int, f.readline().strip().split())
        nums = [int(f.readline().strip()) for i in range(n)]
    with open('diamond.out', 'w') as f:
        print(solve(n, k, nums), file=f)
