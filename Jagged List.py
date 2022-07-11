def is_jagged(list):
  lenght = len(list[1])
  for row in range(len(list)):
    if len(list[row]) != lenght:
      return "list is not Jagged"
  return True

print(is_jagged([[1,2,3], [4,5], [6,7,8]]))