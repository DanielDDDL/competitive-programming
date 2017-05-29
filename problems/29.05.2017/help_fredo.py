import math

num_elements = int(input().rstrip())
array_elements = [int(x) for x in input().rstrip().split(" ")]

total_product = 1
for i in range(len(array_elements)):
    total_product *= array_elements[i]

print(math.ceil(total_product ** (1/num_elements)))