list = [10, 20, 35, 50, 75, 80]
target = 70

def pair_sum(lst, y):
  ptr1 = 0
  ptr2 = len(lst) - 1

  while ptr1 < ptr2:
    if lst[ptr1] + lst[ptr2] == 70:
      return True 
      break
    elif lst[ptr1] + lst[ptr2] > 70:
      ptr2 -= 1
    elif lst[ptr1] + lst[ptr2] < 70:
      ptr1 += 1 
  return False

print(pair_sum(list, target))