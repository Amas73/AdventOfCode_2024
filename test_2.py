import copy

#rawdata = "77 515 6779622 6 91370 959685 0 9861".strip().split()
rawdata = "125 17".strip().split()

data = {int(d):rawdata.count(d) for d in rawdata}
print(data)

for i in range(6):
  newdata = {}
  for num in data.keys():
    match num:
      case 0: 
        newdata.setdefault(1,0)
        newdata[1] += data[0]
      
      case n if len(str(num))%2==0:
        snum = str(n)
        n1 = snum[:len(snum)//2]
        newdata.setdefault(int(n1),0)
        newdata[int(n1)] += data[n]
        n2 = snum[len(snum)//2:]
        newdata.setdefault(int(n2),0)
        newdata[int(n2)] += data[n]

      case _:
        n1 = str(num*2024)
        newdata.setdefault(int(n1),0)
        newdata[int(n1)] += data[num]

  data = copy.deepcopy(newdata)
  #print(i+1,sum(data.values()),len(data))
  print(data)