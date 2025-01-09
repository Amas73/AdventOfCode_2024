fn = open('2024\\input_13_test.txt','r')
fn = open('2024\\input_13.txt','r')

data = [r.strip('\n') for r in fn.readlines()]

tot1 = 0
tot2 = 0

def buttonSplit(str):
  x,y = str.split(':')[1].split(',')
  x = int(x[3:])
  y = int(y[3:])
  return [x,y]

config = []
for n in range(0,len(data),4):
  tmp = {}
  tmp['A'] = buttonSplit(data[n])
  tmp['B'] = buttonSplit(data[n+1])
  tmp['P'] = buttonSplit(data[n+2])
  config.append(tmp)

for n in config:
  Ax, Ay = n['A']
  Bx, By = n['B']
  Px, Py = n['P']

  buttonB = ((Ay * Px) - (Ax * Py)) / ((Ay * Bx) - (Ax * By))
  buttonA = (Px - (Bx * buttonB)) / Ax

  if buttonA > 0 and buttonA < 100 and buttonB >0 and buttonB < 100 and buttonA == int(buttonA) and buttonB == int(buttonB):
    tot1 += int((buttonA * 3) + buttonB)
  
  Px += 10000000000000
  Py += 10000000000000

  buttonB = ((Ay * Px) - (Ax * Py)) / ((Ay * Bx) - (Ax * By))
  buttonA = (Px - (Bx * buttonB)) / Ax

  if buttonA > 0 and buttonB >0 and buttonA == int(buttonA) and buttonB == int(buttonB):
    tot2 += int((buttonA * 3) + buttonB)

print (f"Day 13 part 1 value is: {tot1}")
print (f"Day 13 part 2 value is: {tot2}")
