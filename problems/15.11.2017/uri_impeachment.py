#receive the number of players
#receive the votes from those players
#decide weather of not the impeachment is going to happen
#if more than 2/3 of the votes are 'yes', output = 'impeachment'
#else, output = 'acusacao arquivada'
#votes: 1 = yes, 0 = no

while True:
    try:
        #input
        qnt_players = float(input())
        votes = [int(x) for x in input().rstrip().split(" ")]

        #calculating
        qnt_positive_votes = 0
        necessary_votes = (qnt_players / 3.0) * 2.0
        qnt_reached = False

        for i in range(len(votes)):
            if (votes[i] == 1):
                qnt_positive_votes += 1
                if(qnt_positive_votes >= necessary_votes):
                    qnt_reached = True
                    break

        if(qnt_reached):
            print("impeachment")
        else:
            print("acusacao arquivada")
        
    except:
        break

