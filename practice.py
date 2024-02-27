a=10
print(id(10))
print(id(a))

def ad(a):
    print(id(a))
    a=12
    print(id(a))
    # print(id(b))

ad(a)