import numpy as np # numpy 사용 선언

list1 = [1, 2, 3, 4] # 1차원 행렬
a = np.array(list1) # a라는 행렬을 ndarray화 하기
print(type(a)) # type()을 통해 a의 유형 파악 -> <class 'numpy.ndarray'>
print(a.shape)
# 출력 => (4,) : 1차원(x가 4개)

b = np.array([[1, 2, 3], [4, 5, 6]]) # 2차원
print(b.shape)
# 출력=> (2, 3) : 2차원(x = 2개, y = 3개)

print(b[0, 0]) # 출력값: 1 -> 0행 0열 = 1
print(b[0][0]) # 10행과 같은 의미

c = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]) #3차원
print(c.shape)
# 출력=> (3, 3, 3) : 3차원(x, y, z 모두 3개씩)