while True:
    try:

        num_disc = int(input())
        hours = []

        int_values = []
        for i in range(num_disc):
            info_current_disc = [int(x) for x in input().rstrip().split(" ")]
            hours.append(info_current_disc[1])
            int_values.append(info_current_disc[0] * info_current_disc[1])

        # calculating things
        result = sum(int_values)/(sum(hours)*100)
        print("%0.04f" % result)

    except:
        break