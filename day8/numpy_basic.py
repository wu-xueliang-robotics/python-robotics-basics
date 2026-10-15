import numpy as np
import random

list_data = [1.0, 2.0 , 3.0 , 4.0 ]
print(list_data * 2)
print(list_data + list_data )

arr = np.array([1.0 , 2.0 , 3.0 , 4.0])
print(arr * 2)
print(arr + arr)

np.zeros(5)
np.ones(5)
np.arange(0,10,2)
np.linspace(0,1,5)
np.random.normal(2.0,0.1,size = 20)

raw = np.round(np.random.normal(2.0,0.3,size = 20),3)
print(raw)
print(f"大于2.1的值有{raw[raw > 2.1]}")

arra = np.arange(10)
arra[4] = 5
print(arra)
print(arra[3])
print(arra[2:5])
print(arra[arra > 5])
print(arra[::-1])
