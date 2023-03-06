from codetiming import Timer

array = list(range(100000))

@Timer(name="linear")
def linear(array):
    y = sum(array)
    return y

linear(array)
