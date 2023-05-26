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


def threaded(foo):
    def wrap():
        loop = asyncio.get_running_loop()
        return loop.run_in_executor(None, foo)

    return wrap


def time_print(foo):
    def wrap(*args):
        start = time()
        print(f'{foo(*args)} -> {(time()-start):.3f}')

    return wrap


def async_time_print(coo):
    async def wrap(*args):
        start = time()
        print(f'{await coo(*args)} -> {(time()-start):.3f}')
        return

    return wrap


@threaded
@time_print
def blocking_io(n=6):
    with open('temp.txt', 'w') as f:
        for _ in range(10**n):
            f.writelines('*' * n + '\n')

    return 'file writen finished'


@threaded
@time_print
def other(n=4):
    for step in range(n):
        sleep(0.4)
        print(f'   work step {step}')

    return 'worker finished'


@threaded
@time_print
def cpu_bond(n=7):
    _ = sum(i*i for i in range(10**n))

    return 'cpu bond finished'


@threaded
@time_print
def load_urls(timeout=60):
    urls = URLS

    for url in urls:
        print(f'   load {url}')

        with request.urlopen(url, timeout=timeout) as conn:
            _ = conn.read

    return 'urls load finished'


@async_time_print
async def main():
    await asyncio.gather(
        blocking_io(),
        other(),
        cpu_bond(),
        load_urls()
    )

    return f'\n**********************' \
           f'\nfinish stage'


if __name__ == '__main__':
    asyncio.run(main())
