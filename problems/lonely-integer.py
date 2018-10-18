a = [9, 1, 2, 3, 2, 9, 1, 7, 7, 3, 100]
a = [9, 1, 2, 3, 2, 9, 1, 7, 7]

# 1 Solution: Hash Map
# O(n) time
# O(n) space

hash_map = {}

for item in a:
    if item not in hash_map.keys():
        hash_map[item] = item
    else:
        hash_map.pop(item)

# print(hash_map.values())


# Lonely integer with bitwise
res = a[0]
for i in range(1, len(a)):
    res = res ^ a[i]

print(res)
