def solve(nums):
    count = 0
    a, b = sorted((nums[0], nums[1]))
    x, y = sorted((nums[2], nums[3]))
    if y <= a or x >= b or b - a < abs(a-x) or b - a < abs(b-y):
        count += (b-a)
    else:
        count += abs(x-a)
        count += abs(y-b)
    return count

if __name__ == "__main__":
    with open('teleport.in') as f:
        nums = list(map(int, f.readline().strip().split()))
    with open('teleport.out', 'w') as f:
        print(str(solve(nums)), file=f)
    # with open(0) as f:
    #     nums = list(map(int, f.readline().strip().split()))
    # print(solve(nums))