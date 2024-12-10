import re

fn = open('2024\\input_03_test.txt','r')
fn = open('2024\\input_03.txt','r')

data = fn.readlines()
text = "".join(data)
text2 = text

while (start := text2.find("don't()")) >0: 
   stop = text2.find("do()",start)
   if stop == -1:
    stop = len(text2)
   text2 = text2[:start]+text2[stop+4:]

results = re.findall('mul\(\d{1,3},\d{1,3}\)',text)
results2 = re.findall('mul\(\d{1,3},\d{1,3}\)',text2)

tot1 = 0
for inst in results:
  a,b = re.search('\d{1,3},\d{1,3}',inst)[0].split(",")
  tot1 += int(a) * int(b)
  
print (f"Day 03 part 1 value is: {tot1}")

tot2 = 0
for inst in results2:
  a,b = re.search('\d{1,3},\d{1,3}',inst)[0].split(",")
  tot2 += int(a) * int(b)
  
print (f"Day 03 part 2 value is: {tot2}")
