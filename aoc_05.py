fn = open('2024\\input_05_test.txt','r')
fn = open('2024\\input_05.txt','r')

data = [r.strip('\n') for r in fn.readlines()] 
dataSplit = data.index("")
rules = [[int(x) for x in r.split("|")] for r in data[:dataSplit]]
produce = [[int(x) for x in r.split(",")] for r in data[dataSplit+1:]]

tot1 = 0
tot2 = 0

updates = []
incorrectUpdates = []
for row in produce:
    correct = True
    for y, x in enumerate(row[:-1]):
        if [x, row[y+1]] not in rules:
            correct = False
    if correct:
        updates.append(row)
    else:
        incorrectUpdates.append(row)

for row in updates:
    tot1 += row[len(row)//2]

print (f"Day 05 part 1 value is: {tot1}")

correctedUpdates = []
for row in incorrectUpdates:
    orderedRow = []
    while len(row) > 0:
        testValue = row.pop(0)
        notFound = True
        for x in row:
            if [testValue, x] not in rules:
                row.append(testValue)
                notFound = False
                break
        if notFound:
            orderedRow.append(testValue)
    correctedUpdates.append(orderedRow)

for row in correctedUpdates:
    tot2 += row[len(row)//2]


print (f"Day 05 part 2 value is: {tot2}")
