import numpy as np

def extended_euclidean_algorithm(a,b):
    c=[]
    gcd(a,b,c)
    x=[1,0]
    y=[0,1]
    for i in range(len(c)):
        x.append((x[-1]*c[i]+x[-2]))
        y.append((y[-1]*c[i]+y[-2]))
    for i in range(len(c)+2):
        if i%2==0:
            y[i]=-y[i]
        else:
            x[i]=-x[i]
    return (x,y)

def gcd(a,b,c=[]):
    if b!=0:
        c.append(int(a/b))
        return gcd(b,a%b,c)
    else:
        return a

def gauss_jordan_modular_forward_backward(A,q):
    n=A.shape[0]
    B=np.identity(n)
    M=np.concatenate([A,B],axis=1)%q
    for i in range(n):
        istar=i+np.ndarray.argmax(abs(M[i:n,i]))
        if M[istar,i]==0:
            return None
        else:
            M[[i,istar]]=M[[istar,i]]
        M[i]=M[i]*extended_euclidean_algorithm(M[i,i],q)[0][-2]%q
        for j in range(i+1,n):
            M[j]=(M[j]-M[j,i]*M[i])%q
    for i in range(n)[::-1]:
        for j in range(i+1,n):
            M[i]=(M[i]-M[i,j]*M[j])%q
    inverse=M[:,n:]%q
    return inverse

# def gauss_jordan_modular(A,q):
#     n=A.shape[0]
#     B=np.identity(n)
#     M=np.concatenate([A,B],axis=1)%q
#     for i in range(n):
#         istar=i+np.ndarray.argmax(abs(M[i:n,i]))
#         if M[istar,i]==0:
#             return None
#         else:
#             M[[i,istar]]=M[[istar,i]]
#         M[i]=M[i]*extended_euclidean_algorithm(M[i,i],q)[0][-2]%q
#         for j in range(n):
#             if j!=i:
#                 M[j]=M[j]-M[j,i]*M[i]
#     inverse=M[:,n:]%q
#     return inverse
