import time


def init(func):
    def wrapper(*args, **kwargs):
        g = func(*args, **kwargs)
        next(g)
        return g

    return wrapper


def stage_start(next_coroutine, number):
    for i in range(10):
        data = i + number

        time.sleep(0.2)
        print(data, end=' - ')

        next_coroutine.send(data)

    next_coroutine.close()


@init
def stage_work(next_coroutine, number):
    try:
        while True:
            data = yield
            data += number

            time.sleep(0.2)
            print(data, end=' - ')

            next_coroutine.send(data)

    except GeneratorExit:
        next_coroutine.close()


@init
def stage_final(number):
    try:
        while True:
            data = yield
            data += number

            time.sleep(0.2)
            print(data)

    except GeneratorExit:
        print("finished")


def pipeline():
    st_final = stage_final(4000)
    st_3 = stage_work(st_final, 300)
    st_2 = stage_work(st_3, 20)
    stage_start(st_2, 0)


if __name__ == '__main__':
    pipeline()
