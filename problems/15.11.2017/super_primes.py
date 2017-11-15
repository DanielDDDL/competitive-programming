def is_prime(number):
  if number <= 1:
    return False
  
  elif number <= 3:
    return True
  
  elif number % 2 == 0 or number % 3 == 0:
    return False
    
  i = 5
  while i * i <= number:
    if number % i == 0 or number % (i + 2) == 0:
      return False
    
    i += 6
    
  return True

def are_all_digits_primes(numbers):
  for i in range(len(numbers)):
    if not is_prime(numbers[i]):
      return False
  
  return True

while True:
  
  try:
    in_value = input().rstrip()
    whole_number = int(in_value)
    individual_numbers = [int(x) for x in in_value]
    
    if is_prime(whole_number):
      
      if (are_all_digits_primes(individual_numbers)):
        print("Super")
      else:
        print("Primo")
        
    else:
      print("Nada")
    
  except:
    break
