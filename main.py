def function(str1):
  
  sum = 0
  count = 0 
  lenght = 0

  for char in str1: 
    
    if char.isdigit() == True:
      char = int(char)
      count += 1
      sum = sum + char
      
    lenght = 0
    while char.isdigit() == True:
      lenght += 1
    
  print("Sum of digits: ", sum, "Average of the digits: ", sum/count, "Lenght of longest consecutive substring: ")
    
    
  