from pygame import Vector2
from copy import copy

fn = open('2024\\input_06_test.txt','r')
fn = open('2024\\input_06.txt','r')

data = [r.strip('\n') for r in fn.readlines()] 

tot1 = 0
tot2 = 0
guardChars = ["^",">","v","<"]

start = Vector2()
dir = Vector2(0,-1)
for y,row in enumerate(data):
    for char in guardChars:
        if char in row:
            start = (row.index(char),y)
            dir = dir.rotate(90*guardChars.index(char))
            break

prevPos = copy(start)
walkedPath = data[:]
while True:
    newPos = prevPos + dir
    if newPos.x <0 or newPos.y <0 or newPos.x >= len(walkedPath[0]) or newPos.y >= len(walkedPath):
        break
    if walkedPath[int(newPos.y)][int(newPos.x)] == "#":
        dir = dir.rotate(90)
    else:
        walkedPath[int(newPos.y)] = walkedPath[int(newPos.y)][:int(newPos.x)] + "X" + walkedPath[int(newPos.y)][int(newPos.x)+1:]
        prevPos = newPos
    
for row in walkedPath:
    tot1 += row.count("X")
    print(row)
    
print (f"Day 06 part 1 value is: {tot1}")



print (f"Day 06 part 2 value is: {tot2}")
