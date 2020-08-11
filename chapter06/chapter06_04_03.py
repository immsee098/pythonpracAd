# Chapter06-4-3
# 파이썬 심화
# Asyncio
# 비동기 I/O Coroutine 작업
# Generator -> 반복적인 객체 Return 사용
# 즉, 실행 Stop -> 다른 작업으로 위임 -> Stop 지점 부터 재실행 원리
# non-blocking 비동기 처리에 적합

# Asyncio 변환 작업
# await 뒤에는 항상 async가 붙어야함(두 개는 같이 다님)

# 단일 스레드에서 서로 순서를 양보하는 기법(멀티 아님)

# aiohttp 사용 가능(Asyncio 지원)
import asyncio
import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading

# 시작 시간
start = timeit.default_timer()
urls = ['http://daum.net', 'https://google.com', 'https://apple.com', 'https://tistory.com', 'https://github.com/', 'https://gmarket.co.kr/']


async def fetch(url, executor):
    # 쓰레드 이름 주목!
    print('Thread Name :', threading.current_thread().getName(), 'Start', url)
    # 실행
    # 이것도 urlopen(url)에서 아래로 바꿈.. yielfd from\
    # await urlopen은 불가능(어차피 블락이라) 따라서 아래를씀
    # 이 부분만 스레딩으로 바꾸는 기법
    res = await loop.run_in_executor(executor, urlopen, url)#일꾼 한명/일꾼이 처리할 함수/url
    print('Thread Name :', threading.current_thread().getName(), 'Done', url)
    # 반환
    return res.read()[0:5]

async def main():
    # 쓰레드 풀 생성
    executor = ThreadPoolExecutor(max_workers=10)

    # yield from(await)
    # asyncio.ensure_future :
    futures = [
        asyncio.ensure_future(fetch(url, executor)) for url in urls
    ]
    
    # 결과 취합->일이 다 끝난 후
    # futures를 언패킹 해서 쓰라함
    rst = await asyncio.gather(*futures)

    print()
    print('Result : ', rst)

if __name__ == '__main__':
    # 루프 생성
    # 얘가 전체 함수에서 루프 돌면서 코루틴 관리해주는 것
    loop = asyncio.get_event_loop()
    # 루프 대기
    loop.run_until_complete(main())
    # 완료시간 - 시작시간
    duration = timeit.default_timer() - start
    # 총 실행 시간
    print('Total Time : ', duration)