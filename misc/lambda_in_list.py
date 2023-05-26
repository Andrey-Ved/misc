
def multipliers():
    return [lambda x: i * x for i in range(3)]


def multipliers1():
    def item(i):
        return lambda x: i * x
    return [item(i) for i in range(3)]


def multipliers2():
    return [(lambda i_2: (lambda x: i_2 * x))(i) for i in range(3)]


def multipliers3():
    return [lambda x, i_2=i: i_2 * x for i in range(3)]


def multipliers4():
    return (lambda x: i * x for i in range(3))


if __name__ == '__main__':
    functions = [
        multipliers,
        multipliers1,
        multipliers2,
        multipliers3,
        multipliers4
    ]

    for foo in functions:
        print(
            [f(1) for f in foo()]
        )
