from pygame import Vector2
from copy import copy

fn = open('input_06_test.txt','r')
#fn = open('input_06.txt','r')

data = [r.strip('\n') for r in fn.readlines()] 

tot1 = 0
tot2 = 0
guardChars = ["^",">","v","<"]

start = Vector2()
dir = Vector2(0,-1)
for y,row in enumerate(data):
  for char in guardChars:
    if char in row:
      start = Vector2(row.index(char),y)
      dir = dir.rotate(90*guardChars.index(char))
      break

loopBlockers = []
currentPosition = copy(start)
walkedPath = data[:]

def walkPath(grid,currentPos,loopSearch=False):
  global dir
  global loopBlockers
  updateChar = "X"
  loop = False
  if loopSearch:
    for x,r in enumerate(grid):
      grid[x] = r.replace(".","0").replace("^","0")
  else:
    for r in grid:
      print(r)
  while True:
    newPos = currentPos + dir
    if newPos.x <0 or newPos.y <0 or newPos.x >= len(grid[0]) or newPos.y >= len(grid) or (grid[int(currentPos.y)][:int(currentPos.x)].isnumeric() and int(grid[int(currentPos.y)][:int(currentPos.x)])>8):
      if loopSearch:
        updateChar = str(int(grid[int(currentPos.y)][int(currentPos.x)]) + 1)
      grid[int(currentPos.y)] = grid[int(currentPos.y)][:int(currentPos.x)] + updateChar + grid[int(currentPos.y)][int(currentPos.x)+1:]
      break
    if grid[int(newPos.y)][int(newPos.x)] == "#":
      dir = dir.rotate(90)
    else:
      if loopSearch:
        #print(grid[int(currentPos.y)], currentPos)
        updateChar = str(int(grid[int(currentPos.y)][int(currentPos.x)]) + 1)
      else:
        checkGrid = grid[:]
        checkPos = currentPos + dir
        checkGrid[int(checkPos.y)] = checkGrid[int(checkPos.y)][:int(checkPos.x)] + "#" + checkGrid[int(checkPos.y)][int(checkPos.x)+1:]
        _, looped = walkPath(checkGrid,currentPos,loopSearch=True)
        if looped:
          loopBlockers.append(newPos)
      grid[int(currentPos.y)] = grid[int(currentPos.y)][:int(currentPos.x)] + updateChar + grid[int(currentPos.y)][int(currentPos.x)+1:]
      currentPos = newPos
  return grid, loop

      # checkDir = dir.rotate(90)
      # proposedLoop = True
      # proposedPath = newPos
      # while True:
      #   proposedPath = proposedPath + checkDir
      #   if walkedPath[int(proposedPath.y)][int(proposedPath.x)] == "#":
      #     break
      #   elif walkedPath[int(proposedPath.y)][int(proposedPath.x)] != "X" or proposedPath.x <0 or proposedPath.y <0 or proposedPath.x >= len(walkedPath[0]) or proposedPath.y >= len(walkedPath):
      #     proposedLoop = False
      #     break
      # if proposedLoop:
      #   tot2 += 1
      #   loopBlockers.append(newPos)     
      
walkedPath = walkPath(data[:],currentPosition)

for row in walkedPath:
  tot1 += row.count("X")
  
print (f"Day 06 part 1 value is: {tot1}")


print (f"Day 06 part 2 value is: {tot2}")
