def test(x, y):
    tmp = x
    x = y
    y = tmp
    return y.append(x)
x = ["y"]
y = ["x"]
test(x, y)
print(x)