fn = open('input_11_test.txt','r')
fn = open('input_11.txt','r')

data = [[int(x) for x in r.strip('\n').split(" ")] for r in fn.readlines()][0]
tot1 = 0
tot2 = 0

memo = {} 

def calc(value):
  global memo
  if value in memo:
      return memo[value]
  
  if value == 0:
      result = [1]
  elif len(valStr:=str(value)) % 2 == 0:
      mid = len(valStr) // 2
      num1 = int(valStr[:mid])
      num2 = int(valStr[mid:])
      result = [num1, num2]
  else:
      result = [value * 2024]
  memo[value] = result
  return result

def blink(values, n):
  for _ in range(n):
    newValues = []
    for value in values:
        newValues.extend(calc(value))
    values = newValues
  return values

n1 = 25
blinks = blink(data, n1)
tot1 = len(blinks)
print(memo)
#print(blinks)

print (f"Day 11 part 1 value is: {tot1}")

n2 = 75
blinks = blink(blinks, n2-n1)
tot2 = len(blinks)

print (f"Day 11 part 2 value is: {tot2}")

