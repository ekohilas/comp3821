from random import shuffle
from sys import argv
from math import log

def make_grid(n):
    nums = [x for x in range(n**2)]
    shuffle(nums)
    l = [[y for y in nums[x*n:(x+1)*n]] for x in range(n)]
    print('\n'.join([','.join(['{:{}}'.format(item, int(log(n**2, 10)) + 2 ) for item in row])
        for row in l]))

make_grid(int(argv[1]))

