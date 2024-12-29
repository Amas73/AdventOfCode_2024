from pygame import Vector2
from pygame import Rect

fn = open('input_08_test.txt','r')
fn = open('input_08.txt','r')

data = [r.strip('\n') for r in fn.readlines()] 
tot1 = 0
tot2 = 0

h = len(data)
w = len(data[0])
grid = Rect((0, 0), (w, h))
nodes = {}
for y,row in enumerate(data):
  for x,val in enumerate(row):
    if val != ".":
      if val not in nodes:
        nodes[val] = []
      nodes[val].append(Vector2(x,y))

antiNodes = []
for n in nodes.values():
  for p1 in n[:(len(n)//2)+1]:
    for p2 in n[n.index(p1)+1:len(n)]:
      d = p2 - p1
      if grid.collidepoint(p2+d) and (p2+d) not in antiNodes:
        antiNodes.append(p2+d)
      if grid.collidepoint(p1-d) and (p1-d) not in antiNodes:
        antiNodes.append(p1-d)

tot1 = len(antiNodes)

print (f"Day 08 part 1 value is: {tot1}")

antiNodes = []
for n in nodes.values():
  for p1 in n[:(len(n)//2)+1]:
    for p2 in n[n.index(p1)+1:len(n)]:
      d = p2 - p1
      x=0
      while grid.collidepoint((np:=p2+(d*x))):
        if np not in antiNodes:
          antiNodes.append(np)
        x+=1
      x=0
      while grid.collidepoint((np:=p1-(d*x))):
        if np not in antiNodes:
          antiNodes.append(np)
        x+=1

tot2 = len(antiNodes)

print (f"Day 08 part 2 value is: {tot2}")
