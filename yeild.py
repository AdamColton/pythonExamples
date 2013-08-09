def squares(i):
    for x in range(i):
        yield x*x

def fibb(i):
    x,lx = 1,0
    while(i):
        yield x
        x,lx,i = x+lx, x, i-1

for i in fibb(10):
    print("Fibb: ", i)

for i in squares(10):
    print("Square: ", i)