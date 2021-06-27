def solve(n, nums):
    bessie_size = None
    bessie_index = None
    lst = []
    count = 0
    for i in range(len(nums)-1):
        if nums[i+1] < nums[i]:
            bessie_size = nums[i+1]
            bessie_index = i+1
    for i in range(1, len(nums)+1):
        new_nums = nums[:]
        temp_storage = nums[n - i] 
        new_nums[n - i] = new_nums[bessie_index]
        new_nums[bessie_index] = temp_storage
        if new_nums != nums:
            lst.append(new_nums)
    new_lst = []
    for i in lst:
        a = i.index(bessie_size)
        if (i[:a] == sorted(i[:a]) and i[a+1:] == sorted(i[a+1:])):
            new_lst.append(i)
    count += 1
    for i in range(len(new_lst[0])):
        
    return new_lst
    # return bessie_size, bessie_index

if __name__ == "__main__":
    with open(0) as f:
        n = int(f.readline().strip())
        nums = [int(f.readline().strip()) for i in range(n)]
    print(solve(n, nums))