def qnt_diferent_ing (ing_dish_1, ing_dish_2):
    qnt = 0 # quantity of different ingridients in both dishes 
    for ingridient_1 in ing_dish_1:
        is_found = False
        for ingridient_2 in ing_dish_2:
            if ingridient_1 == ingridient_2:
                is_found = True
                break

        if not is_found:
            qnt += 1

    return qnt

qnt_test_cases = int(input())
for i in range(qnt_test_cases):
    ing_dish_1 = input().rstrip().split(" ")
    ing_dish_2 = input().rstrip().split(" ")
    total_ing = len(ing_dish_1)
    if qnt_diferent_ing(ing_dish_1, ing_dish_2) <= total_ing / 2:
        print("similar")
    else:
        print("dissimilar")
