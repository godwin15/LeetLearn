
def array_reduce(array):
    total = 0

    while len(array) > 1:
        array.sort()
        a = array.pop(0)
        b = array.pop(0)
        total += a + b
        array.append(a + b)
    return total

a = [1,2=]
print(array_reduce(a))