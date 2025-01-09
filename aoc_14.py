fn = open('2024\\input_14_test.txt','r')
#fn = open('2024\\input_14.txt','r')

data = [r.strip('\n') for r in fn.readlines()]
robots = [[v.split(',') for v in a] for a in [[x.split("=")[1] for x in r.split(" ")] for r in data]]

tot1 = 0
tot2 = 0

def travel(grid, pos, vel, n):
    

print (f"Day 14 part 1 value is: {tot1}")
print (f"Day 14 part 2 value is: {tot2}")
