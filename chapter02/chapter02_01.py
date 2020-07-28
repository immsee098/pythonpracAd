#chapter02-01
#파이썬 심화
#데이터 모델

#Namedtupple 실습
#파이썬의 중요한 프레임워크->시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)

#시퀀스 ex 리스트(인덱스 있음)
#시퀀스에 따라오는 것-> 이터레이터

#객체 -> 파이썬의 데이터를 추상화
#모든 객체 -> id, type -> value

#dir 자체도 이터레이터 가능하다(객체(리스트)기때매)

#일반적인 튜플 사용
pt1 =(1.0, 5.0)
pt2 =(2.5, 1.5)

from math import sqrt

line_leng1 = sqrt((pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[1]) ** 2)
print('EX1-1 -', line_leng1)

#네임드 튜플 사용
#불변객체/클래스보다 적은 메모리/다양한 접근법/딕셔너리 키처럼 사용가능
from collections import namedtuple

#네임드 튜플 선언
Point = namedtuple('Point', 'x y')

# 두 점 선언
pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)

# 계산
line_leng2 = sqrt((pt2.x - pt1.x) ** 2 + (pt2.y - pt1.y) ** 2)

# 출력
print('EX1-2 -', line_leng2)
print('EX1-3 -', line_leng1 == line_leng2)



# 네임드 튜플 선언 방법
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
##레이블 두개와 예약어를 넣을 수 있을까?
##리네임 옵션 쓰면 예약어나 중복어는 알아서 _넣어서 이름 바꿔버림
Point4 = namedtuple('Point', 'x y x class', rename=True) # Default=False


# 출력
print('EX2-1 -', Point1, Point2, Point3, Point4)

print()
print()

# Dict to Unpacking
temp_dict = {'x': 75, 'y': 55}

# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)

##########중요!!!!!!!!!!!!!!!!!!!!!!!!!!##########
#딕셔너리 형태를 x y로 할당할 수 있다. 
#그러나 그냥 넣으면 unpacked가 되어서 x에 딕셔너리가 통으로 들어간다
#**을 붙이면 내용물이 풀리면서 알아서 할당된다
p5 = Point3(**temp_dict)

# 출력
print('EX2-2 -', p1, p2, p3, p4, p5)


# 사용
#튜플과 똑디로 사용 가능
print('EX3-1 -', p1[0] + p2[1]) # Index Error 주의
print('EX3-2 -', p1.x + p2.y) # 클래스 변수 접근 방식

# Unpacking
#x와 y에 p3의 x y 값이 자동 할당됨
x, y = p3

print('EX3-3 -', x+y)

# Rename 테스트
print('EX3-4 -', p4)


#리스트는 이터레이터 시퀀스 다 가지고 있는 데이터 담는 그릇

# 네임드 튜플 메소드
#리스트를 네임드튜플로 넣어보자
temp = [52, 38] 

# _make() : 새로운 객체 생성
p4 = Point1._make(temp)

print('EX4-1 -', p4)

# _fields : 필드 네임 확인

print('EX4-2 -', p1._fields, p2._fields, p3._fields) # x y 확인


#_asdict(): 딕셔너리로 반환
# _asdict() : OrderedDict 반환

print('EX4-3 -', p1._asdict(), p4._asdict())
print(dict(p1._asdict()))  #일단 딕셔너리로도 바꿔짐

# _replace() : 수정된 '새로운' 객체 반환
#사실 튜플은 불변인데 리플레이스 쓰면 새로운 객체 반환됨

print('EX4-4 -', p2._replace(y=100))

print()
print()

# 실 사용 실습
# 학생 전체 그룹 생성
# 반20명 , 4개의 반-> (A,B,C,D) 번호

#네임드 튜플 선언
Classes = namedtuple('Classes', ['rank', 'number'])

#그룹 리스트 선언
numbers = [str(n) for n in range(1,21)]
ranks = 'A B C D'.split()

#List Comphrension

#for 써서 내부에서 반복
students = [Classes(rank, number) for rank in ranks for number in numbers]


print('EX5-1 -', len(students))
print('EX5-2 -', students)


# 가독성 X

students2 = [Classes(rank, number) 
                    for rank in 'A B C D'.split() 
                        for number in [str(n) 
                            for n in range(1,21)]]


print()
print()

print('EX6-1 -', len(students2))
print('EX6-2 -', students2)


#출력 
for s in students:
    print('Ex7-1 - ', s)
