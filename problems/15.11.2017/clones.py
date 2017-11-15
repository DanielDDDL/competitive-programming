import math

while True:
    try:
        number_of_clones = int(input())
        result = math.log(number_of_clones,2)
        print(int(result))

    except:
        break
