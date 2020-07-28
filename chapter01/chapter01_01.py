#chapter01-1
#파이썬 심화
#객체지향 프로그래밍(oop) -> 코드 재사용, 중복 방지 등
#클래스 상세 설명
#클래스 변수, 인스턴스 변수

#절차지향 : 위->아래 (실행속도 빠름)

#일반적인 코딩

#학생1
student_name_1 = 'KIM'
student_number_1 = 1
student_grade_1 = 1
student_detail_1 = [
    {'gender':'Male'},
    {'score1': 95},
    {'score2': 88}
]

#학생2
student_name_2 = 'Lee'
student_number_2 = 2
student_grade_2 = 2
student_detail_2 = [
    {'gender':'Male'},
    {'score1': 77},
    {'score2': 92}
]

#학생3
student_name_3 = 'Park'
student_number_3 = 3
student_grade_3 = 4
student_detail_3 = [
    {'gender':'Female'},
    {'score1': 99},
    {'score2': 100}
]


#리스트 구조
#불편함
student_names_list = ['Kim', 'Lee', 'Park']
student_numbers_list = [1,2,3]
student_grades_list = [1,2,4]
student_details_list = [
    {'gender' : 'Male', 'score1': 95, 'score2': 88},
    {'gender' : 'Female', 'score1': 77, 'score2': 92},
    {'gender' : 'Male', 'score1': 99, 'score2': 100}
]

#학생 삭제
del student_names_list[1]
del student_numbers_list[1]
del student_grades_list[1]
del student_details_list[1]

print(student_names_list)

print()

#딕셔너리
#중첩 문제
students_dicts = [
    {'student_name': 'Kim', 'student_number': 1, 'student_grade': 1, 'student_detail': {'gender': 'Male', 'score1': 95, 'score2': 88}},
    {'student_name': 'Lee', 'student_number': 2, 'student_grade': 2, 'student_detail': {'gender': 'Female', 'score1': 77, 'score2': 92}},
    {'student_name': 'Park', 'student_number': 3, 'student_grade': 4, 'student_detail': {'gender': 'Male', 'score1': 99, 'score2': 100}}
]

del students_dicts[1]
print(students_dicts)
print()


#클래스 구조
#구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용

class Student(object):
    def __init__(self, name, number, grade, details):
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details

    def __str__(self):
        return 'str: {}'.format(self._name)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._name, self._number)
    
    
student1 = Student('Kim', 1, 1, {'gender': 'Male', 'score1': 95, 'score2': 88})
student2 = Student('Lee', 2, 2, {'gender': 'Female', 'score1': 77, 'score2': 92})
student3 = Student('Park', 3, 4, {'gender': 'Male', 'score1': 99, 'score2': 100})

print(student1.__dir__())
print(student1.__str__())


#리스트
students_list = []
students_list.append(student1)
students_list.append(student2)
students_list.append(student3)
print()
print(students_list)

for x in students_list:
    print(x)  #알아서 str str 오버라이드해서 출력해줌
















