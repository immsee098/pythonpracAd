#1
def funcs(b):
  return b+1

smp = [0,1,2,3,4,5,6,7]

def mymap(func, a: list):
  return [func(s) for s in a]

print(mymap(funcs, smp))


#2
from functools import reduce

class Foo():
  def __init__(self, *args):
    self.li = list(args)
    # className = self.__class__.__name__
    # print(className)

  def __mul__(self):
    return reduce(lambda x, y: x * y, self.li)

  def __add__(self, oth):
    a1 = sum(self.li) 
    a2 = oth.__str__()
    return a1+int(a2)

  def __gt__(self, x):
      if self.__mul__() >= x.__mul__():
          return True
      else:
          return False

  def __lt__(self, x):
      if self.__mul__() <= x.__mul__():
          return True
      else:
          return False

  def __repr__(self):
      className = self.__class__.__name__
      argStr = ", ".join(str(a) for a in self.li)
      result = className+"("+argStr+")"
      return result

var = Foo(1,2,3,4)
var2 = Foo(10,20,30)
var3 = Foo(1,3,9)
print( type(Foo(1,3,9)))
a =[Foo(1,2), Foo(4,5), Foo(0,3)]
b=[var, var2, var3]
print(var2)
# print("multi", var.__mul__())
# print(var+var2)
# print(var > var2)
print(a)
a.sort()
print(a)

# print((dir(int)))


#3
def wrapper_func():
  dict_a = dict()

  def closer_func(k, v: int):
      nonlocal dict_a

      dict_a.setdefault(k, []).append(v)

      if hash(k) is False:
          return None

      dict_b = {key:sum(value) for key, value in dict_a.items()}
      return dict_b

  return closer_func


fu1 = wrapper_func()

print(fu1('a', 1))
print(fu1('a', 2))
print(fu1('b', 3))
print(fu1('b', 2))



#4
import time

def wrapper_func2(func):
  def time_check(*args):
    startTime = time.perf_counter()

    name = func.__name__
    arg_str = ', '.join(repr(arg) for arg in args)
    
    #time.sleep(11)

    endTime = time.perf_counter()-startTime

    print(['[%0.5fs] %s(%s)' % (endTime, name, arg_str)])
    alert_msg(endTime)

  
  def alert_msg(n):
    if n>=10: 
      print("to long!!")

  return time_check



@wrapper_func2
def time_func(seconds):
    time.sleep(seconds)

@wrapper_func2
def sum_func(*numbers):
    return sum(numbers)

@wrapper_func2
def fact_func(n):
    return 1 if n < 2 else n * fact_func(n-1)


time_func(20)