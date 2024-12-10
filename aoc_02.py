fn = open('2024\\input_02_test.txt','r')
fn = open('2024\\input_01.txt','r')

def variances(chkPosition,value):
  global dir
  global diff
  status = 'safe'
  diff = value-row[chkPosition]
  if chkPosition == 1:
    if diff == 0:
      dir = 0
    else:
      dir = diff // abs(diff)
  if diff !=0:
    newDir = diff // abs(diff)
  else:
    newDir = 0
  if newDir == 0 or newDir != dir or abs(diff)<1 or abs(diff)>3:
    status = 'unsafe'
  return status

data = [[int(x) for x in r.strip('\n').split(" ")] for r in fn.readlines()] 

tot1 = 0
tot2 = 0
for row in data:
  rowStatus = 'safe'
  for n, v in enumerate(row[:-1]):
    if variances(n+1,v) == 'unsafe':
      rowStatus = 'unsafe'
  tot1 += int(rowStatus == 'safe')

for row in data:
  rowStatus = 'safe'
  tollerance = 0
  for n, v in enumerate(row[:-1]):
    if variances(n+1,v) == 'unsafe':
      tollerance += 1
      if n+2 < len(row) and tollerance <2:
        if variances(n+2,v) == 'unsafe':
          rowStatus = 'unsafe'
  tot2 += int(rowStatus == 'safe')
  
print (f"Day 01 part 1 value is: {tot1}")
print (f"Day 01 part 1 value is: {tot2}")
