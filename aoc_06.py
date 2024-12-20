from pygame import Vector2
from copy import copy

fn = open('2024\\input_06_test.txt','r')
#fn = open('2024\\input_06.txt','r')

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
currentPos = copy(start)
walkedPath = data[:]
while True:
    newPos = currentPos + dir
    if newPos.x <0 or newPos.y <0 or newPos.x >= len(walkedPath[0]) or newPos.y >= len(walkedPath):
        walkedPath[int(currentPos.y)] = walkedPath[int(currentPos.y)][:int(currentPos.x)] + "X" + walkedPath[int(currentPos.y)][int(currentPos.x)+1:]
        break
    if walkedPath[int(newPos.y)][int(newPos.x)] == "#":
        dir = dir.rotate(90)
    else:
        checkDir = dir.rotate(90)
        proposedLoop = True
        proposedPath = newPos
        while True:
            proposedPath = proposedPath + checkDir
            if walkedPath[int(proposedPath.y)][int(proposedPath.x)] == "#":
                break
            elif walkedPath[int(proposedPath.y)][int(proposedPath.x)] != "X" or proposedPath.x <0 or proposedPath.y <0 or proposedPath.x >= len(walkedPath[0]) or proposedPath.y >= len(walkedPath):
                proposedLoop = False
                break
        if proposedLoop:
            tot2 += 1
            loopBlockers.append(newPos)       
        walkedPath[int(currentPos.y)] = walkedPath[int(currentPos.y)][:int(currentPos.x)] + "X" + walkedPath[int(currentPos.y)][int(currentPos.x)+1:]
        currentPos = newPos
    
for row in walkedPath:
    tot1 += row.count("X")
    
print (f"Day 06 part 1 value is: {tot1}")

# for pt in loopBlockers:
#     print(pt)

print (f"Day 06 part 2 value is: {tot2}")
