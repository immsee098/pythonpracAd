#1 b
a = [[1]*10]*10
sum=0
print(a)
for i in range(10):
    del a[i][0]
    print("aa", a)
    for elem in a[i]:
        sum = sum+ elem
print(sum)
#2 b
#3 a, b, c
#4 d
#5 d
#6 a
#7 d
#8 추상 클래스
#9 제너레이터
#10 비동기