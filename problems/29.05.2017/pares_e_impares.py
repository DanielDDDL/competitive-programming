qnt_num = int(input())
even_numbers = []
odd_numbers = []

for i in range(qnt_num):
    num = int(input())
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

# sorting numbers
even_numbers.sort()
odd_numbers.sort()

for i in range(len(even_numbers)):
    print(even_numbers[i])

for j in range(len(odd_numbers)-1,-1,-1):
    print(odd_numbers[j])
