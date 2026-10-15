import numpy as np

def moving_average_np(data , window = 5):
    kernel = np.ones(window) / window  #kernel---内核#
    return np.convolve(data, kernel ,mode = "valid")  #convolve---卷积#

def moving_average_loop(data,window = 5):
    result = []
    for i in range(len(data) + 1 - window):
        result.append(sum(data[i:i + window]) / window)
    return result

np.random.seed(42)
raw = np.random.normal(2.0,0.1,size = 50)

loop_result = moving_average_loop(raw , window = 5)
np_result = moving_average_np(raw , window = 5)

print("loop last five number:",[f"{i:.2f}"for i in loop_result[:5]])
print("np last five number :",[f"{i:.2f}" for i in np_result[:5]])
print("equal or different:",np.allclose(loop_result,np_result))  #判断两个浮点数组是否一致#