# verificar se todas as ilhas possuim todos os ingredientes necessÃ¡rios
# se nÃ£o, "sad"
# se sim...
# verificar se todas as ilhas possuiem ingredientes Ãºnicos daquela ilha
# se sim, "all"
# se nao, "some"

# return true if all the islands can suply
# the ingredients required; false otherwise
def does_chef_have_all_ingredients(info_case, info_islands):

    # creating a list with all the ingredient
    ing_required = list(range(1, info_case[1] + 1))

    for island in info_islands:
        # looking for ingredients in each of the islands
        for i in range(len(island)):
            for j in range(len(ing_required)):
                if (island[i] == ing_required[j]):
                    # removing from the list if found
                    del ing_required[j]
                    break

    # return false if an item was not found in any of islands
    return len(ing_required) == 0

def is_island_neeeded(info_islands, ind_current_island):

    # copying the info_island without an specific island, the current one
    islands_copy = list(info_islands)
    del islands_copy[ind_current_island]

    # going through each ingredient to see if we find a unique one
    for ing_1 in info_islands[ind_current_island]:
        is_required = True # se assume it is not found in any other island
        for island_2 in islands_copy:
            for ing_2 in island_2:
                if ing_1 == ing_2:
                    # current ingredient not required anymore
                    # found on another island
                    is_required = False

        # if one of the ingreient is required, the whole island is as well
        if is_required:
            return True

    # no unique ingredient found
    # island not needed
    return False

qnt_test_cases = int(input())
for k in range(qnt_test_cases):
    # 0 - number of islands
    # 1 - quantity of ingredients
    info_case = [int(x) for x in input().rstrip().split(" ")]
    info_islands = [] # bidimensional array containing the info of every island
    for i in range(info_case[0]):
        island = [int(x) for x in input().rstrip().split(" ")]
        del island[0] # not needed
        info_islands.append(island)

    # if the chef can't cook
    if not does_chef_have_all_ingredients(info_case, info_islands):
        print("sad")
    else:
        are_all_necessary = True
        for i in range(len(info_islands)):
            if not is_island_neeeded(info_islands, i):
                are_all_necessary = False
                break

        if are_all_necessary:
            print("all")
        else:
            print("some")
