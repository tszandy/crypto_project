import numpy as np
class ajtai:
    def __init__(self, n = 3):
        self.n = n
        self.m=n**3
        self.r_n=n**n

    def B_n(self):
        return np.random.random(self.n)*self.r_n-self.r_n/2

    
    def S_n(self):
        pass
