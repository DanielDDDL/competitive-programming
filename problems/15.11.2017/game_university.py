# this one is easy, alright?
# you are going to receive a n number of lines and a code that represents you
# then comes n lines with 2 number on them: your code and a number that can be either 0 or 1
# count how many times each of these lines are equal to 'your_code 0'

while True:
    try:

        info_test_case = [int(x) for x in input().rstrip().split(" ")]
        
        number_gameplays = info_test_case[0]
        player_code = info_test_case[1]

        qnt_game_found = 0
        
        for i in range(number_gameplays):
    
            info = [int(x) for x in input().rstrip().split(" ")]
            if(info[0] == player_code and info[1] == 0):
                qnt_game_found += 1

        print(qnt_game_found)
        
    except:
        break
