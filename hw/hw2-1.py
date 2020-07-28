#1번
with open('./resource/a.csv', 'r') as a:
    c = a.read()
    numList = list(map(int, c.split(",")))

    sum = 0
    for num in numList:
        sum += num

    print(sum)



#2
class Median:
    def __init__(self):
        self.numberList=[]
 
    def get_item(self, item):
        self.numberList.append(item)
 
    def clear(self):
        self.numberList=[]
 
    def show_result(self):

        self.numberList.sort()
       
        numLength = len(self.numberList)
        result = 0
        if numLength%2==0:
            numMid1 = self.numberList[int(numLength/2)]
            numMid2 = self.numberList[int(numLength/2 - 1)]
            result = (numMid1+numMid2)/2
        else:
            result = self.numberList[numLength//2]
        print(result)
 
median= Median()
for x in range(10):
    median.get_item(x)
median.show_result()
 
median.clear()
for x in [0.5, 6.2, -0.4, 9.6, 0.4]:
    median.get_item(x)
median.show_result()



#3
print()
class Animal:
    def __init__(self, name):
        self.name = name
 
    def speak(self):
        print(self.name + ' cannot speak.')
 
    def move(self):
        print(self.name + ' cannot move.')
 
 
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def move(self):
        print(self.name + ' movers like a jagger.')
 

class Retriever(Dog):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(self.name + ' is smart enough to speak.')
 
 
dog = Dog('Nancy')
dog.speak()
dog.move()
 
super_dog = Retriever('Michael')
super_dog.speak()
super_dog.move()


#4
print()
class Foo:
    def __init__(self):
        super().__init__()

    def bar():
        print("A")

    def func(self):
        print("B")
    
    def __str__(self):
        return "D"


    class Bar():
        def __init__(self):
                super().__init__()

        def func():
            print("C")


Foo.bar()
Foo().func()
Foo.Bar.func()
print(Foo())