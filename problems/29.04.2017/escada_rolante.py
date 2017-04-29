while True:
    num_people = int(input())
    if num_people != 0:
        entrance_time = [int(x) for x in input().rstrip().split(" ")]
        total_time = 10
        for i in range(1, len(entrance_time)):
            if (entrance_time[i] - entrance_time[i - 1] >= 10):
                total_time += 10
            else:
                total_time += entrance_time[i] - entrance_time[i - 1]

        print (total_time)
    else:
        break
