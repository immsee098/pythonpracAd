# Chapter05-1
# 파이썬 심화
# 객체 참조 중요한 특징들
# Python Object Referrence

print('EX1-1 -')
#그냥 dir 쓰면 여기 실행하는 실행영역 상태만 알려줌
print(dir())

# id vs __eq__ (==) 증명
x = {'name': 'kim', 'age': 33, 'city': 'Seoul'}
y = x

print('EX2-1 -', id(x), id(y)) #아이디값 동일
print('EX2-2 -', x == y)
print('EX2-3 -', x is y) #같은 객체를 보고있냐
print('EX2-4 -', x, y)

x['class'] = 10
print('EX2-5 -', x, y) #x에 넣었지만 y에도 들어가버림

print()
print()

z = {'name': 'kim', 'age': 33, 'city': 'Seoul', 'class': 10}

print('EX2-6 -', x, z)
print('EX2-7 -', x is z) #아이디값 다름
print('EX2-8 -', x is not z) 
print('EX2-9 -', x == z) # 값이 같다 값만 같음->새로 할당된거라

# 객체 생성 후 완전 불변 -> 즉, id는 객체 주소(정체성)비교, ==(__eq__) 는 값 비교
# 보통 is로 아이디값 같냐 아니냐로 비교해서 거르는 편

print()
print()

# 튜플 불변형의 비교
# 튜플은 불변이라 같은 값이라도 아이디는 항상 다른듯
tuple1 = (10, 15, [100, 1000])
tuple2 = (10, 15, [100, 1000])

print('EX3-1 -', id(tuple1), id(tuple2))
print('EX3-2 -', tuple1 is tuple2)
print('EX3-3 -', tuple1 == tuple2)
print('EX3-4 -', tuple1.__eq__(tuple2))

print()
print()

# Copy, Deepcopy(깊은 복사, 얕은 복사)

# Copy
tl1 = [10, [100, 105], (5, 10, 15)]
tl2 = tl1
tl3 = list(tl1)
## 둘 차이가 뭘까??
## tl1, tl2와 tl3는 id값이 다름. list 생성자로 만들어서
## 리스트 복사할때는 list 생성자로 때려박아야 아이디값 복사 안됨

print('EX4-1 -', tl1 == tl2)
print('EX4-2 -', tl1 is tl2)
print('EX4-3 -', tl1 == tl3)
print('EX4-4 -', tl1 is tl3)

# 증명
tl1.append(1000)
tl1[1].remove(105)

print('EX4-5 -', tl1)
print('EX4-6 -', tl2)
print('EX4-7 -', tl3)

print()

# print(id(tl1[2]))
tl1[1] += [110, 120]
tl1[2] += (110, 120)

print('EX4-8 -', tl1)
print('EX4-9 -', tl2) # 튜플 재 할당(객체 새로 생성)
##->불변이라 아이디값 새로운걸로 갈아치운거
###따라서 리스트 안에 튜플 넣는 거... 안전하지 않다... 
print('EX4-10 -', tl3)
# print(id(tl1[2]))

print()
print()


#Deep Copy

# 장바구니
class Basket:
    def __init__(self, products=None):
        if products is None:
            self._products = []
        else:
            self._products = list(products)

    def put_prod(self, prod_name):
        self._products.append(prod_name)

    def del_prod(self, prod_name):
        self._products.remove(prod_name)


import copy

basket1 = Basket(['Apple', 'Bag', 'TV', 'Snack', 'Water'])
basket2 = copy.copy(basket1)
basket3 = copy.deepcopy(basket1)
###################################
###################################
#####존나 중요한 부분@@@@@
#여기까진 각각 다른 인스턴스로 복사됨 아이디값 다 다름
print('EX5-1 -', id(basket1), id(basket2), id(basket3))

#근데 막상 프로덕트의 아이디값은 쉘로 카피 시 같아짐을 볼 수 잇음
#안에 내용물은 다 똑같이 복사됨..아이디값이
print('EX5-2 -', id(basket1._products), id(basket2._products), id(basket3._products))

print()

basket1.put_prod('Orange')
basket2.del_prod('Snack')

print('EX5-3 -', basket1._products)
print('EX5-4 -', basket2._products)
print('EX5-5 -', basket3._products)

print()
print()


# 함수 매개변수 전달 사용법

def mul(x, y):
    x += y
    return x
#기존값 보존됨
x = 10
y = 5

print('EX6-1 -', mul(x, y), x, y)
print()

a = [10, 100]
b = [5, 10]

#a 즉 원본이 변경되어버림
#가변형은 주소를 넘겨버림... 데이터가 변경되어버림
#리스트 같은 건 데이터를 복사하는 게 아닌 주소를 넘겨야 빠르기때문에 이렇게 설계됨
print('EX6-2 -', mul(a, b), a, b) # 가변형 a -> 원본 데이터 변경

c = (10, 100)
d = (5, 10)

#튜플은 불변형이라 ok
print('EX6-2 -', mul(c, d), c, d) # 불변형 c -> 원본 데이터 변경 안됨


###원본이 수정되면 안 되는 건 불변형으로, 아님 걍 가변형 ㄱ(빠름)


# 파이썬 불변형 예외
# 사본 생성을 하지 않음
# str, bytes, frozenset, Tuple : 사본 생성 X -> 참조 반환

tt1 = (1, 2, 3, 4, 5)
tt2 = tuple(tt1) #이래도 같은 곳을 바라봄
tt3 = tt1[:] #이래도!! 같은 곳 바라봄

print('EX7-1 -', tt1 is tt2, id(tt1), id(tt2))
print('EX7-2 -', tt3 is tt1, id(tt3), id(tt1))

tt4 = (10, 20, 30, 40, 50)
tt5 = (10, 20, 30, 40, 50)
ss1 = 'Apple'
ss2 = 'Apple'

#아예 똑같은 값이면 튜플의 경우 하나 참조함.. 위의 예외들 모두
print('EX7-3 -', tt4 is tt5, tt4 == tt5, id(tt4), id(tt5))
print('EX7-4 -', ss1 is ss2, ss1 == ss2, id(ss1), id(ss2))































