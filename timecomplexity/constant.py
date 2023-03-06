from codetiming import Timer

array = list(range(100000))

@Timer(name="constant")
def constant(array):
    x = 1 + array[0]
    return x

constant(array)
