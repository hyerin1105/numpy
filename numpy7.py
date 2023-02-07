import numpy as np

lst1 = [
    [1, 2],
    [3, 4]
]

lst2 = [
    [5, 6],
    [7, 8]
]

a = np.array(lst1)
b = np.array(lst2)

c = np.dot(a, b) #내적함수: dot(), 외적함수: outer()
print(c)