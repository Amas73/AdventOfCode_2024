fn = open('input_07_test.txt','r')
fn = open('input_07.txt','r')

data = [r.strip('\n') for r in fn.readlines()] 
equations = [r.split(": ") for r in data]

tot1 = 0
tot2 = 0

def checkEquations(calcs, part=1):
  total = 0
  for result, constants in calcs:
    r = int(result)
    vals = [int(x) for x in constants.split(" ")]
    calculatedValues = [vals[0]]
    for x in vals[1:]:
      tempValues = []
      for v in calculatedValues:
        tempValues.append(v+x)
        tempValues.append(v*x)
        if part == 2:
          tempValues.append(int(str(v)+str(x)))
      calculatedValues = tempValues[:]
    
    valid = False
    for v in calculatedValues:
      if v == r:
        valid = True
    if valid:
      total += r
  return total

tot1 = checkEquations(equations)

print (f"Day 07 part 1 value is: {tot1}")

tot2 = checkEquations(equations,part=2)
print (f"Day 07 part 2 value is: {tot2}")
