from pygame import Vector2
from pygame import Rect
from copy import deepcopy

runTest = False

if runTest:
  fn = open('2024\\input_14_test.txt','r')
  w = 11
  h = 7
else:
  fn = open('2024\\input_14.txt','r')
  w = 101
  h = 103

data = [r.strip('\n') for r in fn.readlines()]
bots = [[v.split(',') for v in a] for a in [[x.split("=")[1] for x in r.split(" ")] for r in data]]
ebhq = [[0 for x in range(w)] for y in range(h)]
area = Rect((0,0), (w,h))

robots = []
for r in bots:
  tmp = []
  for x,y in r:
    tmp.append(Vector2(int(x),int(y)))
  robots.append(tmp)

def travel(pos, vel, n):
  global time
  time[100-n][int(pos.y)][int(pos.x)] += 1
  if n == 0:
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
  travel(pos, vel, n)

def safteyFactor(grid):
  hw, hh = w // 2, h // 2
  q1 = sum([sum(r[:hw]) for r in grid[:hh]])
  q2 = sum([sum(r[hw+1:]) for r in grid[:hh]])
  q3 = sum([sum(r[:hw]) for r in grid[hh+1:]])
  q4 = sum([sum(r[hw+1:]) for r in grid[hh+1:]])

  tot = 1
  for val in [q1,q2,q3,q4]:
    tot *= val
  return [tot,[q1,q2,q3,q4]]

def prntGrid(grid):
  for r in grid:
    print(r)

time = []
for n in range(101):
  time.append(deepcopy(ebhq))

for p, v in robots:
  travel(p, v, 100)

tot1 = safteyFactor(time[100])[0]

tot2 = 0
tmp = 0
for x in range(100):
  # t = safteyFactor(time[x])[1]
  # top = t[0] + t[1]
  # bot = t[2] + t[3]
  # if bot > (top*2.5):
  #   #tmp = t
  #   tot2 = x
  #   break
  print(f"\n\n   ----- for time of {x} seconds:")
  prntGrid(time[x])
  input()

print (f"Day 14 part 1 value is: {tot1}")
print (f"Day 14 part 2 value is: {tot2}")
