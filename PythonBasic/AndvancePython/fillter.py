def check(x):
    if x>18:
        return True
    else:
        return False
    
a = [15,0,45,787,1,15,16,19]

new = list(filter(check,a))

print(new)

