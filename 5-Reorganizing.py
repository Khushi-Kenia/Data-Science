import numpy as np
before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(before)
after = before.reshape((4, 2))                      #size should remain the same (elements amount)
print(after)

#Vertical Stacking
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])
print(np.vstack([v1, v2]))

#Horizontal Stacking
h1 = np.array([[1, 2], [8, 9]])
h2 = np.array([[7, 0], [4, 5]])
print(np.hstack([h1, h2]))