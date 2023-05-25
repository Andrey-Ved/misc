from functools import reduce
from operator import and_


def init(func):
    def wrapper(*args, **kwargs):
        g = func(*args, **kwargs)
        next(g)
        return g

    return wrapper


@init
def checking_by_step():
    stack = []
    right = ""
    check = True

    while True:
        supplement = yield check

        if supplement not in "()[]{}":
            continue

        if supplement in "([{":
            stack.append(supplement)

        else:
            if len(stack) < 1:
                check = False

            else:
                if stack[-1] == "(":
                    right = ")"
                elif stack[-1] == "[":
                    right = "]"
                elif stack[-1] == "{":
                    right = "}"
                if right != supplement:
                    check = False
                else:
                    stack.pop()


def checking_braces(s: list) -> bool:
    """
    >>> checking_braces("((13[]({})[]))")
    True
    >>> checking_braces("(5+(2*6+7)-8)+[45}*{0}")
    False
    >>> checking_braces("((}")
    False
    >>> checking_braces("([]{5*df}77)")
    True
    >>> checking_braces("9}}")
    False
    """
    checking = checking_by_step()

    return reduce(
        and_,(
            checking.send(i)
            for i in s
        )
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

    # ############# little explanation about yield ############
    #
    # @init
    # def sample(multiplier):
    #     x = 0
    #
    #     while True:
    #         x = yield x * multiplier
    #         print(f'accepted value {x}  ')
    #
    #
    # print('---------------------------')
    #
    # s = sample(multiplier=10)
    #
    # for i in range(1, 4):
    #     print(f'response to transmitted {i} - {s.send(i)}')
    #     print('---------------------------')
