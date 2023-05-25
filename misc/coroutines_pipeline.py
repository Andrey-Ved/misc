import time


def init(func):
    def wrapper(*args, **kwargs):
        g = func(*args, **kwargs)
        next(g)
        return g

    return wrapper


def stage_start(next_coroutine):
    for i in range(10):
        data = i

        time.sleep(0.2)
        print(data, end=' - ')

        next_coroutine.send(data)

    next_coroutine.close()


@init
def stage_2(next_coroutine):
    try:
        while True:
            data = yield
            data += 20

            time.sleep(0.2)
            print(data, end=' - ')

            next_coroutine.send(data)

    except GeneratorExit:
        next_coroutine.close()


@init
def stage_3(next_coroutine):
    try:
        while True:
            data = yield
            data += 300

            time.sleep(0.2)
            print(data, end=' - ')

            next_coroutine.send(data)

    except GeneratorExit:
        next_coroutine.close()


@init
def stage_final():
    try:
        while True:
            data = yield
            data += 4000

            time.sleep(0.2)
            print(data)

    except GeneratorExit:
        print("finished")


def pipeline():
    st_final = stage_final()
    st_3 = stage_3(st_final)
    st_2 = stage_2(st_3)
    stage_start(st_2)


if __name__ == '__main__':
    pipeline()