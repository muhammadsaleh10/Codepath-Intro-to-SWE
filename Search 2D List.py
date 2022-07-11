def search(lst):
  target = 1
  counter = 0
  for row in lst:
    if target in row:
      counter += 1
  return counter

print(search([[1,2,3], [1,1,1], [0,1,2]]))