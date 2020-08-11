# 1
#주어진 기반 코드를 완성하여, 소수를 순서대로 반환하는 제네레이터를 구현하시오. 
# max_iter 횟수 만큼 출력하도록 하시오. 
# 함수를 구현하는 데에 사용한 모듈을 import하는 코드를 답안에 반드시 포함하시오.
import math

class PrimeNumberGenerator:
    def __init__(self, max_iter):
        self.max_iter = max_iter

    def __iter__(self):

        ve = self.max_iter
        count = 0
        num = 0

        while count<ve:
            num +=1
            if num <= 1:
                continue
            if num <= 3:
                count += 1
                yield num
            if num % 2 == 0 or num % 3 == 0:
                continue

            r = int(math.sqrt(num))
            f = 5
            while f <= r:
                if num % f == 0 or num % (f+2) == 0:
                    continue
                f += 6

            count += 1
            yield num
        return 
        
png = PrimeNumberGenerator(7)

pn = iter(png)

# print('EX3-1 -', next(pn))
# print('EX3-1 -', next(pn))

# 2
# 아래 기능을 수행하는 coroutine 함수를 구현하시오.

# coroutine 생성 시 정수 n을 입력받는다.
# 매번 실행 시 정수 x를 입력받는다.
# coroutine의 상태는 현재까지 입력받은 x값 중 가장 작은 수이다.
# coroutine은 n번까지 실행 후 종료된다.

def coroutine(n):
    num = 0
    count = 0
    numLi = []

    try: 
        while count<n+1:
            a = yield num
            numLi.append(a)
            count = count+1
            numLi.sort()
            print('-> coroutine received : ', numLi)
            print("numLi least >> ", numLi[0])

    except Exception:
        print('Except')

    finally:
        print("most small >> ", numLi[0])


# x = int(input("숫자를 입력하세요"))

# s1 = coroutine(x)
# next(s1)

# for i in range(x):
#     y = int(input("넣을 숫자를 입력"))
#     s1.send(y)

# s1.close



    
## 과제3.

# ----

# `__slots__`를 사용하여 최적화된 클래스를 구현하시오. 아래 조건을 만족하도록 구현하시오.

# - 클래스의 이름은 `Vector3D`로 한다.
# - 클래스의 멤버 변수는 `x`, `y`, `z`로 한다.
# - 클래스의 사칙연산을 구현한다.
#   - Vector3D 객체끼리의 합과 차는 `x`, `y`, `z`를 각각 합/차를 구해 Vector3D로 반환한다.
#   - Vector3D 객체끼리의 곱은 내적 (`x1 * x2 + y1 * y2 + z1 * z2`)을 숫자로 반환한다.
#   - Vector3D 객체끼리의 나눗셈은 `NaN`을 반환한다.
#   - 그 외에 모든 경우 `NotImplementedError` 예외를 발생시킨다.
# - 클래스를 print()로 출력할 경우, 아래 포맷으로 출력한다.
#   - `"Vector3D (%.3f, %.3f, %.3f)" % (x, y, z)`

class Vector3D:
    __slots__ = ['x', 'y', 'z']

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        try:
            x1 = (self.x+other.x)
            y1 = self.y+other.y
            z1 = self.z+other.z
            return (x1, y1, z1)
        except NotImplementedError: 
            print("not implemented")
     

    def __sub__(self, other):
        x1 = (self.x-other.x)
        y1 = self.y-other.y
        z1 = self.z-other.z
        return (x1, y1, z1)

    def __mul__(self, other):
        multi = self.x*other.x + self.y*other.y + self.z*other.z
        return multi

    def __truediv__(self, other):
        return "NaN"

    def __repr__(self):
        return ("Vector3D (%.3f, %.3f, %.3f)" % (self.x, self.y, self.z))

    def __context(self):
        print("error")


v1 = Vector3D(1,2,3)
v2 = Vector3D(3,4,5)
print(v1+v2)

print(dir(int))

## 과제4.

# ----

# 아래와 같은 기능을 하는 데코레이터 함수를 구현하시오. 함수를 구현하는 데에 필요한 모듈을 import하는 코드를 답안에 반드시 포함하시오.

# - 데코레이터 함수의 이름은 `coroutine`으로 한다.
# - primer의 데코레이터로 사용되며, 아래 기능을 수행한다.
#   - primer로부터 coroutine을 반환한다.
#   - coroutine의 첫 yield문까지 실행시켜, 곧바로 send가 가능하게 한다.
#   - 첫 yield문까지 실행하는 과정에서 시간이 1초 이상 소요될 경우, `TimeOutError` 예외를 발생시킨다.
from functools import wraps
import time

def coroutine(func):

    @wraps(func)
    def primer(*args, **kwargs):
        start = time.time()
        gen = func(*args, **kwargs)
        next(gen)
        end = time.time() - start
        if end>1:
            raise TimeoutError
        else:
            return gen
    return primer

@coroutine
def sumer():
    total = 0
    term = 0
    while True:
        term = yield total
        total += term


su = sumer() #시작함(next도 한 번 내부적으로 데코레이터에 의해 호출됨)

print('EX2-1 -', su.send(100))
print('EX2-2 -', su.send(40))
print('EX2-3 -', su.send(60))
