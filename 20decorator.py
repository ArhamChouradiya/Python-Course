"""ONE WAY TO DECORATE FUNCTION
def decor(fun):
    def inner():
        result=fun()
        return result*2
    return inner

def num():
    return 5

resultfun=decor(num)
print(resultfun())
"""

def decor(fun):
    def inner():
        result=fun()
        return result*2
    return inner

@decor  #ANOTHER WAY IS TO THROUGH @ decor function name above the function you want to decorate
def num():
    return 5

print(num())