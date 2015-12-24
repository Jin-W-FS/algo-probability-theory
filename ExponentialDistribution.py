import random

def frac():
    first = current = random.random()
    even = False
    while True:
        last = current
        current = random.random()
        even = not even
        if current > last:
            if even:
                return first
            else:
                return None

def expovariate():
    K = 0
    while True:
        X = frac()
        if X is None:
            K += 1
        else:
            return K + X

with open("data.log", "w") as outf:
    for i in range(10**5):
        print(expovariate(), file=outf)
