# receive number of people
# receive min and max height
# output number of people who are allowed to use the rollecoast
# end of file

while True:
    try:

        # [0]number of people, [1]min height and [2]max height
        info = [int(x) for x in input().rstrip().split(" ")]

        num_allowed_people = 0
        for i in range(info[0]):
            current_height = int(input())
            if info[1] <= current_height <= info[2]:
                num_allowed_people += 1

        print(num_allowed_people)


    except:
        break