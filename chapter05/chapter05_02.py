# Chapter05-2
# 파이썬 심화
# 파이썬 클래스 특별 메소드 심화 활용 및 상속
# Special Method, Class ABC(추상 클래스)

# class 선언
class VectorP(object):
    # private 선언
    def __init__(self, x, y):
        ##밑줄 두 개는 PRIVATE와 동일하게 작동
        self.__x = float(x)
            # if y<30:
            #     raise ValueError('dddd') -> return 안되지만 이건됨
        self.__y = float(y)

    def __iter__(self):
        return (i for i in (self.__x, self.__y)) # Generator
        #튜플로 받고있기때문..

    #이거 덕에 __에서 언더바 떼고 불러도 호출이됨
    #자바의 @Data 느낌인듯
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, v):
        self.__x = v

    @property
    def y(self):
        return self.__y

    #세터 역할만함
    @y.setter
    def y(self, v):
        #직접 접근해도 이거때매 y값이 비적합하면 걸러짐
        if v < -273:
            raise ValueError("Temperature below -273 is not possible")
        self.__y = v

# 객체 선언
v5 = VectorP(20, 40)

# print('EX1-2 -', v5.__x, v5.__y)

#처음 init을 받을 때 조건을 걸어주면 객체 생성 당시에는 1회 거름 가능
#그러나 v._y=10처럼 생성 후 직접 접근해서 변경해버릴수가 있어서 곤란해짐

# 일종의 파이썬용 bean같은 것
# 따라서 java의 getter setter 기능이 필요함->데코레이터 유

print('EX1-3 -',dir(v5), v5.__dict__)
#아래 언더바 __ 떼고 찍어야 찍힘
print('EX1-4 -', v5.x, v5.y) # 타 언어와 달리 근본적인 해결책 X, 파이썬 개발자 간의 암묵적 약속

#Getter/Setter 해두면 __뗴고 직접 접근해도 겟셋이 불러짐!!!

# Iter 확인
for v in v5:
    print('EX1-5 -', v)

print()
print()


# __slot__
# 파이선 인터프리터에게 통보
# 해당 클래스가 가지는 속성을 제한
###보통 인스턴스 속성을 dic로 가지는데 메모리를 꽤 잡아먹음
###따라서 set으로 바꿔서 다수 객체 생성 시 메모리 사용 공간 감소
# __dict__ 속성 최적화 -> 다수 객체 생성시 -> 메모리 사용(공간) 대폭 감소


# 성능 비교 (클래스 2개 선언)
class TestA(object):
    __slots__ = ('a',) #이제 a만 사용할 수 있음 a의 속성값만 가짐

class TestB(object):
    pass

use_slot = TestA()
no_slot = TestB()


print('EX2-1 -', use_slot)
# print('EX2-2 -', use_slot.__dict__) #set으로 바뀜
print('EX2-3 -', no_slot)
print('EX2-4 -', no_slot.__dict__)

use_slot.a = 10
# use_slot.b = 10


# 메모리 사용량 비교
import timeit

# 측정을 위한 함수 선언
def repeat_outer(obj):
    def repeat_inner():
        obj.a = 'test'
        del obj.a
    return repeat_inner


#number 수만큼 반복하는 함수
#min 써서 함수 실행에 가장 적게 걸린 수 보여줌
print('EX3-1 -', min(timeit.repeat(repeat_outer(use_slot), number=1000)))
print('EX3-2 -', min(timeit.repeat(repeat_outer(no_slot), number=1000)))

print()
print()

# 객체 슬라이싱
class ObjectS:
    def __init__(self):
        self._numbers = [n for n in range(1, 10000, 3)]
    
    def __len__(self):
        return len(self._numbers)

    def __getitem__(self, idx):
        return self._numbers[idx]

s = ObjectS()

print('EX3-1 -', s.__dict__)
print('EX3-2 -', len(s._numbers)) #len 없어도 이렇게 하면 되긴함
print('EX3-3 -', len(s)) #len메서드 구현 안햇음 오류남
##리스트의 추상 메서드를 전부 구현해두어서 리스트처럼 사용가능
print('EX3-4 -', s[1:10])
print('EX3-5 -', s[-1])
print('EX3-6 -', s[::10])

print()
print()


# 파이썬 추상클래스
# 참고 : https://docs.python.org/3/library/collections.abc.html

#자체적으로 객체 생성 불가->자바는 그럼(interface, abstract)
#상속을 통해서 자식이 구현해야함 자식이 인스턴스 생성해야함
#개발과 관련된 공통된 내용(필드, 메소드) 추출 및 통합해서 공통된 내용으로 작성하게 하는 것
#요구사항을 모두 구현해야 작동

from collections.abc import Sequence

# Sequence 상속 받지 않았지만, 자동으로 __iter__, __contains__ 기능 작동
# 객체 전체를 자동으로 조사 -> 시퀀스 프로토콜

class IterTestA():
    def __getitem__(self, idx):
        return range(1, 50, 2)[idx] # range(1, 50, 2)


i1 = IterTestA()

print('EX4-1 -', i1[4])
print('EX4-2 -', i1[4]) # [idx] 제거 후
print('EX4-3 -', 3 in i1[1:10])
# print('EX4-4 -', [i for i in i1[:]])

print()
print()


# Sequence 상속 
# 요구사항인 추상메소드 모두 구현해야 동작
# 위와 다른 점은 부모가 있다는 것 정도

#평소에는 이거 내부적으로 알아서 상속받아서 구현됨(그래서 구현안해도 에러안나는거)

from collections.abc import Sequence

class IterTestB(Sequence):
    def __getitem__(self, idx):
        return range(1, 50, 2)[idx] # range(1, 50, 2)

    def __len__(self, idx):
        return len(range(1, 50, 2)[idx])


i2 = IterTestB()

print('EX4-5 -', i2[4])
# print('EX4-6 -', len(i2[:]))
print('EX4-7 -', len(i2[1:6]))

print()
print()


# abc 활용 예제
import abc

#ABC 상속을 받아야함
class RandomMachine(abc.ABC): # metaclass=abc.ABCMeta (3.4 이하 버전)
    # __metaclass__ = abc.ABCMeta
    
    # 추상 메소드
    @abc.abstractmethod  ###흔히 말하는 강제되는 abstract 추가
    def load(self, iterobj):
        '''iterable 항목 추가'''
    

    # 추상 메소드
    @abc.abstractmethod
    def pick(self, iterobj):
        '''무작위 항목 뽑기'''
    
    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        return tuple(sorted(items))

import random

class CraneMachine(RandomMachine):
    def __init__(self, items):
        self._randomizer = random.SystemRandom() #시스템에 의한 난수 생성
        self._items = []
        self.load(items)
    
    def load(self, items):
        #부모에게 없는 구현부를 구현함
        self._items.extend(items)
        self._randomizer.shuffle(self._items)
    
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('Empty Crane Box.')
    
    def __call__(self):
        return self.pick()
    
    # 메소드 오버라이드
    # def inspect(self):
    #     print('Override Test')

# 서브 클래스 확인
# T /F로 나옴 왼쪽이 오른쪽의 자식인가?로 질문
print('EX5-1 -', issubclass(RandomMachine, CraneMachine))
print('EX5-2 -', issubclass(CraneMachine, RandomMachine))
# 상속 구조 확인
#가계도 찍는 클래스
print('EX5-3 -', CraneMachine.__mro__)

cm = CraneMachine(range(1,100)) # 추상메소드 구현 안하면 에러

#아이템 넣고
print('EX5-4 -', cm._items)
#하나 뽑고
print('EX5-5- ', cm.pick())
#그냥 불러도 알아서 call
print('EX5-6- ', cm())
#자식에서 오버라이딩 안하면 부모꺼 가져옴
#->모두 뽑아서 순서 정렬한거
print('EX5-7- ', cm.inspect())
