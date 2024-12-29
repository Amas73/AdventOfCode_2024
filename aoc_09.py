fn = open('input_09_test.txt','r')
fn = open('input_09.txt','r')

data = [r.strip('\n') for r in fn.readlines()][0]
tot1 = 0
tot2 = 0

storage = []
dataType = 'file'
id = 0
for v in data:
  if dataType == 'file':
    for i in range(int(v)):
      storage.append(id)
    dataType = 'freespace'
    id += 1
  else:
    for i in range(int(v)):
      storage.append('')
    dataType = 'file'

compactStorage = []
idx = 0
while idx < len(storage):
  val = storage[idx]
  if type(val) == str:
    while type(id:=storage.pop()) == str:
      pass
    compactStorage.append(id)
  else:
    compactStorage.append(val)
  idx += 1

#print (compactStorage)
for idx,id in enumerate(compactStorage):
  tot1 += idx * id

print (f"Day 09 part 1 value is: {tot1}")


# print (f"Day 09 part 2 value is: {tot2}")