from codetiming import Timer
# from itertools import combinations

array = list(range(100000))

@Timer(name="quadratic")
def quadratic(array):
    z = [(a, b) for idx, a in enumerate(array) for b in array[idx + 1:]]
    return z[-1]

quadratic(array)