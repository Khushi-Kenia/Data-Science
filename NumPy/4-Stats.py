import numpy as np
stats = np.array([[1, 2, 3], [8, 5, 6]])
print(stats)
print(np.min(stats, axis = 1))                  #axis = 1 refers to columns and axis = 0 refers to rows
print(np.max(stats, axis = 0))
print(np.sum(stats))                            #play around with axis here
