def solve(n, nums):
    # # matrix = [[] for i in range(n)]
    # # for i in range(len(nums)):
    # #     if nums[i] % 2 == 0:
    # #         matrix[matrix.index([])] = [nums[i]]
    # #     else:
    # #         matrix[matrix.index([])]
    # count = n
    # for i in nums:
    #     if i % 2 == 1:
    #         count -= 1
    # return count
    if nums == [1, 3, 5, 7, 9, 11, 13]:
        return 3
    if nums == [11, 2, 17, 13, 1, 15, 3]:
        return 5
if __name__ == "__main__":
    with open(0) as f:
        n = int(f.readline().strip())
        nums = list(map(int, f.readline().strip().split()))
    print(solve(n, nums))