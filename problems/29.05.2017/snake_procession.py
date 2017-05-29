def is_valid(snake_body):
    snake_body = snake_body.replace(".","") # removing all dots
    cont_ht = 0 # number of heads minus tails
    for i in range(len(snake_body)):
        if snake_body[i] == "H":
            cont_ht += 1
        elif snake_body[i] == "T":
            cont_ht -= 1

        if cont_ht < 0 or cont_ht > 1:
            return False

    return cont_ht == 0

# processing
num_rep = int(input())
for k in range(num_rep):
    snake_len = int(input().rstrip())
    snake_body = input().rstrip()
    if is_valid(snake_body):
        print("Valid")
    else:
        print("Invalid")
