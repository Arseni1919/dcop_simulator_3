import itertools
import random

import numpy as np

# print()
# print('hello world')
#
# res = str(12) not in 'na12bb'
# print(min({pos_i: pos_i/2.4 for pos_i in [1,2,3]}.values()))
#
# number_list = ['a', 'b', 'c']
# less_than_zero = list(filter(lambda x: x == 'a', number_list))
# comb = {'a': 1, 'b': 2}
# k = list(comb.keys())[list(comb.values()).index(1)]
#
# a = ['a', 'b', 'c']
# b = ['d', 'e', 'f']
# c = ['g', 'h', 'i']
#
# for a1, a2 in itertools.product(a,a):
#     print(f'{a1} amd {a2}')
# print(list(itertools.product(a,a)))
#
# print(list(map(lambda x: x == 3, [1,2,3])))
import math
l = [1,2,10, 8]
print(f'sum: {sum(l)}')
print(f'max: {max(l)}')
print(f'min: {min(l)}')
print(f'min: {math.count(l)}')
import time
# start_time = time.time()
# your script
# elapsed_time = time.time() - start_time
# print(time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
# # print(f'sum: {sum([True, False, True])}')
# any([not x for x in [1, 2, 2]])
# print(any([not x for x in [1, 2, 2]]))
import matplotlib.pyplot as plt
# plt.close()


import datetime
# print(datetime.datetime.now())
if None:
    print('A')
else:
    print('B')
a = [1, 2, 7, 4, 5]
b = [9, 8, 7, 6, 5]
print('mean', np.mean(a), 'var', np.var(a))
common = set(a) & set(b)
print(len(common))


