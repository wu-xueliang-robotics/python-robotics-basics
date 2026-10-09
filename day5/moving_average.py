import random
import statistics
from utils.robot_math import moving_average

raw = [random.gauss(2.0,0.1)for i in range(50)]

filtered = moving_average(raw,window = 5)

print("原始 前十",[f"{x:.3f}" for x in raw[:10]])
print("滤波 前十",[f"{x:.3f}" for x in filtered[:10]])

print(f"原始：均值{statistics.mean(raw):.3f} 标准差{statistics.stdev(raw):.4f}")
print(f"滤波：均值{statistics.mean(filtered):.3f} 标准差 {statistics.stdev(filtered):.4f}")
