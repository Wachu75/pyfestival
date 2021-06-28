import secrets
import numpy as np

b = np.random.rand(10, 10)
print(b)
c = np.random.rand(0, 10)
mylist = list("ABCDEFGH")
a = secrets.randbits(4)
b = secrets.choice(mylist)
# 0101 4difrents bits
print(b)

print(a)
