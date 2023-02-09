import numpy as np

a = np.zeros((2, 2)) # 0으로 2*2 채우기
print(a)

a = np.ones((2, 3)) # 1로 2*2 채우기
print(a)

a = np.full((2, 3), 5) # 5로 2*3의 모든 칸 채우기
print(a)

a = np.eye(3) # 행과 열이 각각 3개씩 있는 identity matrix 출력하기
print(a)

a = np.array(range(20)).reshape((4, 5)) # 0~19까지 20개의 원소들로 4*5 행렬 만들기
print(a)
print(np.arange(20).reshape(4, 5)) # 15행과 같은 의미