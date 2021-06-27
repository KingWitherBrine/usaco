# def solve(a, dct, greatest):
#   nums_dict = {}
#   for i in range(greatest):
#     nums_dict[i] = False
#   for i in dct.items():
#     for j in range(i[0], i[1]):
#       nums_dict[j] = True
#   lst = []
#   for i in dct:
#     num_dict1 = nums_dict.copy()
#     for j in range(i, dct[i]):
#       num_dict1[j] = False
#     count = 0
#     for val in num_dict1.values():
#       if val == True:
#         count += 1
#     lst.append(count)
#   return lst
# # print(solve(3, {5: 9, 1: 4, 3: 7}, 9))
# # Debugged using Python Tutor

# if __name__ == "__main__":
#   with open(0) as f:
#     a = int(f.readline().strip())
#     lst = [list(map(int, f.readline().strip().split())) for i in range(a)]
#     dct = {}
#     for i in lst:
#       dct[i[0]] = i[1]
#       greatest = max(dct.values())
#     # found lambda use at:
#     # https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/ 
#     # and https://stackoverflow.com/questions/13669252/what-is-key-lambda
#     print(solve(a, dct, greatest))
print(7)