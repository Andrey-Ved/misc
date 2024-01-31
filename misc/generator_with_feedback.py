#####################################################
#
#  example from the book
#  Matthew Wilkes "Advanced Python Development"
#
#####################################################

import itertools


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
