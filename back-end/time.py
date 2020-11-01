from random import random
from timeit import timeit

import numpy as np

N = 10 ** 6

normal_datas = [random() for _ in range(N)]

print(timeit(lambda: sum(normal_datas), number=10))

np_random_datas = np.array(normal_datas)
print(timeit(lambda: np.sum(np_random_datas), number=10))
