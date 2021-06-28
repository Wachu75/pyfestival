import numpy as np

a = np.array([1,2,3,4])
print(a)

a = np.arange(0, 80, 10)
indices = [1,2,-3]
y = a[indices]
print(y)
mask = np.array([0,1,1,0,0,0,1,0], dtype=bool )
z = a[mask]
print(z)
a = np.arange(25).reshape(5, 5)
#mask = np.array([0, 2, 3, 3], [2, 3, 1, 4])
y = a[[0,2,3,3],[2,3,1,4]]
#y = a[mask]
print(y)
z = a[a % 3 == 0]
print(z)
#-------------------------
a = np.ones((3, 5))
b = np.ones((5,))
b.reshape(1, 5)
#  b[np.newaxis, :]
#--------------dokonczyć myśl ?

a = np.array([[1,2,3],[4,5,6]])
print(a.sum())
print(a.sum(axis=0))
print(a.sum(axis=0).shape)
print(a.sum(axis=-1))
print(a.sum(axis=-1).shape)
print(np.min(a))
print()


