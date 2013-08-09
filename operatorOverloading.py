class op_test(object):
    def __init__(self,val):
        self.val = val
        self.list = []
    def __eq__(self, other):
        return (self.val.lower() == other.val.lower())
    def append(self,x):
        self.list.append(x)
    def __getitem__(self,x):
        return self.list[x]

a = op_test("Adam")
b = op_test("adam")

print(a == b)

a.append('3')
a.append('1')
a.append('4')
a.append('1')
a.append('5')

print(a[2])
