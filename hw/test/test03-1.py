#1 c
#2 b, c
#3 c
#4 d
#5 d
#6 d

#7 54
from functools import partial

def foo(x=10, y=20, z=4):
    return x+y+z

print(partial(foo, foo())(10,10))

#8 d

#9 __mul__(self, x):
class A:
    def __init__(self, value):
        self.value=value

    def __mul__(self, x):
        return self.value*x.value


    def __str__(self):
        return 'Value:{}'.format(self.value)

class B:
    def __init__(self, value):
        self.value=value

a=A(100)
b=B(20)
print(a*b)

#10 클로저