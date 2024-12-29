import sys,os,re,itertools,time,copy,string
from utils import *
os.system('color & cls')

rawdata = [[c for c in r.strip()] for r in open('input_06.txt','rt').readlines()]
w,h = len(rawdata[0]),len(rawdata)
lim = 0

for y in range(h):
  for x in range(w):
    if rawdata[y][x]=='.': rawdata[y][x]='0'
    if rawdata[y][x]=='^': 
      rawdata[y][x]='0'
      start = (x,y)

newdata = copy.deepcopy(rawdata)
pos = copy.deepcopy(start)    
print(f'\033[?25l')

spots = set()

def traverse(doloop = False):
  global pos
  d = 'N'
  left,loop = False,False
  while not left and not loop:
    newpos = (pos[0]+dir[d][0],pos[1]+dir[d][1])
    if newpos[0]<0 or newpos[0] >= w or newpos[1] < 0 or newpos[1] >= h: left = True
    else:
      if newdata[newpos[1]][newpos[0]] in ['#','X']:
        match d:
          case 'N': d = 'E'
          case 'E': d = 'S'
          case 'S': d = 'W'
          case 'W': d = 'N'
      else:
        spots.add(newpos)
        newdata[pos[1]][pos[0]] = str(int(newdata[pos[1]][pos[0]])+1)
        if doloop and int(newdata[pos[1]][pos[0]])>9: loop = True
        pos = newpos
  return left,loop
  
def display(delay=0):
  for y in range(1,h+1):
    for x in range(1,w+1):
      c = newdata[y-1][x-1]
      match c:
        case '#': put(c,x,y,93)
        case 'X': put(c,x,y,97)
        case i if i in string.digits: put(i,x,y,35)
        case '^': put(c,x,y,35)
        case _: put(c,x,y,31)
  time.sleep(delay)

traverse()
display()
print(f'\033[{h+2};{0}H',len(spots))    


for y in range(h):
  for x in range(w):
    if newdata[y][x] in string.digits:
      lim = max(lim,int(newdata[y][x]))

blocks = copy.deepcopy(spots)
#blocks.remove(start)
loops = []
for b in blocks:
  newdata = copy.deepcopy(rawdata)
  pos = copy.deepcopy(start)    
  newdata[b[1]][b[0]] = 'X'
  _,loop = traverse(True)
  if loop: 
    loops.append(b)
    put('X',b[0],b[1],97)
  #display()
  
print(f'\033[{h+2};20H',len(loops))    
  