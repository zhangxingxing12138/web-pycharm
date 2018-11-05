from functools import reduce
def sum_2(l):
    return reduce(lambda x,y:x+y,l)
