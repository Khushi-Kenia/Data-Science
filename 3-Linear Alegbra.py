import numpy as np
a = np.ones((2,3))
b = np.full((3,2),2)
c = np.matmul(a,b)
d = np.linalg.det(np.matmul(a,b))
print(d)