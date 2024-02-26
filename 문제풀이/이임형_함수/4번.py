# 4-1
def print_coin():
    print("비트코인")
# 4-2
print_coin()

# 4-3
for _ in range(100):
    print_coin()

# 4-4
def print_coins():
    for _ in range(100):
        print("비트코인")

# 4-5
def mul(a,b):
    return a*b

def toUpper(ch):
    print(ch.upper())

def pickup_even(l):
    n=[]
    for i in l:
        if i%2==0:
            n.append(i)
    return n
