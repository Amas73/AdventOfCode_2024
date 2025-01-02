fn = open('input_09_test.txt','r')
fn = open('input_09.txt','r')

def swap(lst, idx1, idx2):
  lst[idx1], lst[idx2] = lst[idx2], lst[idx1]

data = [r.strip('\n') for r in fn.readlines()][0]
tot1 = 0
tot2 = 0

storage = []
files = {}
freespace = []
dataType = 'file'
id = 0
for v in data:
  p = int(v)
  if dataType == 'file':
    files[id] = p
    for i in range(p):
      storage.append(id)
    dataType = 'freespace'
    id += 1
  else:
    freespace.append([len(storage),p])
    for i in range(p):
      storage.append('.')
    dataType = 'file'

compactStorage = storage[:]
s = len(compactStorage)
prevIdx = s
for idx in range(s):
  val = compactStorage[idx]
  if type(val) == str:
    for l in range(prevIdx-1,idx,-1):
      if type(compactStorage[l]) == int:
        swap(compactStorage,idx, l)
        prevIdx = l+1
        break
for idx,id in enumerate(compactStorage):
  if type(id) == int:
    tot1 += idx * id

print (f"Day 09 part 1 value is: {tot1}")

def lastIndex(lst, val, start=0):
  for i in range(start-1,0,-1):
    if lst[i] == val:
      return i

optimisedStorage = storage[:]
lstIdx = len(optimisedStorage)
for fileId in range(len(files)-1,0,-1):
  storageBlks = files[fileId]
  for x in range(len(freespace)):
    idx, cnt = freespace[x]
    if cnt >= storageBlks:
      for i in range(idx,idx+storageBlks):
        lstIdx = lastIndex(optimisedStorage, fileId, lstIdx)
        if lstIdx > i:
          swap(optimisedStorage, i, lstIdx)        
      if cnt - storageBlks > 0:
        freespace[x] = [idx+storageBlks, cnt - storageBlks]
      else:
        freespace.pop(x)
      break  

for idx,id in enumerate(optimisedStorage):
  if type(id) == int:
    tot2 += idx * id

print (f"Day 09 part 2 value is: {tot2}")