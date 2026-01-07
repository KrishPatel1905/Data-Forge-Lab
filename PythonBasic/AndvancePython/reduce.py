from functools import reduce

number = [10,20,30,40,50]

def sum(a,b):
    return a+b


new = reduce(sum,number)

print(new)