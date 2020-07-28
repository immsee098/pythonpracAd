# Chapter02-2
# 파이썬 심화
# Special Method(Magic Method)
# 참조1 : https://docs.python.org/3/reference/datamodel.html#special-method-names
# 참조2 : https://www.tutorialsteacher.com/python/magic-methods-in-python

# 매직메소드 실습
# 파이썬의 중요한 핵심 프레임워크 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)

# 매직메소드 기초 설명
#미리 만들어놔서 그냥 사용할 수 있는 것들임-> __로 시작하는 미리 만들어진것들

# 기본형

print(int)

# 모든 속성 및 메소드 출력
print(dir(int))
print()
print()

# 사용
n = 100
print('EX1-1 -', n + 200)
#더한다는 + 자체를 이미 구현해두었다 -> __add__가 있기 때문
#+를 쓰는 순간 __add__로 호출되어서 출력됨
print('EX1-2 -', n.__add__(200))
print('EX1-3 -', n.__doc__)
#bool호출하면 __bool__이 나오는셈
print('EX1-4 -', n.__bool__(), bool(n))
print('EX1-5 - ', n * 100, n.__mul__(100))

print()
print()

# 클래스 예제1
class Student:
    def __init__(self, name, height):
        self._name = name
        self._height = height

    def __str__(self):
        return 'Student Class Info : {} , {}'.format(self._name, self._height)

    def __ge__(self, x):
        print('Called >> __ge__ Method.')
        if self._height >= x._height:
            return True
        else:
            return False

    def __le__(self, x):
        print('Called >> __le__ Method.')
        if self._height <= x._height:
            return True
        else:
            return False

    def __sub__(self, x):
        print('Called >> __sub__ Method.')
        return self._height - x._height



# 인스턴스 생성
s1 = Student('James', 181)
s2 = Student('Mie', 165)

#print(s1+s2)는 불가능함
#but s1.__height>s2.__height 은 가능함. 이미 int끼리는 비교 가능하게 내부적으로 만들어둠
#따라서 클래스에서 이 비교 메서드 __ge__ / __le__ 를 오버로딩해서 비교 가능하게 만드렁버릴수도 있음
#파이썬은 모든 것...심지어 int까지 내부적으로는 객체취급해서 가능하다

# 매직메소드 출력
print('EX2-1 -', s1 >= s2)
print('EX2-2 -', s1 <= s2)
print('EX2-3 -', s1 - s2)
print('EX2-4 -', s2 - s1)
print('EX2-5 - ', s1)
print('EX2-6 - ', s2)


#클래스 예제2

class Vector():
    
    def __init__(self, *args):
        '''Create a vector, example : v = Vector(1,2)'''
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        '''Returns the vector infomations'''
        return 'Vector(%r, %r)' % (self._x, self._y)

    def __add__(self, other):
        '''Returns the vector addition of self and other'''
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, y):
        return Vector(self._x * y, self._y * y)
    
    def __bool__(self):
        return bool(max(self._x, self._y))


# Vector 인스턴스 생성
v1 = Vector(3,5)
v2 = Vector(15, 20)
v3 = Vector()


# 매직메소드 출력
print('EX3-1 -', Vector.__init__.__doc__)
print('EX3-2 -', Vector.__repr__.__doc__)
print('EX3-3 -', Vector.__add__.__doc__)
print('EX3-4 -', v1, v2, v3)
print('EX3-5 -', v1 + v2)
print('EX3-6 -', v1 * 4)
print('EX3-7 -', v2 * 10)
print('EX3-8 -', bool(v1), bool(v2))
#기본값이 0이고 0은 boolean은 false됨
print('EX3-9 -', bool(v3))

print()
print()





