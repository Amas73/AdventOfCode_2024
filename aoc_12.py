fn = open('2024\\input_12_test.txt','r')
fn = open('2024\\input_12.txt','r')

data = [r.strip('\n') for r in fn.readlines()]
w = len(data[0])
h = len(data)

tot1 = 0
tot2 = 0

regions = []
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
counted = [[[] for x in range(w)] for y in range(h)]

def printGrid(g):
  for a in g:
    print(a)

def safeCheck(grid, x,y,value):
  if x >= 0 and x < w and y >= 0 and y < h:
    return grid[y][x] == value
  return False

def travel(grid, x, y, currType):
  global region
  if (x >= 0 and x < w and y >= 0 and y < h and currType in counted[y][x]):
    return
  if (x < 0 or x >= w or y < 0 or y >= h or grid[y][x] != currType):
    region[1] +=1
    return
  region[0] += 1
  counted[y][x].append(currType)
 
  ### Identify corners for part 2
  if (x == 0 or not safeCheck(grid, x-1, y, currType)) and (y == 0 or not safeCheck(grid, x, y-1, currType)):  ## top left
    region[2] += 1
  if (x == w-1 or not safeCheck(grid, x+1, y, currType)) and (y == 0 or not safeCheck(grid, x, y-1, currType)):  ## top right
    region[2] += 1
  if (x == 0 or not safeCheck(grid, x-1, y, currType)) and (y == h or not safeCheck(grid, x, y+1, currType)):  ## bottom left
    region[2] += 1
  if (x == w-1 or not safeCheck(grid, x+1, y, currType)) and (y == h or not safeCheck(grid, x, y+1, currType)):  ## bottom right
    region[2] += 1
  if (x >= 0 and y >= 0 and x < w and y < h) and (not safeCheck(grid, x-1, y-1, currType) and safeCheck(grid, x, y-1, currType) and safeCheck(grid, x-1, y, currType)):   ## inside top left
    region[2] +=1
  if (x >= 0 and y >= 0 and x < w and y < h) and (not safeCheck(grid, x+1, y-1, currType) and safeCheck(grid, x, y-1, currType) and safeCheck(grid, x+1, y, currType)):   ## inside top right
    region[2] +=1
  if (x >= 0 and y >= 0 and x < w and y < h) and (not safeCheck(grid, x-1, y+1, currType) and safeCheck(grid, x, y+1, currType) and safeCheck(grid, x-1, y, currType)):   ## inside bottom left
    region[2] +=1
  if (x >= 0 and y >= 0 and x < w and y < h) and (not safeCheck(grid, x+1, y+1, currType) and safeCheck(grid, x, y+1, currType) and safeCheck(grid, x+1, y, currType)):   ## inside bottom right
    region[2] +=1
 
  for dx, dy in directions:
    travel(grid, x + dx, y + dy, currType)
  return region

for y, row in enumerate(data):
  for x, plant in enumerate(row):
    dirChr = '*'
    region = [0,0,0]
    if not counted[y][x]:
      regions.append(travel(data, x, y, plant))

for x,y,z in regions:
    tot1 += x*y
    tot2 += x*z

print (f"Day 10 part 1 value is: {tot1}")

print (f"Day 10 part 2 value is: {tot2}")
