from math import sqrt

# This is a set of demo code that uses a decorator
# to mimic some behavior of functional languages
# When the 'functional' decorator is applied to a
# function, it will remember every value it calculates
# and will never perform the same calculation
# twice. This is very useful for recursive functions.

def functional(func):
    def build(*x):
        try:
            if x not in func.D:              #check if value exists in the functions dictionary
                func.D[x] = func(*x)     #if its not there, calculate
        except:                          #if the function doesn't have a dictionary defined yet
            func.D = {}                  #create dictionary
            func.D[x] = func(*x)         #calculate value for x
        return func.D[x]                 #return value
    return build

@functional
def fac(x):
    if (x < 2):
        return 1
    return fac(x-1) * x

@functional
def fibb(x):
    if ( x < 2 ):
        return 1
    return fibb(x-1) + fibb(x-2)

@functional
def is_prime(x):
    for i in range(2,int(sqrt(x))):
        if is_prime(i) and ( x % i == 0 ):
            return False
    return True

@functional
def goofy(x,y):
    if x == 0:
        return y
    if y == 0:
        return x
    return goofy(x%y,x) + goofy(y%x, y)

print( goofy(6,5) )
print( fac(100) )
print( fibb(100) )
print( is_prime(10123468391) )
print( is_prime(10123468392) )