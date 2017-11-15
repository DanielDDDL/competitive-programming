while True:
    try:
        num_days = int(input())
        record = 0
        for i in range(num_days):
            # 0 - min and 1 - kil
            info_train = [int(x) for x in input().rstrip().split(" ")]
            current_time = info_train[1]/info_train[0]
            if current_time > record:
                record = current_time
                print(i + 1)

    except:
        break