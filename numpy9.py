import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float64)
print(a.dtype)

d = np.random.permutation(6).reshape(2, 3) # 겹치지 않게 난수 출력(순열)
print(d)