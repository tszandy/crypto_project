import numpy as np
import numpy.linalg as la
from utils import *

n=15
l=4
sigma=0
count=0
import GGH
g=GGH.GGH(n=n,l=l,sigma=sigma)
m=np.random.randint(low=-100,high=100,size=(n,1))
c=g.encrypt(m)
print('c',c)
print('m',m)
print(m-la.inv(g.B)@g.R@np.round(la.inv(g.R)@c))
print(g.Hadamard_ratio(g.R))
print(g.Hadamard_ratio(g.B))

# import GGH
# for n in range(1,40):
#     g=GGH.GGH(n=n,l=l,sigma=sigma)
#     print(g.Hadamard_ratio(g.R))
#     print(g.Hadamard_ratio(g.B))
