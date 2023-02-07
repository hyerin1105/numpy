import numpy as np

lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# print(np.arange(1,10).reshape(3, 3))
a = np.array(lst)

bool_indexing_array = np.array([
    [False, True, False], 
    [True, False, True],
    [False, True, False]
])
# bool_indexing = (a % 2 == 0)
# print(bool_indexing)

n = a[bool_indexing_array]
# n = a[bool_indexing]

print(n) #True값만 출력