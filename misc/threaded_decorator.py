import asyncio
from time import time, sleep
from urllib import request


URLS = ['https://vk.com',
        'https://russian.rt.com/',
        'https://www.youtube.com/',
        'https://mail.ru/',
        'https://www.google.ru/',
        'https://timeweb.com/ru/',
        'https://yandex.ru/']


def threaded(func):
    def wrap():
        loop = asyncio.get_running_loop()
        return loop.run_in_executor(None, func)

    return wrap


@threaded
def blocking_io(n=6):
    start = time()

    with open('temp.txt', 'w') as f:
        for _ in range(10**n):
            f.writelines('*' * n + '\n')

    print('file writen finished ->', time()-start)
    return True


@threaded
def other(n=4):
    start = time()

    for step in range(n):
        sleep(0.4)
        print(f'work step {step}')

    print('worker finished ->', time() - start)
    return True


@threaded
def cpu_bond(n=7):
    start = time()

    bonds = sum(i*i for i in range(10**n))

    print('cpu bond finished ->', time()-start)
    return bonds


@threaded
def load_urls(timeout=60):
    urls = URLS
    start = time()

    for url in urls:
        print(f'load {url}')

        with request.urlopen(url, timeout=timeout) as conn:
            _ = conn.read

    print('urls load finished ->', time() - start)
    return True


async def main():
    start = time()

    await asyncio.gather(
        blocking_io(),
        other(),
        cpu_bond(),
        load_urls()
    )

    print('\n**********************\n')
    print('finish stage ->', time() - start)


if __name__ == '__main__':
    asyncio.run(main())
