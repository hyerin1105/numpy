import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

s = np.sum(a) # 원소 총합
print(s)

s = np.sum(a, axis=0) # 열끼리 합
print(s)

s = np.sum(a, axis=1) # 행끼리 합
print(s)

s = np.prod(a) # 원소 전부 곱하기
print(s)

print(a @ b)

print(a @ np.eye(2, 2))