#
# array
#

import numpy as np

np.set_printoptions(precision=3)

# asc sort
asc_data = np.array([122, 323, 4, 56, 334, 2, 5, 89])
asc_data.sort()
print('asc sort = ', asc_data)

# desc sort
desc_data = np.array([122, 323, 4, 56, 334, 2, 5, 89])
desc_data[::-1].sort()
print('desc sort = ', desc_data)

# accumulation
acc_data = np.array([2, 4, 5, 56, 89, 122, 323, 334])
print('cumsum = ', acc_data.cumsum())

#
# ramdom
#
from numpy import random

# set initial value of seed
random.seed(0)

# create random data
random_data = random.random(10)
print('random_data = ', random_data)

# choice random data and replace means duplicate
random_data = np.array([2, 4, 5, 56, 89, 122, 323, 334])
choiced_replace_true = random.choice(random_data, 5, replace=True)
print('choiced_replace_true = ', choiced_replace_true)
choiced_replace_false = random.choice(random_data, 5, replace=False)
print('choiced_replace_false = ', choiced_replace_false)

#
# matrix
#

# create matrix
array1 = np.arange(9).reshape(3, 3)
print('array1 = \n', array1)
print('array1 rows = ', array1[0, :])
print('array1 column = ', array1[:, 0])

# calculate
array1 = np.arange(9).reshape(3, 3)
array2 = np.arange(9, 18).reshape(3, 3)
print('array1 = \n', array1)
print('array2 = \n', array2)

# matrix multiple
matrix_multiple = np.dot(array1, array2)
print('matrix_multiple = \n', matrix_multiple)

# multiple
multiple = array1 * array2
print('multiple = \n', multiple)

# practice 2-1 natural number sum
array = np.array([i + 1 for i in range(50)])
print(sum(array))

# practice 2-2 standard normal distribution
random.seed(0)
randn = random.randn(10)
print('randn = ', randn)
print('max = ', randn.max())
print('min = ', randn.min())
print('sum = ', randn.sum())

# practrice 2-3
m = np.ones((5, 5), dtype=np.int64) * 3
print(m.dot(m))

#
# graph
#
file_path = './images/plot.png'

import matplotlib as mpl
import seaborn as sns
import matplotlib.pyplot as plt

random.seed(0)

fig = plt.figure(figsize=(20, 6))
plt.hist(np.random.randn(10 ** 5) * 10 + 50, bins=60, range=(20, 80))

fig.savefig(file_path)