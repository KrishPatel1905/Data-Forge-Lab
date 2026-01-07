number = [10,20,30,40,50]

def square(x):
    return x*x

new = list(map(lambda x:x*x,number))
print(new)