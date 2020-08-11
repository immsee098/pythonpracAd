# Chapter06-1
# 파이썬 심화
# 흐름제어, 병행처리(Concurrency)
# 제네레이터, 반복형
# Generator

# 파이썬 반복형 종류
# for, collections, text file, List, Dict, Set, Tuple, unpacking, *args
# 공부할 것 : 반복형 객체 내부적으로 iter 함수 내용, 제네레이터 동작 원리, yield from

# 반복 가능한 이유? -> iter(x) 함수 호출

t = 'ABCDEF'

# for 사용
for c in t:
    print('EX1-1 -', c)

print()

# while 사용

w = iter(t)

while True:
    try:
        print('EX1-2 -', next(w))
    except StopIteration:
        break  #반복 불가능하면 에러내는대신 break함

print()

from collections import abc  #추상클래스인데 반복 가능하게해줌

# 반복형 확인
print('EX1-3 -', hasattr(t, '__iter__'))
print('EX1-4 -', isinstance(t, abc.Iterable))

##__dir__로 찍어봤을때 __iter__있음 반복형임

print()

# next 사용

class WordSplitIter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')
    
    #iterable record라는 것을 알려주는 부분
    def __next__(self):
        # print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stop! Stop!')
        self._idx += 1
        return word
    
    def __iter__(self):
        print('Called __iter__')
        return self
    
    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)


wi = WordSplitIter('Who says the nights are for sleeping')

print('EX2-1 -', wi)
print('EX2-2 -', next(wi))
print('EX2-3 -', next(wi))
print('EX2-4 -', next(wi))
print('EX2-5 -', next(wi))
print('EX2-6 -', next(wi))
print('EX2-7 -', next(wi))
print('EX2-8 -', next(wi))
# print('EX2-9 -', next(wi))

print()
print()



print()
print()

# Generator 패턴
# 1.지능형 리스트, 딕셔너리, 집합 -> 데이터 셋이 증가 될 경우 메모리 사용량 증가 -> 제네레이터 완화
# 2.단위 실행 가능한 코루틴(Coroutine) 구현에 아주 중요
# 3.딕셔너리, 리스트 한 번 호출 할 때 마다 하나의 값만 리턴 
# #-> 아주 작은 메모리 양을 필요로 함

class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')
    
    def __iter__(self):
        for word in self._text:

            ##yield 자체가 제너레이터다!!!
            ##next에서 구현한 걸 다 알아서 해줌
           yield word # 제네레이터
        return
    
    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)


wg = WordSplitGenerator('Who says the nights are for sleeping')

wt = iter(wg)

print('EX3-1 -', wt)
print('EX3-2 -', next(wt))
print('EX3-3 -', next(wt))
print('EX3-4 -', next(wt))
print('EX3-5 -', next(wt))
print('EX3-6 -', next(wt))
print('EX3-7 -', next(wt))
print('EX3-8 -', next(wt))
# print('EX3-9 -', next(wt))

print()
print()


# Generator 예제1

def generator_ex1():
    print('start')
    yield 'AAA'
    print('continue')
    yield 'BBB'
    print('end')

temp = iter(generator_ex1())

#제너레이터 때매 하나씩만 출력됨
#yield를 만나면 next를 만날 때까지 멈춰버림

# print('EX4-1 -', next(temp))
# print('EX4-2 -', next(temp))
# print('EX4-1 -', next(temp))

for v in generator_ex1():
    pass
    # print('EX4-3 -', v)

print()

# Generator 예제2

temp2 = [x * 3 for x in generator_ex1()]
temp3 = (x * 3 for x in generator_ex1())
#리스트라 이미 메모리에 만들어서 올려둠
print('EX5-1 -',temp2)
#아직 메모리로 만들어서 올리지 않앗음
print('EX5-2 -',temp3)

for i in temp2:
    print('EX5-3 -', i)

print()
print()

for i in temp3:
    print('EX5-4 -', i)

print()
print()


# Generator 예제3(자주 사용하는 함수)

import itertools

gen1 = itertools.count(1, 2.5)

#next가 호출되기 전에는 연산식만 저장하고 있음
print('EX6-1 -', next(gen1))
print('EX6-2 -', next(gen1))
print('EX6-3 -', next(gen1))
print('EX6-4 -', next(gen1))
# ... 무한

print()


# 조건
gen2 = itertools.takewhile(lambda n : n < 1000, itertools.count(1, 2.5))

for v in gen2:
    print('ex6-5 -', v)


print()

# 필터 반대
# 조건 반대만 출력
gen3 = itertools.filterfalse(lambda n : n < 3, [1,2,3,4,5])

for v in gen3:
    print('EX6-6 -', v)


print()


# 누적 합계
gen4 = itertools.accumulate([x for x in range(1, 101)])

for v in gen4:
    print('EX6-7 -', v)

print()

# 연결1
gen5 = itertools.chain('ABCDE', range(1,11,2))

print('EX6-8 -', list(gen5))

# 연결2
# 튜플 형식으로 반환(0, 'A') 등..
# 인덱스 지정해주는 것이라 생각하면될듯
gen6 = itertools.chain(enumerate('ABCDE'))

print('EX6-9 -', list(gen6))

# 개별
# 튜플 형태로 개별 찢어줌 ('A'), ('B'),,,
gen7 = itertools.product('ABCDE')

print('EX6-10 -', list(gen7))

# 연산(경우의 수)->경우의수 곱연산
gen8 = itertools.product('ABCDE', repeat=2)

print('EX6-11 -', list(gen8))

# 그룹화
# 반복된 걸 리스트로 만들어서 가지고잇음
gen9 = itertools.groupby('AAABBCCCCDDEEE')

# print('EX6-12 -', list(gen9))

for chr, group in gen9:
    print('EX6-12 -', chr, ' : ', list(group))

print()
