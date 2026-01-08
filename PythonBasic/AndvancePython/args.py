def sum(*args):
    print(args)
    total =0
    for item in args:
        total = total+item
    return total

print(sum(10,20,30,40))