fn = open('2024\\input_04_test.txt','r')
fn = open('2024\\input_04.txt','r')

def wordCount(y,x):
    global data
    global word
    cnt = 0
    wordLen = len(word)
    if x + wordLen <= len(data[y]):
        cnt += int(word == data[y][x:x+wordLen])
        if y + wordLen <= len(data):
            testWord = ''
            for z in range(wordLen):
                testWord += data[y+z][x+z]
            cnt += int(word == testWord)
        if y >= wordLen -1:
            testWord = ''
            for z in range(wordLen):
                testWord += data[y-z][x+z]
            cnt += int(word == testWord)
    if x >= wordLen-1:
        cnt += int(word[::-1] == data[y][x-wordLen+1:x+1])
        if y + wordLen <= len(data):
            testWord = ''
            for z in range(wordLen):
                testWord += data[y+z][x-z]
            cnt += int(word == testWord)
        if y >= wordLen -1:
            testWord = ''
            for z in range(wordLen):
                testWord += data[y-z][x-z]
            cnt += int(word == testWord)
    if y + wordLen <= len(data):
        testWord = ''
        for z in range(wordLen):
            testWord += data[y+z][x]
        cnt += int(word == testWord)
    if y >= wordLen -1:
        testWord = ''
        for z in range(wordLen):
            testWord += data[y-z][x]
        cnt += int(word == testWord)
    return cnt

data = [r.strip('\n') for r in fn.readlines()]

word = 'XMAS'
tot1 = 0

for ln, row in enumerate(data):
    for n, char in enumerate(row):
        if char == word[0]:
            tot1 += wordCount(ln,n)

print (f"Day 04 part 1 value is: {tot1}")


def XwordCount(y,x):
    global data
    global word
    word1 = data[y-1][x-1] + data[y][x] + data[y+1][x+1]
    word2 = data[y+1][x-1] + data[y][x] + data[y-1][x+1]
    return int((word == word1 or word == word1[::-1]) and (word == word2 or word == word2[::-1]))

word = 'MAS'
tot2 = 0

for ln, row in enumerate(data):
    if ln > 0 and ln < len(data)-1:
        for n, char in enumerate(row):
            if n > 0 and n < len(row)-1:
                if char == 'A':
                    tot2 += XwordCount(ln,n)
    #                 c = XwordCount(ln,n)
    #                 print(c, end='')
    #             else:
    #                 print(".",end="")
    #         else:
    #             print(".",end="")
    #     print()
    # else:
    #     print("."*len(row))

print (f"Day 04 part 2 value is: {tot2}")