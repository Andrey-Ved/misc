from multiprocessing import Process, Value


def increment_value(shared_int):
    shared_int.value = shared_int.value + 1


def increment_value_with_lock(shared_int):
    with shared_int.get_lock():
        shared_int.value = shared_int.value + 1


def main(
        iterations_number,
        process_number,
        with_lock=False
):

    for _ in range(iterations_number):
        shared_int = Value('i', 0)

        process = []

        [process.append(
            Process(
                target=increment_value_with_lock if with_lock
                else increment_value,
                args=(shared_int, )
            )
        ) for _ in range(process_number)]

        [p.start() for p in process]
        [p.join() for p in process]

        print(shared_int.value)
        assert shared_int.value == process_number, 'race condition'


if __name__ == '__main__':
    print(' ******** now with lock ****** ')
    main(
        iterations_number=30,
        process_number=3,
        with_lock=True
    )

    print(' ******** now without lock ****** ')
    main(
        iterations_number=30,
        process_number=3,
        with_lock=False
    )
