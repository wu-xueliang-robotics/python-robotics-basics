import numpy as np

#旋转矩阵#
def rotation_matrix(theta):
    c,s = np.cos(theta),np.sin(theta)
    return np.array([
        [c,-s,0],
        [s,c,0],
        [0,0,1]
    ])

#位移矩阵#
def translation_matrix(x,y):
    return np.array([
        [1,0,x],
        [0,1,y],
        [0,0,1]
    ])

angle = np.pi/2
R = rotation_matrix(angle)
P = np.array([1.0,0.0,1.0])

print("befor rotation:",P)
print("after rotation:",R @ P)

T1 = translation_matrix(1,0)
T2 = rotation_matrix(np.pi/2)
T3 = translation_matrix(0.5,0)

T_total = T1 @ T2 @ T3

p = np.array([0.0,0.0,1.0])
print(T1 @ p)
print(T1 @ T2 @ p)
print("final location:",T_total @ p)  #p先乘T3,再乘T2,再乘T1#
print(T3 @ T2 @ T1 @ p)  #p先乘T1,再乘T2,再乘T3#