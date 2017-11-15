while True:
    try:

        letters = input()
        input()  # not using this
        pos_letters = [int(x) for x in input().rstrip().split(" ")]

        message = ""
        for i in range(len(pos_letters)):
            message += letters[pos_letters[i] - 1]  # 1 is 1 :D

        print(message)

    except:
        break