"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.
"""
from collections import Sequence


def _check_window(x: int, y: int, z: int) -> bool:
    return (x + y) == z


data_to_process = [0, 1, 1, 2, 3, 5]


assert len(data_to_process) >= 3

a, b, c = data_to_process[0], data_to_process[1], data_to_process[2]
while data_to_process:
    if not _check_window(a, b, c):
        print(f'{a} {b} {c}')
        raise ValueError("Ivalid data")
    print(data_to_process)
    data_to_process = data_to_process[1:]
    if len(data_to_process) < 3:
        break
    a, b, c = b, c, data_to_process[2]
print("It's a fib sequence!")

