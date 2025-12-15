import numpy as np
import sys

# a = np.array([1, 2, 3,4,5], dtype=np.int64)
# print(a)
# print(a.dtype)
# print(a.shape)
# print(a.nbytes)
# print(a.itemsize)

# c = np.arange(10)
# print(c)
# print(c.dtype)
# print(c.shape)
# print(c.nbytes)

# A = np.arange(6)
# print(x)
# y = x.reshape(2, 3)
# print("x:", x)
# print("y:", y)
# print("x.shape:", x.shape)
# print("x.nbytes:", x.nbytes)
# print("y.shape:", y.shape)
# print("y.nbytes:", y.nbytes)


# x = np.array([1, 2, 3, 4])
# print("x:", x)
# print("x shape:", x.shape)

# y = x.reshape(2, 2)
# print("y:", y)
# print("y shape:", y.shape)

# x = np.array([10, 20, 30, 40])
# y = x.reshape(2, 2)

# print("x:", x)
# print("y:", y)

# y[0, 0] = 999   # modify y

# print("After modification:")
# print("x:", x)
# print("y:", y)

# x = np.array([1,2,3,4,5,6])
# y = x.reshape(2,3)

# print(y.base is A) 

# x = np.array([1,2,3,4,5,6])
# z = x[::2]        # slicing with a step
# w = x.copy()      # explicit copy

# print("z base is x:", z.base is x)
# print("w base is x:", w.base is x)

# x = np.array([10, 20, 30, 40, 50, 60])
# a = x[1:4]     # slice index 1 to 3
# print("x:", x)
# print("a:", a)
# print("a.base is x:", a.base is x)

# b = x[::2]
# print("b:", b)
# print("b.base is x:", b.base is x)

# x = np.array([100, 200, 300, 400, 500, 600])

# a = x[2:5]
# b = x[::3]
# c = x[[0, 3]]
# print("a:", a)
# print("b:", b)
# print("c:", c)  
# print(a.base is x)
# print(b.base is x)
# print(c.base is x)

# x = np.array([12, 5, 30, 7, 42, 19, 8])

# a = x[x < 10]       # all values < 10  
# b = x[x % 2 == 0]   # all even numbers  
# c = x[x > 20]       # all values > 20  

# x = np.array([
#     [10, 20, 30],
#     [ 5, 15, 25],
#     [40, 50, 60],
#     [ 7,  8,  9]
# ])

# a = x[x[:, 0] < 10]          # rows where col0 < 10
# b = x[x[:, 1] >= 15]         # rows where col1 >= 15
# c = x[x[:, 2] % 3 == 0]      # rows where col2 divisible by 3

# print("a:", a)
# print("b:", b)
# print("c:", c)

# A = np.array([[1,2,3],
#               [4,5,6]])

# b = np.array([10,20,30])
# c = A + b
# print("A:\n", A)
# print("b:", b)
# print("A + b:\n", c)


# x = np.array([5, 10, 15, 20])

# print("x * 3:", x * 3)
# print("x -5:", x - 5)
# print("x / 5", x / 5)
# print("x ** 2:", x ** 2)

# x = np.array([
#     [2, 4,  6],
#     [3, 6,  9],
#     [5, 10, 15]
# ])
# print(np.sum(x))     # total
# print(np.mean(x))    # average
# print(np.max(x))     # largest value
# print(np.min(x))     # smallest value
# print(np.std(x)) 


# A = np.array([[1,2],[3,4]])
# B = np.array([[5,6],[7,8]])
# C = np.array([9,10])

# v= np.vstack([A, B])
# h = np.hstack([A, B])
# col = np.column_stack([A[:,0], C])
# print("v:\n", v)
# print("h:\n", h)
# print("col:\n", col)

x = np.array([1,2,3,4,5,6,7,8])
x_split = np.array_split(x, 4)
print("x_split:", x_split)
parts = np.split(x, [3, 6])
print("parts:", parts)