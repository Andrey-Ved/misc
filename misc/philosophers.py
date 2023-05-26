"""
Dining philosophers problem
https://en.wikipedia.org/wiki/Dining_philosophers_problem
"""

from threading import Event, local, Lock, Thread, current_thread
from contextlib import contextmanager
from time import sleep, time
from queue import Queue


STICKS_NUMBER = 5
CYCLES_NUMBER = 10
PAUSE = 0.1

_cycle_completed = Event()
_local = local()


def printer(print_queue, period_is_over):
    while True:
        message = print_queue.get()
        print(message)

        if period_is_over.is_set():
            break


@contextmanager
def acquire(*locks):
    locks = sorted(locks, key=lambda x: id(x))

    acquired = getattr(_local, 'acquired', [])

    if acquired and max(id(lock) for lock in acquired) >= id(locks[0]):
        raise RuntimeError('Lock Order Violation')

    acquired.extend(locks)
    _local.acquired = acquired

    try:
        for lock in locks:
            lock.acquire()
        yield

    finally:
        for lock in reversed(locks):
            lock.release()

        del acquired[-len(locks):]


def philosopher(
        left,
        right,
        print_queue,
        cycles_number=CYCLES_NUMBER,
        pause=PAUSE
):
    for i in range(cycles_number):
        with acquire(left, right):
            snack_time = time()

            sleep(pause)
            hunger_duration = time() - snack_time

            if hunger_duration > pause * 2:
                raise RuntimeError(
                    f'{current_thread()} - death from starvation'
                )

            print_queue.put(
                f'{current_thread()}, eating, '
                f'was hungry for {hunger_duration:.3f} sec'
            )


def main(sticks_number=STICKS_NUMBER):
    chopsticks = [
        Lock()
        for _ in range(sticks_number)
    ]

    print_queue = Queue()

    printer_thread = Thread(
        target=printer,
        args=(print_queue, _cycle_completed)
    )

    printer_thread.start()

    threads = [
        Thread(
            target=philosopher,
            args=(
                chopsticks[n],
                chopsticks[(n + 1) % sticks_number],
                print_queue
            )
        )
        for n in range(sticks_number)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    _cycle_completed.set()


if __name__ == '__main__':
    main()
