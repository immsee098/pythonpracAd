# Chapter03-1
# 파이썬 심화
# 시퀀스형 
# 컨테이너(Container : 서로다른 자료형[list, tuple, collections.deque], 
# Flat : 한 개의 자료형[str,bytes,bytearray,array.array, memoryview])
# Flat이 더 빠름... 어레이가 당연히 더 빠름
# 가변(list, bytearray, array.array, memoryview, deque) vs 불변(tuple, str, bytes)
# 리스트 및 튜플 심화

# 지능형 리스트(Comprehending Lists)

# Non Comprehending Lists
chars = '!@#$%^&*()_+'

##유니코드로 바꾸는 코드 만들기
codes1 = []

for s in chars:
    #아스키 코드값 출력 함수
    codes1.append(ord(s))

# Comprehending Lists->쬠 더 빠름
codes2 = [ord(s) for s in chars]

# Comprehending Lists + Map, Filter
# 속도 약간 우세
codes3 = [ord(s) for s in chars if ord(s) > 40]
#map은 변환해서 리스트로 넣어줌/filter는 걸러줌
codes4 = list(filter(lambda x : x > 40, map(ord, chars)))

# 전체 출력
print('EX1-1 -', codes1)
print('EX1-2 -', codes2)
print('EX1-3 -', codes3)
print('EX1-4 -', codes4)
print('EX1-5 -', [chr(s) for s in codes1])
print('EX1-6 -', [chr(s) for s in codes2])

print()
print()

# Generator 생성 방법
# 반복을 하나씩 해서 값을 생성해냄
# 값을 발생시키는 구조만 물고 대기탐

import array

# Generator : 한 번에 한 개의 항목을 생성(메모리 유지x)
tuple_g = (ord(s) for s in chars)
#Array
array_g = array.array('I',  (ord(s) for s in chars)) #"I"는 인트형이라는 뜻 첫 값은 자료형

#이거 찍어보면 제너레이터 나옴->줄만 세워두고 아직 값을 안찍어둠
#튜플은 메모리에 안 올려두고 대기탐/리스트는 메모리에 올리고 전부 사용
#그때그때 하나씩 꺼내서만 사용해도 되는건 이게 성능상 굿
print('EX2-1 -', type(tuple_g))

print('EX2-2 -', next(tuple_g))
print('EX2-3 -', type(array_g))
print('EX2-3 -', array_g.tolist())

print()
print()


# 제네레이터 예제
print('EX3-1 -', ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,11)))

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,11)):
    print('EX3-2', s)


print()
print()

# 리스트 주의 할 점
marks1 = [['~'] * 3 for n in range(3)]
marks2 = [['~'] * 3] * 3

#두개 자체는 똑같이 생김
print('EX4-1 -', marks1)
print('EX4-2 -', marks2)

print()

# 수정
marks1[0][1] = 'X'
marks2[0][1] = 'X'

print('EX4-3 -', marks1) #첫 번째 리스트의 두 번째만 바꿔줌
print('EX4-4 -', marks2) #모든 것의 두번째 다 바꿔줌

# 증명
print('EX4-5 -', [id(i) for i in marks1])
print('EX4-6 -', [id(i) for i in marks2]) #같은 아이디 세 개 들어가잇음->세개 그대로 복사해서 붙인거라
#세 개가 똑같은 걸 보고 있다. 그래서 하나만 바꿔도 같이 바뀜. 특정 주소값 하나 값을 바꿨지만 바라보는 곳이 같아서


# Tuple Advanced

# Unpacking
#짐을 풀어서 알아서 딱딱 삽입해주는거->몫 나머지 등
print('EX5-1 -', divmod(100, 9))
#앞에 *붙으면 알아서 풀어쓰라는말
print('EX5-2 -', divmod(*(100, 9)))
#아예 이건 결과 튜플 자체도 풀려버림
print('EX5-3 -', *(divmod(100, 9)))

print()

x, y, *rest = range(10)
print('EX5-4 -', x, y, rest)

#1, 2가 x y에 다 할당되어서 rest는 빈 리스트로 나옴
x, y, *rest = range(2)
print('EX5-5 -', x, y, rest)

x, y, *rest = 1, 2, 3, 4, 5
print('EX5-6 -', x, y, rest)


#unpacking
#함수로 인자 넘길때 풀어서 넘겨주는 것


print()
print()

# Mutable(가변) vs Immutable(불변)

l = (10, 15, 20)
m = [10, 15, 20]

print('EX6-1 -', l, id(l))
print('EX6-2 -', m, id(m))


l = l * 2
m = m * 2

print('EX6-3 -', l, id(l))
print('EX6-4 -', m, id(m))

#튜플은 자체 연산자 사용해도 값 바뀜
#그치만 리스트는? 내부에 재할당함
#리스트도 그치만 아래처럼 자산에게 재할당하는 형식이 더 나음
l *= 2
m *= 2

print('EX6-5 -', l, id(l))
print('EX6-6 -', m, id(m))

print()


# sort vs sorted 
# reverse, key=len, key=str.lower, key=func

# sorted : 정렬 후 새로운 객체 반환
#원본이 변경안됨
f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']

print('EX7-1 -', sorted(f_list))
print('EX7-2 -', sorted(f_list, reverse=True))
#글자의 길이순대로 정렬
print('EX7-3 -', sorted(f_list, key=len))
#끝 글자를 기준으로 정렬
print('EX7-4 -', sorted(f_list, key=lambda x: x[-1]))
print('EX7-5 -', sorted(f_list, key=lambda x: x[-1], reverse=True))
print()


# sort : 정렬 후 객체 직접 변경
# 심지어 반환조차 none으로 한다->즉??반환값 없음. sort하고 대입해도 반환값 안나와서 none뜸

# 반환 값 확인(None)
print('EX7-7 -', f_list.sort(), f_list)
print('EX7-8 -', f_list.sort(reverse=True), f_list)
print('EX7-9 -', f_list.sort(key=len), f_list)
print('EX7-10 -', f_list.sort(key=lambda x: x[-1]), f_list)
print('EX7-11 -', f_list.sort(key=lambda x: x[-1], reverse=True), f_list)
