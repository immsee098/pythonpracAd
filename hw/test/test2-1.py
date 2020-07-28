#1) c

class Foo:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('I am '+ self.name)

class Bar(Foo):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('Yo are '+ self.name)

bar = Bar('John')
bar.speak()

#2) c
#3) d
#4)
#5) a

#6)a
def int_sum(*args):
    sum='aa' #0
    try:
        for n in args:
            sum += n

    except:
        print("error")

    return sum

print(int_sum('r'))

#7) from pkg.foo import Foo
#8) datetime.datetime.now()
import datetime
now = datetime.datetime.now()
print(now)

#9) 생성자
#10) 중첩 함수