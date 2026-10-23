import numpy as np
import time

N = 1000

A_list = [[float(i + j) for j in range(N)]for i in range(N)]
B_list = [[float(i - j) for j in range(N)]for i in range(N)]

start = time.time()
result_list = [[sum(A_list[i][k] * B_list[k][j]for k in range(N))
                for j in range(N)]
                for i in range(N)]
python_time = time.time() - start
print(f"纯python:{python_time:.2f}秒")

A_np = np.array(A_list)
B_up = np.array(B_list)

start = time.time()
result_up = A_np @ B_up 
numpy_time = time.time() - start
print(f"numpy:  {numpy_time:.4f}秒")

print(f"加速比：  {python_time / numpy_time:.0f}倍")