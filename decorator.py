def test():
    print("this is a test: A")

def set_decorator(meth):
    def func(self):
        test()
        meth(self)
        return "This is a test: C"
    return func
    
class decTest:
    @set_decorator
    def decoratorMeth(self):
        print("this is a test: B")


objTest = decTest()
print("--Starting--")
print( objTest.decoratorMeth() )
print()
print("--Notice no test C--")
objTest.decoratorMeth()
print("--Done--")