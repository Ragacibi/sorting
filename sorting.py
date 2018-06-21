#! /usr/bin/env python3
''' This program does a bubble sort of the given input
values and return a generator object
'''

def bub_sort(iterable, rev=False):
    '''This function does bubble 
sort'''
    iterable = list(iterable)
    repeat = sum(1 for elem in iterable) - 1
    print()
    while repeat != 0:
        for _ in range(repeat):
            swap = True
            if iterable[_] > iterable[_+1]:
                iterable[_],iterable[_+1] = iterable[_+1],iterable[_]
        
        repeat-=1
#    iterable = map(iter,iterable)
    yield map(iter,iterable)

if __name__ == '__main__':
    IP = map(int, input("Enter integers: ").split())
    OP = bub_sort(IP)
    print(list(OP))

exit(0)
