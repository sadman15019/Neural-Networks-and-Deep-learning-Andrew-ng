import numpy as np
'''
A=np.array([[56.0,0.0,4.4,68.0],
            [1.2,104.0,52.0,8.0],
            [1.8,135.0,99.0,0.9]])
cal=A.sum(axis=0) #sum vetically,axis=1 sums horizantally
percentage=100*A/cal.reshape(1,4) #this division is point to point operation ,not matrix operation
print(percentage)

x=np.array([[[1],[2]],[[3],[4]]])
print(x.shape)


a=np.random.randn(4,3)
b=np.random.randn(1,3)
c=a*b
print(c.shape)
a=np.array([[2,1],[1,3]])
print(np.dot(a,a))

#numpy reshaping
#-1 is for one unknown dimension
A=np.array([56,0,4,68,1,104,52,8,18,135,99,9])
A=A.reshape(4,3)
B=np.array([[56.0,0.0,4.4,68.0],
            [1.2,104.0,52.0,8.0],
            [1.8,135.0,99.0,0.9]])
B=B.reshape(-1)
print(A)
print(B)
'''