# Chapter03-2
# 파이썬 심화
# 시퀀스형
# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> Key 중복 허용 X, Set -> 중복 허용 X / 중복값이 있나 검색->해시테이블로 검색
# 해시값을 이용해서 빠르게 동일한거 찾아감
# Dict 및 Set 심화
# 파이썬은 대체로 Dictonary로 구성됨(key:value)

# Dict 구조
print('EX1-1 -')
# print(__builtins__.__dict__)

print()
print()


#hash값 확인(중복 허용 여부 확인)
t1 = (10, 20, (30, 40, 50))
##리스트는 언제든 변경 가능이라 중복체크 의미가 없음(넣는대로 다 들어감)
##안에 리스트가 들어가있어서 아래 에러남(어차피 변경되니 데이터만 담으면됨)
t2 = (10, 20, [30, 40, 50])


print('EX1-2 -', hash(t1))
# print('EX1-3 -', hash(t2))

print()
print()

# 지능형 딕셔너리(Comprehending Dict)
import csv

# 외부 CSV TO List of tuple

with open('resources/test1.csv', 'r', encoding='UTF-8') as f :
    temp = csv.reader(f)
    #Header Skip
    next(temp)
    #변환
    NA_CODES = [tuple(x) for x in temp]

print('EX2-1 -',)
print(NA_CODES)

#자동으로 dictory 만들어준다
n_code1 = {country: code for country, code in NA_CODES}
n_code2 = {country.upper(): code for country, code in NA_CODES}

print()
print()

print('EX2-2 -',)
print(n_code1)


# Dict Setdefault 예제

source = (('k1', 'val1'),
            ('k1', 'val2'),
            ('k2', 'val3'),
            ('k2', 'val4'),
            ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# No use setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print('EX3-1 -', new_dict1)

#Use setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)


print('EX3-2 -', new_dict2)

print()
print()

#사용자 정의 dict 상속(UserDict 가능)

class UserDict(dict):
    def __missing__(self, key):
        print('Called : __missing__')
        if isinstance(key, str):
            raise KeyError(key)
        return self[self(key)]

    #딕셔너리를 호출하면 get메서드 호출
    def get(self, key, default=None):
        print('Called : __getitem__')
        try:
            return self[key]
        except KeyError:
            return default
    
    def __contains__(self, key):
        print('Called : __contains__')
        return key in self.keys() or str(key) in self.keys()

user_dict1 = UserDict(one=1, two=2)
user_dict2 = UserDict({'one': 1, 'two': 2})
user_dict3 = UserDict([('one',1),('two',2)])

# 출력
print('EX4-1 -', user_dict1, user_dict2, user_dict3)
print('EX4-2 -', user_dict2.get('two'))
print('EX4-3 -', 'one' in user_dict3)
# print('EX4-4 -', user_dict3['three'])
# 본래 딕셔너리라면 three에서 에러띠우지만 커스텀해서 None반환하게만든것
print('EX4-5 -', user_dict3.get('three'))
print('EX4-6 -', 'three' in user_dict3)

print()
print()


# immutable Dict

from types import MappingProxyType

d = {'key1': 'TEST1'}

d_frozen = MappingProxyType(d)

print('EX5-1 -', d, id(d))
print('EX5-2 -', d_frozen, id(d_frozen))
#아이디 값은 다르지만 키/밸류는 같아서 폴스/트루 나옴
print('EX5-3 -', d is d_frozen, d == d_frozen)

#수정 불가
# d_frozen['key1'] ='ssss'

#원본은 수정 가능
d['key2'] = 'TEST2'

print('EX5-4 -', d)

print()
print()


#Set 구조(FrozenSet)

#중복안되는 셋이지만 중복을 넣어버림
s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
s4 = set() # Not {} #공 {}은 딕셔너리로 인식
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'})

# 추가
s1.add('Melon')

# 추가 불가
# s5.add('Melon')

print('EX6-1 -', s1, type(s1))
print('EX6-2 -', s2, type(s2))
print('EX6-3 -', s3, type(s3))
print('EX6-4 -', s4, type(s4))
print('EX6-5 -', s5, type(s5))


# 선언 최적화
#set으로 명시 선언과 리스트 후 셋 선언 차이
#내부로 돌아가는 형태가 달라서 바로 셋 선언이 더 빠름{}이거
from dis import dis

print('EX6-5 -')
print(dis('{10}'))

print('EX6-6 -')
print(dis('set([10])'))

print()
print()

# 지능형 집합(Comprehending Set)
from unicodedata import name

print('EX7-1 -')

print({name(chr(i), '') for i in range(0,256)})




























