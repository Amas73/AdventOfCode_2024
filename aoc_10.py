fn = open('input_10_test.txt','r')
fn = open('input_10.txt','r')

data = [r.strip('\n') for r in fn.readlines()]
tot1 = 0
tot2 = 0

trailheads = []
for row, val in enumerate(data):
  for col, v in enumerate(val):
    if v == '0':
      trailheads.append([col,row])

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def travel(grid, x, y, currHeight, endPositions):
  global directions
  if (x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid) or grid[y][x] != currHeight):
    return
  if grid[y][x] == '9':
    #if [x,y] not in endPositions:
      endPositions.append([x,y])
  for dx, dy in directions:
    travel(grid, x + dx, y + dy, str(int(currHeight)+1), endPositions)

def distinctList(lst):
  return list(set(map(tuple, lst)))

for x,y in trailheads:
  endPositions = []
  travel(data, x, y, '0', endPositions)
  #print (f"Path count: {len(endPositions)}")
  uniqueEndPositions = distinctList(endPositions)
  tot1 += len(uniqueEndPositions)
  tot2 += len(endPositions)

print (f"Day 10 part 1 value is: {tot1}")

print (f"Day 10 part 2 value is: {tot2}")
