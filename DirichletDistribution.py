import random

def dirichletvariate(N, params):
    '''https://en.wikipedia.org/wiki/Dirichlet_distribution#Random_number_generation'''
    sample = [random.gammavariate(a,1) for a in params]
    s = sum(sample)
    return [v/s for v in sample]

def split(N):
    return dirichletvariate(N, [1] * N)

with open("data.log", "w") as outf:
    for i in range(10**4):
        print(*split(3), file=outf)
