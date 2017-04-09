from random import shuffle
from sys import argv

def numbers(n):
    l = [x for x in range(n*2+1)]
    shuffle(l)
    print(*sorted(l[:len(l)//2]))
    print(*sorted(l[len(l)//2:]))

numbers(int(argv[1]))
