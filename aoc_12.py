from copy import copy

fn = open('input_12_test.txt','r')
#fn = open('input_12.txt','r')

data = [[x for x in r.strip('\n')] for r in fn.readlines()]
w = len(data[0])
h = len(data)

tot1 = 0
tot2 = 0
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

counted = [[0]*w]*h

def plot(grid, x, y, type):
  if (x < 0 or x >= w or y < 0 or y >= h or grid[y][x] != type or counted[y][x] > 0):
    return
  if grid[y][x] == type:
    counted[y][x] = 1
    
  for dx, dy in directions:
    plot(grid, x + dx, y + dy, type)



print (f"Day 12 part 1 value is: {tot1}")

print (f"Day 12 part 2 value is: {tot2}")

