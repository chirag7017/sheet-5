# find the output:
list=[1,3,5,7,9,11,13,15,17,19,21]
print(len(list))
print(list[-2:5:-1])
print(list[-2:])
print(list[-2::])
print(list[:-2])
print(list[::-2])
print(list[::-1])

# output:
# 11
# [19, 17, 15, 13]
# [19, 21]
# [19, 21]
# [1, 3, 5, 7, 9, 11, 13, 15, 17]
# [21, 17, 13, 9, 5, 1]
# # [21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]