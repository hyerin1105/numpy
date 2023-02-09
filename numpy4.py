import numpy as np

lst = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
a = np.array(lst)

s = a[[0, 2], [1, 3]] #a[[row1, row2], [col1, col2]]
print(s)
