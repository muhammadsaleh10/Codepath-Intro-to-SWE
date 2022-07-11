# l = [[0, 0, 1], [1, 1, 1], [4, 0, 0]]
# Output: 4

# l = [[100, 200, 300], [100, 200, 0], [200, 200, 200]]
# Output: 600

def max_sum(lst):

  temp = []
  max = 0
  
  for row in lst:
    sum = 0
    for el in row: 
      sum += el
    temp.append(sum)

  for i in temp:
    if i > max: 
      max = i

  return max
  
print(max_sum(l))