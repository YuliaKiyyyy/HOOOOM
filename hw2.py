import time
import struct
import random
import hashlib
from multiprocessing import Pool, cpu_count


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1,3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


if __name__ == '__main__':
    start_time = time.time()

    with Pool(processes=cpu_count()) as pool:
        chunk_size = 10
        total_sum = sum(pool.map(slow_calculate, range(0, 501, chunk_size)))

    print("Total sum:", total_sum)
    print("Execution time: {} seconds".format(time.time() - start_time))