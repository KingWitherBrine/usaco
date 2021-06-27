from itertools import permutations as perms

def solve(n, nums):
    lst = []
    for i in range(1, n):
        lst.append(list(perms(nums, i)))
    new_lst = [[n] for n in nums]
    for i in lst:
        for j in i:
            if sum(j)/len(j) in j and sorted(j) not in new_lst:
                new_lst.append(sorted(j))
    return len(new_lst)
if __name__ == "__main__":
    with open(0) as f:
        n = int(f.readline().strip())
        nums = list(map(int, f.readline().strip().split()))
    print(solve(n, nums))