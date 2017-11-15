while True:
  
try:
    
	# 0 - number of people who did the test 
    
	# 1 - number of people interested on knowing their position
    
	info_test_case = [int(x) for x in input().rstrip().split(" ")]
    
    
	
	grades = []
    
	for i in range(info_test_case[0]):
      
		grades.append(int(input()))
      
    

	grades.sort(reverse=True)
    
    

	for i in range(info_test_case[1]):
      
		position = int(input())
      
		print(grades[position - 1])
      
   
   
  
except:
    
	break