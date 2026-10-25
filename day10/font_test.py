import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 1. 直接“硬编码”指定刚刚从终端查到的字体文件绝对路径
font_path = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'

# 创建字体属性对象，强制使用这个文件
font_prop = FontProperties(fname=font_path)

# 2. 修复负号显示
matplotlib.rcParams["axes.unicode_minus"] = False

# 3. 画图
fig, ax = plt.subplots(figsize=(6, 3))

# 4. 核心关键：在设置标题和标签时，显式传入 fontproperties 参数
ax.set_title("中文标题测试：机器人轮速", fontproperties=font_prop)
ax.set_xlabel("时间 (秒)", fontproperties=font_prop)
ax.set_ylabel("轮速 (rps)", fontproperties=font_prop)

ax.plot([1, 2, 3], [2, 3, 5])

# 5. 保存图片
plt.savefig("font_test.png", dpi=150)
print("已保存 font_test.png")