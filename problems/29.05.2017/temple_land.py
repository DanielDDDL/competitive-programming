def is_simetrical (first_half, second_half):
    for i in range(len(first_half)):
        if first_half[i] != second_half[i]:
            return False

    return True

def is_height_incresing_valid(first_half):
    for i in range(1,len(first_half)):
        if first_half[i] - first_half[i - 1] != 1:
            return False

    return True

def is_valid (list_parts):
    first_half = list_parts[0:int(len(list_parts)/2)]
    second_half = list_parts[int(len(list_parts)/2) + 1:len(list_parts)]
    second_half = second_half[::-1]

    if is_simetrical(first_half, second_half):
        if is_height_incresing_valid(first_half):
            return first_half[0] == 1

    return False

num_cases = int(input())
for k in range(num_cases):
    # input
    num_parts = int(input())
    desc_parts = [int(x) for x in input().rstrip().split(" ")]
    # processing
    if (num_parts % 2 == 0):
        print("no")
    else:
        if is_valid(desc_parts):
            print("yes")
        else:
            print("no")
