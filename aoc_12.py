fn = open('2024\\input_12_test.txt','r')
#fn = open('2024\\input_12.txt','r')

data = [r.strip('\n') for r in fn.readlines()]
w = len(data[0])
h = len(data)

tot1 = 0
tot2 = 0

fields = []
regions = []
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
emptyGrid = [[0 for x in range(w+2)] for y in range(h+2)]
counted = [[[] for x in range(w)] for y in range(h)]

def travel(grid, x, y, currType):
  global region
  if (x >= 0 and x < w and y >= 0 and y < h and currType in counted[y][x]):
    return
  if (x < 0 or x >= w or y < 0 or y >= h or grid[y][x] != currType):
    region[1] +=1
    region[2][y+1][x+1] = 1
    return
  region[0] += 1
  counted[y][x].append(currType)
  for dx, dy in directions:
    travel(grid, x + dx, y + dy, currType)
  return region

for y, row in enumerate(data[:1]):
  for x, plant in enumerate(row):
    region = [0,0,emptyGrid[:]]
    if not counted[y][x]:
      regions.append(travel(data, x, y, plant))

for x,y,grid in regions[:1]:
    tot1 += x*y
    for a in grid:
      print(a)


print (f"Day 10 part 1 value is: {tot1}")

print (f"Day 10 part 2 value is: {tot2}")
