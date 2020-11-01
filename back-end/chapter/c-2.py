# array
import numpy as np

np.set_printoptions(precision=3)

data = np.array([122, 323, 4, 56, 334, 2, 5, 89])
data.sort()
print(data)

data[::-1].sort()
print(data)

data.sort()
print(data.cumsum())

# ramdom
from numpy import random

random.seed(0)

data_ = random.random(10)
print('random=', data_)
