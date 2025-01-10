from pygame import Vector2
from pygame import Rect
from copy import deepcopy

fn = open('2024\\input_14_test.txt','r')
fn = open('2024\\input_14.txt','r')

data = [r.strip('\n') for r in fn.readlines()]
bots = [[v.split(',') for v in a] for a in [[x.split("=")[1] for x in r.split(" ")] for r in data]]
#grid size
w = 101
h = 103
ebhq = [[0 for x in range(w)] for y in range(h)]
area = Rect((0,0), (w,h))

robots = []
for r in bots:
  tmp = []
  for x,y in r:
    tmp.append(Vector2(int(x),int(y)))
  robots.append(tmp)

tot1 = 1
tot2 = 0

def travel(grid, pos, vel, n):
  if n == 0:
    #print(pos)
    grid[int(pos.y)][int(pos.x)] += 1
    return
  n -= 1
  pos += vel
  if not area.collidepoint(pos):
    if pos.x < 0:
      pos.x += w
    if pos.x >= w:
      pos.x -= w
    if pos.y < 0:
      pos.y += h
    if pos.y >= h:
      pos.y -= h
  travel(grid, pos, vel, n)

finishPos = deepcopy(ebhq)
for p, v in robots:
  travel(finishPos, p, v, 100)

hw, hh = w // 2, h // 2
q1 = sum([sum(r[:hw]) for r in finishPos[:hh]])
q2 = sum([sum(r[hw+1:]) for r in finishPos[:hh]])
q3 = sum([sum(r[:hw]) for r in finishPos[hh+1:]])
q4 = sum([sum(r[hw+1:]) for r in finishPos[hh+1:]])

for val in [q1,q2,q3,q4]:
  tot1 *= val

print (f"Day 14 part 1 value is: {tot1}")
print (f"Day 14 part 2 value is: {tot2}")
