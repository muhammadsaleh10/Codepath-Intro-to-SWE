book = [
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0]
]

row = int(input("Enter a row number from 0 to 4, where 0 is the farthest back row: "))
col = int(input("Enter desired seat numbers in this row from 0 to 7 where 0 is the left most seat (Use first_seat:last_seat+1 foramt when selecting multiple seats): "))

def bok(r, c):
  if book[r][c] == 0:
    book[r][c] = 1
    return "seat(s)", c, "in row", r, "have boon booked!"
  else:
    return "seat(s)", c, "in row", r, "are not available"

print(bok(row, col))