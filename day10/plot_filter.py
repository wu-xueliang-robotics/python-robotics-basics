import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np

# 自动找系统里真实存在的中文字体（跨 Windows/Ubuntu 都能用）
CANDIDATES = [
    "Noto Sans CJK SC", 
    "Noto Serif CJK SC", 
    "Noto Sans CJK JP",    # Ubuntu 装了 fonts-noto-cjk 就有
    "WenQuanYi Micro Hei", "WenQuanYi Zen Hei",  # Ubuntu 常见
    "SimHei", "Microsoft YaHei",                  # Windows 常见
]
available = {f.name for f in font_manager.fontManager.ttflist}
found = [c for c in CANDIDATES if c in available]

if found:
    matplotlib.rcParams["font.sans-serif"] = found + ["DejaVu Sans"]
    print(f"使用中文字体: {found[0]}")
else:
    print("警告：没找到中文字体，中文会显示成方块")

matplotlib.rcParams["axes.unicode_minus"] = False

np.random.seed(42)
n = 200
t = np.linspace(0,4,n)

true_signal = 2.0 + 0.5 * np.sin(2 * np.pi * t)

noise = np.random.normal(0 , 0.2 , n)
raw =  true_signal + noise 

window = 5
kernel = np.ones(window) / window
filtered = np.convolve(raw,kernel,mode = "valid")

t_filtered = t[window//2:window//2+len(filtered)]

fig,axes = plt.subplots(2,2,figsize = (14,8))

#origin data
ax = axes[0,0]
ax.plot(t,raw,color = "gray",linewidth = 1 , label = "原始数据")
ax.plot(t , true_signal , "b--" ,linewidth = 2 , label = "真实信号")
ax.set_title("(1)原始传感器数据")
ax.set_xlabel("时间(s)");ax.set_ylabel("距离(m)")
ax.legend();ax.grid(True,alpha = 0.3)

#滤波后
ax = axes[0,1]
ax.plot( t , raw , color = "gray", linewidth = 1 , alpha = 0.4 , label = "原始数据")
ax.plot(t_filtered , filtered , "r-" ,linewidth = 2 , label = f"滑动平均({window})")
ax.plot(t , true_signal , "b--" ,linewidth = 2 , label = "真实信号")
ax.set_title("(2)滤波后")
ax.set_xlabel("时间(s)");ax.set_ylabel("距离(m)")
ax.legend();ax.grid(True,alpha = 0.3)

#噪声分布直方图
ax = axes[1,0]
noise_only = raw - true_signal
ax.hist(noise_only,bins = 30 , color = "steelblue", alpha = 0.7)
ax.set_title("(3)噪声分布(应该接近正态分布)")
ax.set_xlabel("误差(m)");ax.set_ylabel("频次")
ax.grid(True,alpha = 0.3)

#误差对比：滤波把误差变小了
ax = axes[1,1]
err_raw = raw - true_signal
err_filtered = filtered - true_signal[window//2:window//2+len(filtered)]
ax.plot(t,err_raw,color = "gray",linewidth = 1 ,alpha = 0.5,label = f"原始误差(std = {np.std(err_raw):.3f})")
ax.plot(t_filtered,err_filtered,"r--",linewidth = 2 ,label = f"滤波误差(std = {np.std(err_filtered):.3f})")
ax.axhline(0,color = "black",linewidth = 0.5)
ax.set_title("(4)误差对比(滤波后误差明更小)")
ax.set_xlabel("时间(t)");ax.set_ylabel("误差(m)")
ax.legend();ax.grid(True,alpha = 0.3)

plt.tight_layout()
plt.savefig("filter_result.png",dpi = 150)
print("已保存filter_result.png")