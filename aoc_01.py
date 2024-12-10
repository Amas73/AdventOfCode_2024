fn = open('2024\\input_01_test.txt','r')
fn = open('2024\\input_01.txt','r')

data = fn.readlines()
list1, list2 = [], []
for row in data:
  values = row.strip("\n").split("  ")
  list1.append(int(values[0]))
  list2.append(int(values[1]))

list1.sort()
list2.sort()

tot1 = 0
for n, v in enumerate(list1):
  tot1 += abs(list2[n] - v)
  
print (f"Day 01 part 1 value is: {tot1}")

tot2 = 0
for v in list1:
  tot2 += v * list2.count(v)

print (f"Day 01 part 2 value is: {tot2}")
