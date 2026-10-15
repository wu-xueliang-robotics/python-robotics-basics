import numpy as np

T = np.array([
    [1 , 0 , 1],
    [0 , 1 , 2],
    [0 , 0 , 1]
])

point = np.array([0.5 , 0.3 , 1])

new_point = T @ point  #当@的右侧是一个一维数组时，numpy会临时把它但作列向量参与运算#

print(T)
print("change befor:",point)
print("change after:",new_point)

A = np.array([[1 , 2],[3 , 4]])
print(A.T) #转置#
print(np.linalg.inv(A)) #求逆#
print("A @ A = ",A @ A) #矩阵乘法#
print("A * A = ",A * A) #矩阵逐元素相乘#

B = np.array([[0,0,3],[0,0,5],[1,2,3]])

point1 = np.array([0,0,1])

point2 = B @ point1
print("变化前：",point1)
print("变换后：",point2)