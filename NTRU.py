import numpy as np
import numpy.linalg as la
import random
import fractions
from utils import *

class NTRU:
    def __init__(self,n=7,q=31,p=3,d_f=3,d_g=2,d_r=2):
        self.n=n
        self.q=q
        self.p=p
        self.d_f=d_f
        self.d_g=d_g
        self.d_r=d_r

        self.generate_f()
        self.generate_C_f()
        self.generate_inverse_C_f_q()
        self.generate_inverse_C_f_p()

        self.generate_g()
        self.count=0
        while not(self.C_f_qp_condition()):
            self.generate_f()
            self.generate_C_f()
            self.generate_inverse_C_f_q()
            self.generate_inverse_C_f_p()
            self.count+=1

        self.h=self.p*self.inverse_C_f_q@self.g%self.q
        inverse_p_q=extended_euclidean_algorithm(self.p,self.q)[0][-2]%self.q
        self.H=inverse_p_q*self.convolute_matrix(self.h)


    def generate_f(self):
        self.f=np.zeros((self.n,1),dtype='int')
        a=[i for i in range(self.n)]
        random.shuffle(a)
        for i in a[:self.d_f]:
            self.f[i]=1
        for i in a[self.d_f+1:2*self.d_f]:
            self.f[i]=-1

    def generate_C_f(self):
        self.C_f=self.convolute_matrix(self.f)

    def generate_g(self):
        self.g=np.zeros((self.n,1),dtype='int')
        a=[i for i in range(self.n)]
        random.shuffle(a)
        for i in a[:self.d_g]:
            self.g[i]=1
        for i in a[self.d_g:2*self.d_g]:
            self.g[i]=-1

    def convolute_matrix(self,f):
        C_m=np.zeros((len(f),len(f)),dtype='int')
        for i in range(len(f)):
            C_m[:,i]=np.reshape(np.roll(f,i),self.n)
        return(C_m)

    def generate_inverse_C_f_q(self):
        self.inverse_C_f_q=gauss_jordan_modular_forward_backward(self.C_f,self.q)

    def generate_inverse_C_f_p(self):
        self.inverse_C_f_p=gauss_jordan_modular_forward_backward(self.C_f,self.p)

    def C_f_qp_condition(self):
        c1=isinstance(self.inverse_C_f_q,np.ndarray)
        c2=isinstance(self.inverse_C_f_p,np.ndarray)
        if c1 and c2:
            c3=la.norm(self.inverse_C_f_p@self.C_f%self.p-np.identity(self.n))<=1e-10
            c4=la.norm(self.inverse_C_f_q@self.C_f%self.q-np.identity(self.n))<=1e-10
            return c3 and c4
        else:
            return False

    def generate_r(self):
        r=np.zeros((self.n,1))
        a=[i for i in range(self.n)]
        random.shuffle(a)
        for i in a[:self.d_r]:
            r[i]=1
        for i in a[self.d_r:2*self.d_r]:
            r[i]=-1
        return(r)

    def encrypt(self,m):
        return (self.convolute_matrix(self.h)@self.generate_r()+m) %self.q

    def decrypt(self,c):
        a=(self.C_f@c)%self.q
        for i in range(len(a)):
            if a[i]>=self.q/2:
                a[i]-=self.q
        return self.inverse_C_f_p@a%self.p
