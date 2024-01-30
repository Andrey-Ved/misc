import itertools
import operator


def test1():
    c = itertools.count()
    # next() function returns next item in the iterator. By default, starts with number 0 and increments by 1.
    print(next(c))  # Output:0
    print(next(c))  # Output:1
    print(next(c))  # Output:2
    print(next(c))  # Output:3

    # Returns an infinite iterator starting with number 5 and incremented by 10.
    # The values in the iterator are accessed by next()
    c1 = itertools.count(5, 10)
    print(next(c1))  # Output:5
    print(next(c1))  # Output:10
    print(next(c1))  # Output:15

    # accessing values in the iterator using for loop.step argument can be float values also.
    c2 = itertools.count(2.5, 2.5)
    for i in c2:
        # including terminating condition, else loop will keep on going.(infinite loop)
        if i > 25:
            break
        else:
            print(i, end=" ")  # Output:2.5 5.0 7.5 10.0 12.5 15.0 17.5 20.0 22.5 25.0

    # step can be negative numbers also.negative numbers count backwards.
    c3 = itertools.count(2, -2.5)
    print(next(c3))  # Output:2
    print(next(c3))  # Output:-0.5
    print(next(c3))  # Output:-3.0


def test2():
    list_a = [1, 2020, 70]
    list_b = [2, 4, 7, 2000]
    list_c = [3, 70, 7]

    for a in list_a:
        for b in list_b:
            for c in list_c:
                if a + b + c == 2077:
                    print(a, b, c)

    from itertools import product

    list_a = [1, 2020, 70]
    list_b = [2, 4, 7, 2000]
    list_c = [3, 70, 7]

    for a, b, c in product(list_a, list_b, list_c):
        if a + b + c == 2077:
            print(a, b, c)

    leaders = ['Yang', 'Elon', 'Tim', 'Tom', 'Mark']
    selector = [1, 1, 0, 0, 0]
    print(list(itertools.compress(leaders, selector)))
    # ['Yang', 'Elon']

    from itertools import groupby

    for key, group in groupby('YAaANNGGG'):
        print(key, list(group))
    # Y ['Y']
    # A ['A']
    # a ['a']
    # A ['A']
    # N ['N', 'N']
    # G ['G', 'G', 'G']

    from itertools import groupby

    for key, group in groupby('YAaANNGGG', lambda x1: x1.upper()):
        print(key, list(group))
    # Y ['Y']
    # A ['A', 'a', 'A']
    # N ['N', 'N']
    # G ['G', 'G', 'G']

    author = ['Y', 'a', 'n', 'g']

    result = itertools.combinations(author, 2)

    for x in result:
        print(x)
    # ('Y', 'a')
    # ('Y', 'n')
    # ('Y', 'g')
    # ('a', 'n')
    # ('a', 'g')
    # ('n', 'g')

    author = ['Y', 'a', 'n', 'g']

    result = itertools.permutations(author, 2)

    for x in result:
        print(x)

    # ('Y', 'a')
    # ('Y', 'n')
    # ('Y', 'g')
    # ('a', 'Y')
    # ('a', 'n')
    # ('a', 'g')
    # ('n', 'Y')
    # ('n', 'a')
    # ('n', 'g')
    # ('g', 'Y')
    # ('g', 'a')
    # ('g', 'n')

    nums = [1, 2, 3, 4, 5]
    print(list(itertools.accumulate(nums, operator.mul)))
    # [1, 2, 6, 24, 120]

    nums = [1, 2, 3, 4, 5]
    print(list(itertools.accumulate(nums, lambda a1, b1: a1 * b1)))
    # [1, 2, 6, 24, 120]

    print(list(itertools.repeat('Yang', 3)))
    # ['Yang', 'Yang', 'Yang']

    count = 0

    for c in itertools.cycle('Yang'):
        if count >= 12:
            break
        else:
            print(c, end=',')
            count += 1

    for i in itertools.count(0, 2):
        if i == 20:
            break
        else:
            print(i, end=" ")

    letters = ['a', 'b', 'c', 'd', 'e']
    result = itertools.pairwise(letters)
    print(list(result))
    # [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e')]

    nums = [1, 61, 7, 9, 2077]
    print(list(itertools.takewhile(lambda x1: x1 < 100, nums)))
    # [1, 61, 7, 9]

    nums = [1, 61, 7, 9, 2077]
    print(list(filter(lambda x1: x1 < 10, nums)))
    # [1, 7, 9]

    nums = [1, 61, 7, 9, 2077]
    print(list(itertools.takewhile(lambda x1: x1 < 10, nums)))
    # [1]


def sum_ints(source):
    total = 0

    for num in source:
        total += num

        yield total


def get_wrap_feedback_pair(initial=None):
    shared_state = initial

    def feedback():
        while True:
            yield shared_state

    def wrap(wrapped):
        nonlocal shared_state

        for item in wrapped:
            shared_state = item

            yield item

    return feedback, wrap


def test():
    feedback, wrap = get_wrap_feedback_pair(1)
    sums = wrap(
        sum_ints(
            feedback()
        )
    )
    sums = itertools.islice(sums, 3)

    assert [a for a in sums] == [1, 2, 4]


if __name__ == '__main__':
    test()
    test1()
    test2()
