from pygame import Vector2
from copy import deepcopy

fn = open('2024\\input_14_test.txt','r')
#fn = open('2024\\input_14.txt','r')

data = [r.strip('\n') for r in fn.readlines()]
bots = [[v.split(',') for v in a] for a in [[x.split("=")[1] for x in r.split(" ")] for r in data]]
#grid size
w = 101
h = 103
ebhq = [[0 for x in range(w)] for y in range(h)]

robots = []
for r in bots:
  tmp = []
  for x,y in r:
    tmp.append(Vector2(int(x),int(y)))
  robots.append(tmp)

tot1 = 0
tot2 = 0

def travel(grid, pos, vel, n):
  if n == 0:
    grid[pos.y][pos.x] += 1
    return
  n -= 1
  pos += vel
  

print (f"Day 14 part 1 value is: {tot1}")
print (f"Day 14 part 2 value is: {tot2}")
