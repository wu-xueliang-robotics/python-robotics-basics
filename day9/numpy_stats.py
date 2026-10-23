import numpy as np

np.random.seed(42)
normal = np.random.normal(2.0,0.05,size = 1000)
outliers = np.array([9.5,8.8,7.2,6.9,9.9])
raw = np.concatenate([normal,outliers])

print(f"均值  {np.mean(raw):.4f}")
print(f"标准差{np.std(raw):.4f}")
print(f"中位数{np.median(raw):.4f}")
print(f"最小值{np.min(raw):.4f}")
print(f"25%分位{np.percentile(raw,25):.4f}")
print(f"75%分位{np.percentile(raw,75):.4f}")

mu,sigma = np.mean(raw),np.std(raw)
lower,upper = mu - 3 * sigma,mu + 2 *sigma
print(f"正常范围：[{lower:.4f},{upper:.4f}]")

outliers_found = raw[(raw < lower) | (raw > upper)]
print(f"检测出异常{len(outliers_found)}个：{outliers_found}")

clean = raw[(raw > lower)&(raw < upper)]
print(f"清洗前{len(raw)}个，均值{np.mean(raw):.4f}")