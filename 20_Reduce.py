from functools import reduce

price = [10,20,30,40,50,-90]

total = reduce(lambda x,y:x+y,price)

print(total)

