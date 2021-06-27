def solve(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if sum(nums[i:j+1]) / len(nums[i:j+1]) in nums[i:j+1]:
                count += 1
    return count
if __name__ == "__main__":
    with open(0) as f:
        n = int(f.readline().strip())
        nums = list(map(int, f.readline().strip().split()))
    print(solve(nums))