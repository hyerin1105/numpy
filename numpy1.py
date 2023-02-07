import numpy as np

list1 = [1, 2, 3, 4] #1차원 행렬
a = np.array(list1)
print(type(a))
print(a.shape)

b = np.array([[1, 2, 3], [4, 5, 6]]) #2차원
print(b.shape)
print(b[0, 0]) #출력값: 1
print(b[0][0])

c = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]) #3차원
print(c.shape)

#출력값
# (4,)
# (2, 3)
# (3, 3, 3)