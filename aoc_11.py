from copy import copy

fn = open('input_11_test.txt','r')
fn = open('input_11.txt','r')

data = [[int(x) for x in r.strip('\n').split(" ")] for r in fn.readlines()][0]
stones = {int(d):data.count(d) for d in data}
tot1 = 0
tot2 = 0

def calc(value):
  if value == 0:
      result = [1]
  elif len(valStr:=str(value)) % 2 == 0:
      mid = len(valStr) // 2
      num1 = int(valStr[:mid])
      num2 = int(valStr[mid:])
      result = [num1, num2]
  else:
      result = [value * 2024]
  return result

def blink(values, n):
  for _ in range(n):
    newValues = {}
    for k in values.keys():
        for key in calc(k):
            newValues.setdefault(key,0)
            newValues[key] += values[k]
    values = copy(newValues)
  return values

n1 = 25
blinks = blink(stones, n1)
tot1 = sum(blinks.values())
#print(blinks)

print (f"Day 11 part 1 value is: {tot1}")

n2 = 75
blinks = blink(blinks, n2-n1)
tot2 = sum(blinks.values())

print (f"Day 11 part 2 value is: {tot2}")

