#chapter01-2
#파이썬 심화
#객체지향 프로그래밍(oop) -> 코드 재사용, 중복 방지 등
#클래스 상세 설명
#클래스 변수, 인스턴스 변수

#클래스 재 선언
class Student():
    """
    Student Class
    Author : Yoon
    Date : 2020.07.17

    """

    #클래스 변수
    student_count = 0

    def __init__(self, name, number, grade, details, email=None):
        #아래 5개는 인스턴스 변수
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details
        self._email = email

        #클래스 고유 이름으로 클래스 변수 접근 가능
        #여기서 Student를 빼면 지역변수(def함수 내의 변수)로 인식해버림
        Student.student_count +=1

    def __str__(self):
        return 'str {}'.format(self._name)

    def __repr__(self):
        return 'repr {}'.format(self._name)

    def detail_info(self):
        print('Current Id : {}'.format(id(self)))
        print('Student Detail Info : {} {} {}'.format(self._name, self._email, self._details))

    def __del__(self):
        Student.student_count -= 1


#self 의 의미 -> self는 실제로 인스턴스화 시킴
studt1 = Student('Cho', 2, 3, {'gender': 'Male', 'score1': 65, 'score2': 44})
studt2 = Student('Chang', 4, 1, {'gender': 'Female', 'score1': 85, 'score2': 74}, 'stu2@naver.com')

print(id(studt1))
print(id(studt2))
##내용물이 같아도 공간이 다르면 아이디 값이 다르게 나옴

print(id(studt1))
print(id(studt2))

print(studt1._name == studt2._name)
print(studt1 is studt2) #아이디값 비교-> 인스턴스 값이 같나?

a='ABC'
b=a
print(a is b) #아이디값 무조건 같다고 나옴


#dir & dict 확인

#dir은 속성을 보여줌 -> str함수 등 내부적으로 구현된 것까지 보여줌
print(dir(studt1))
print(dir(studt2))

print()
print()

#dict는 속성의 값까지 보여줌
print(studt1.__dict__)
print(studt2.__dict__)

# Docstring
#주석 볼수도있음
print(Student.__doc__)
print()

#실행
studt1.detail_info()

#에러
#Student.detail_info()

print(Student.student_count)

#인스턴스화 된 변수 넣어주면 직접 접근 가능
Student.detail_info(studt1)
Student.detail_info(studt2)

#비교
print(studt1.__class__) #부모 알려줌->기존 틀을 알려줌
print(id(studt1.__class__) == id(studt2.__class__)) #원형(CLass의 아이디값이 같냐? 같다! 원형은 하나를 공유하니)


#인스턴스 변수
#직접 접근(PEP 문법적으로 권장x)

studt1._name = 'HAHAHA'
print(studt1._name) #이러면 안돼 캡슐화 해야함

print()
print()

#클래스 벼수

# 접근
print(studt1.student_count)
print(studt2.student_count)
print(Student.student_count)

print()
print()

# 공유 확인
print(Student.__dict__)
print(studt1.__dict__)


# 인스턴스 네임스페이스 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스 변수))
#그래도 없으면 에러남

del studt2
print(studt1.student_count) #2에서 찍엇는데 1에서 찍어도 그 내용이 적용되어있음


















