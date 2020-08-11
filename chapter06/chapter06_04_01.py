# Chapter06-4-1
# 파이썬 심화
# Asyncio
# 비동기 I/O Coroutine 작업
# 작업권을 넘겨서 바로 실행될 수 있게 해주는 것

# Generator -> 반복적인 객체 Return 사용
# 즉, 실행 Stop -> 다른 작업으로 위임 -> Stop 지점 부터 재실행 원리
# non-blocking 비동기 처리에 적합

# BlockIO
# 순차 실행

# 한 명 때문에 모두가 멈춰줘야하는 상황
import timeit
from urllib.request import urlopen

urls = ['http://daum.net', 'https://google.com', 'https://apple.com', 'https://tistory.com', 'https://github.com/', 'https://gmarket.co.kr/']
start = timeit.default_timer()

# 순차 실행부
for url in urls:
    print('Start', url)
    # 네트워크나 파일 쓰기 등... 이거때매 블락됨
    urlopen(url)
    print('Done', url)

# 완료시간 - 시작시간
duration = timeit.default_timer() - start

# 총 실행 시간
print('Total Time : ', duration)