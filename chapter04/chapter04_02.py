# Chapter04-2
# 파이썬 심화
# 일급 함수(일급 객체)
# Decorator & Closure

# 파이썬 변수 범위(global)

# 예제1
def func_v1(a):
    print(a)
    print(b)

# 예외
# func_v1(5)

# 예제2
##전역으로 b 넣어버려서 지역에서 끌어다씀
b = 10

def func_v2(a):
    print(a)
    print(b)

func_v2(5)


# 예제3
# 예제2
b = 10

def func_v3(a):
    # global b
    print(a)
    print(b)
    b = 20

##이거 절대 오류난다
#why? local 변수 b는 실행 전 할당됨 값은? 위에서부터 내려오면서 읽음
#지역 안에 b가 있다는 사실만 체크하고 전역의 b는 무시하는데 막상 실행해보니
#지역의 b는 호출 후에야 값이 넣어지는 상황 발생
# func_v3(5)

##함수 실행 흐름 볼 수 있는 모듈
from dis import dis

print('EX1-1 -')
print(dis(func_v3))

print()
print()


# Closure(클로저)
# 반환되는 내부 함수에 대해 선언된 연결을(정보) 가지고 참조하는 방식
# 반환 당시 함수의 유효범위를 벗어난 변수 또는 메소드에 직접 접근 가능

a = 10

print('EX2-1 -', a + 10)
print('EX2-2 -', a + 100)


# 결과를 누적 할 수 없을까?
print('EX2-3 -', sum(range(1,51)))
print('EX2-3 -', sum(range(51,101)))

print()
print()


# 클래스 이용
class Averager():
    def __init__(self):
        self._series = []

    def __call__(self, v):
        self._series.append(v)
        print('class >>> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)


# 인스턴스 생성

avg_cls = Averager()

# 누적 확인
print('EX3-1 -', avg_cls(15))
print('EX3-2 -', avg_cls(35))
print('EX3-3 -', avg_cls(40))

print()
print()


# 클로저(Closure) 사용
#전역 변수 사용 감소
#디자인 패턴 적용
#은닉화 가능

def closure_avg1():
    # Free variable -> 자유 변수 영역
    series = [] #여기가 유효범위 넘어선 영역임
    # 클로저 영역
    def averager(v):
        series.append(v) #유효범위 넘어선 시리즈 끌고오기
        print('def >>> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)
    
    #내부 함수를 리턴해줘야함(함수 자체를 리턴함)
    return averager

avg_closure1 = closure_avg1()

#일급 객체기때메 자유 변수 영역 내용물을 물고 다니면서 사용 가능하단것
print('EX4-1 -', avg_closure1(15))
print('EX4-2 -', avg_closure1(35))
print('EX4-3 -', avg_closure1(40))

print()
print()

#but 메모리 영역의 자원을 잡아먹을수있음.
#외부함수의 객체를 계속 지니고 있어야 하기 때문

# function inspection

print('EX5-1 -', dir(avg_closure1))
print()
#co__붙은 것들 중 co_freevars 영역이 있음
#이거 찍어서 출력하면 자유변수영역임
print('EX5-2 -', dir(avg_closure1.__code__))
print()
#튜플 형식으로 물고있음
print('EX5-3 -', avg_closure1.__code__.co_freevars)
print()
#클로저 내부에도 함수랑 똑같이 내부가 구성되어있음
print('EX5-4 -', dir(avg_closure1.__closure__[0]))
print()
#이것도 함수처럼 매직 메소드 정의되어있음
print('EX5-4 -', avg_closure1.__closure__[0].cell_contents)
#함수에-함수에-함수 느낌 

print()
print()


# 잘못된 클로저 사용 예

def closure_avg2():
    # Free variable
    cnt = 0
    total = 0
    # 클로저 영역
    def averager(v):
        # series = [] # Check
        cnt += 1 # cnt = cnt + 1
        total += v
        return total / cnt
    
    return averager

avg_closure2 = closure_avg2()
# print('EX5-1 -', avg_closure2(15)) # 예외
# 내부 함수의 cnt, total은 외부의 cnt, total과 별개이다
# 따라서 내부cnt가 무언가 값을 할당받기 전 + 연산을 해서 에러가나는것


# Nonlocal 사용 -> Free variable 변환
def closure_avg3():
    # Free variable
    cnt = 0
    total = 0
    # 클로저 영역
    def averager(v):
        nonlocal cnt, total
        cnt += 1
        total += v
        return total / cnt
    
    return averager

avg_closure3 = closure_avg3()

print('EX6-1 -', avg_closure3(15))
print('EX6-2 -', avg_closure3(35))
print('EX6-3 -', avg_closure3(40))

print()
print()


# 데코레이터 실습
# 외부에서 내부로 스냅샷 하는 개념이 동일

# 1. 중복 제거, 코드 간결
# 2. 클로저보다 문법 간결
# 3. 조합해서 사용 용이

# 단점
# 1. 디버깅 어려움
# 2. 에러의 모호함
# 3. 에러 발생지점 추적 어려움

import time

# 함수 퍼포먼스 체크
import time

def perf_clock(func):
        #여기서 args는 데코레이터 붙은 함수의 param값들이 들어옴
    def perf_clocked(*args):
        # 시작 시간 
        st = time.perf_counter() 
        result = func(*args)
        # 종료 시간
        et = time.perf_counter() - st 
        # 함수명
        name = func.__name__
        # 매개변수 
        arg_str = ', '.join(repr(arg) for arg in args)
        # 출력
        print('[%0.5fs] %s(%s) -> %r' % (et, name, arg_str, result)) 
        return result 
        #스냅샷이되
    return perf_clocked

@perf_clock
def time_func(seconds):
    time.sleep(seconds)

@perf_clock
def sum_func(*numbers):
    return sum(numbers)

@perf_clock
def fact_func(n):
    return 1 if n < 2 else n * fact_func(n-1)



# 데코레이터 미사용

# 일단 사용할 펑션을 하나씩 넣어줘야함
# 데코레이터에 넣으면 함수도 실행되고 데코레이터도 실행됨
non_deco1 = perf_clock(time_func)
non_deco2 = perf_clock(sum_func)
non_deco3 = perf_clock(fact_func)

#이거 하면 func가 뜨는데 내부에서 자유변수로 함수를 유지하고 있다는뜻
print('EX7-1 -', non_deco1, non_deco1.__code__.co_freevars)
print('EX7-2 -', non_deco2, non_deco2.__code__.co_freevars)
print('EX7-3 -', non_deco3, non_deco3.__code__.co_freevars)

print('*' * 40, 'Called Non Deco -> time_func')
print('EX7-4 -')
non_deco1(0.5)
print('*' * 40, 'Called Non Deco -> sum_func')
print('EX7-5 -')
non_deco2(10, 15, 25, 30, 35)
print('*' * 40, 'Called Non Deco -> fact_func')
print('EX7-6 -')
non_deco3(10)

print()
print()


# 데코레이터 사용
# @functools.lru_cache() -> 추가 학습 권장
# 자기 원래 함수 실행하듯 하면 되는 것
print('*' * 40, 'Called Deco -> time_func')
print('EX8-1 -')
time_func(0.5)
print('*' * 40, 'Called Deco -> sum_func')
print('EX8-2 -')
sum_func(10, 15, 25, 30, 35)
print('*' * 40, 'Called Deco -> fact_func')
print('EX8-3 -')
fact_func(10)




















































