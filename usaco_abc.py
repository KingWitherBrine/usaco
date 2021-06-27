def solve(nums):
    nums.sort()
    for a in nums:
        for b in nums:
            for c in nums:
                if a+b in nums and b+c in nums and c+a in nums and a+b+c in nums:
                    return a, b, c

if __name__ == "__main__":
    with open(0) as f:
        nums = list(map(int, f.readline().strip().split()))
    print(*solve(nums))