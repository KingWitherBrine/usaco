def solve(nums):
    a = min(nums)
    nums.remove(a)
    b = min(nums)
    return a, b, max(nums) - a - b
if __name__ == "__main__":
    with open(0) as f:
        nums = list(map(int, f.readline().strip().split()))
    print(*solve(nums))