import numpy as np

lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
] #2차원(1차원 배열을 원소로 가지므로)
arr = np.array(lst)

# slice: 일부분만 출력하기
a = arr[0:2, 0:2]
print(a)
print(arr[1: , :1])

a = arr[1:, 1:]
print(a)