import numpy as np
import numpy.linalg as la
from utils import *


n=60
for n in range(400,1010):
    print('n',n)
    q=101
    p=5
    import NTRU
    N=NTRU.NTRU(n=n,q=q,p=p)
    # m=np.zeros((n,1))
    m=np.random.randint(low=0,high=p,size=(n,1))
    # print('m',m)
    c=N.encrypt(m)
    # print('c',c)
    new_m=N.decrypt(c)
    # print('new_m',new_m)
    # print(m-new_m)
    print('count',N.count)


# la.norm(N.inverse_C_f_p@N.C_f%p-np.identity(n))












# print(N.f)
# print(N.C_f)
# print(N.inverse_C_f_p)
# print(N.inverse_C_f_q)
# print(N.C_f@N.inverse_C_f_p)
# print(N.C_f@N.inverse_C_f_p%3)
# print(N.C_f@N.inverse_C_f_q)
# print(N.C_f@N.inverse_C_f_q%31)
# print(N.h)

# f=np.array([-1,0,0,1,1,-1,1])
# g=np.array([17,28,9,30,1,16,28])
# print(f)
# print(N.convolute_matrix(f))
# print(g)
# print(N.convolute_matrix(g))
# print(N.convolute_matrix(f)@N.convolute_matrix(g)%32)
