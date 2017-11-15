# 4 4
# 1/6/2016 0 0 1 0
# 12/7/2016 1 1 1 0
# 5/10/2016 1 1 1 1
# 25/12/2016 0 0 0 0
# 5 3
# 20/9/2016 0 1 1 1 1
# 30/9/2016 1 0 1 1 1
# 1/10/2016 1 1 0 1 1

# receive the number of people and of possible days
# for each line receive the data and wether of not people will be able to go
# 1 if they can, 0 otherwise
# which mean that the day will be considered a good one if everybody says '1'
# if no day choosen is considered good, print 'Pizza antes de FdI'
# else, just print the day as it was entered

while True:
    try:

        # [0] number of people and [1] number of days
        info_test_case = [int(x) for x in input().rstrip().split(" ")]
        is_day_found = False

        for i in range(info_test_case[1]):

            # [0]day and then if people will be able to come
            info = input().rstrip().split(" ")

            if not is_day_found:
                is_current_day = True
                for j in range(1, len(info)):
                    if info[j] == "0":
                        is_current_day = False
                        break

                if is_current_day:
                    is_day_found = True
                    print(info[0])

        if not is_day_found:
            print("Pizza antes de FdI")

    except:
        break