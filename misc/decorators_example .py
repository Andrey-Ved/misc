
class Tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args):
        self.calls += 1
        print(f'call {self.calls} to {self.func.__name__}')
        self.func(*args)


def prn(func):
    print("start")
    return func


def adder(func):
    def wrapped(*args):
        args = [2 * i for i in args]
        return func(*args)

    return wrapped


@prn
@Tracer
@adder
def spam(a, b, c):
    print(a + b + c)


if __name__ == '__main__':
    for _ in range(3):
        spam(1, 1, 1)
