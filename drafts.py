import itertools
import random
print()
print('hello world')

res = str(12) not in 'na12bb'
print(min({pos_i: pos_i/2.4 for pos_i in [1,2,3]}.values()))

number_list = ['a', 'b', 'c']
less_than_zero = list(filter(lambda x: x == 'a', number_list))
comb = {'a': 1, 'b': 2}
k = list(comb.keys())[list(comb.values()).index(1)]

a = ['a', 'b', 'c']
b = ['d', 'e', 'f']
c = ['g', 'h', 'i']

for a1, a2 in itertools.product(a,a):
    print(f'{a1} amd {a2}')
print(list(itertools.product(a,a)))






