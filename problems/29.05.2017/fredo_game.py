num_cases = int(input())
for k in range(num_cases):
    # 0 - number of initial ammo
    # 1 - number of obstacles
    info_case = [int(x) for x in input().rstrip().split(" ")]
    obstacles = [int(x) for x in input().rstrip().split(" ")]
    isPossible = True
    for i in range(len(obstacles)):
        if obstacles[i] == 0:
            info_case[0] -= 1
            if info_case[0] == 0 and i != (info_case[1] - 1):
                isPossible = False
                print("No", i + 1)
                break
        else:
            info_case[0] += 2

    if isPossible:
        print("Yes", info_case[0])
