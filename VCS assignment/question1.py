input = [5, 3, 2, 8, 4, 5, 2, 1, 9, 5, 3]
set1 = set(input)

for val in set1:
    input.remove(val)
input.sort()

output = list(set1) + input
print(output)