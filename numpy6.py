import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = a + b # 인자끼리 더한 값
# c = np.add(a, b)
print(c) # shape가 같아야 가능

c = a - b
print(c)

c = a * b
print(c)

c = a / b
print(c)