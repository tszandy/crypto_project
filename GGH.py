import numpy as np
import random
import numpy.linalg as la

class GGH:
    """
    This is a class for GGH crypto system
    """
    def __init__(self,n = 3,l = 4,sigma = 1):
        """
        Parameters:
            n(int): size of message
        """
        self.n = n
        self.l=l
        self.generate_R()
        self.generate_B()
        self.sigma=sigma

    def generate_R(self):
        self.R=np.random.randint(low=-self.l,high=self.l,size=(self.n,self.n))
        self.R=self.R+np.identity(self.n)*round(np.sqrt(self.n))*self.l

    def generate_B(self):
        self.B=np.copy(self.R)
        for i in range(4):
            self.B=self.B@self.generate_L()
            self.B=self.B@self.generate_U()

    def generate_L(self):
        L=np.zeros((self.n,self.n))
        for i in range(self.n):
            for j in range(0,i+1):
                if i==j:
                    L[i,j]=random.sample([-1,1],1)[0]
                else:
                    L[i,j]=random.sample([-1,0,1],1)[0]
        return L

    def generate_U(self):
        U=np.zeros((self.n,self.n))
        for i in range(self.n):
            for j in range(i,self.n):
                if i==j:
                    U[i,j]=random.sample([-1,1],1)[0]
                else:
                    U[i,j]=random.sample([-1,0,1],1)[0]
        return U

    def encrypt(self,m):
        return self.B@m+np.random.random((self.n,1))*2*self.sigma-self.sigma

    def decrypt(self,c):
        return la.inv(self.B)@self.R@np.round(la.inv(self.R)@c)

    def Hadamard_ratio(self,B):
        length=1
        for i in B:
            length*=la.norm(i)
        return((la.det(B)/length)**(1/len(B)))

    # def decrypt(self,c):
    #     return la.solve(self.B,self.R@np.round(la.solve(self.R,c)))
