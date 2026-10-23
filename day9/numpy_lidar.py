import numpy as np

np.random.seed(42)

wall_x = np.full(2000,5.0)
wall_y = np.random.uniform(-2,2,2000)
wall_z = np.random.uniform(0,1.5,2000)

points = np.column_stack([wall_x,wall_y,wall_z])
print(f"点云形状：{points.shape}")

distances = np.linalg.norm(points,axis=1)
print(f"最近{np.min(distances):.3f}m,最远{np.max(distances):.4f}m")
print(f"平均距离{np.mean(distances):.4f}m")

near_mask = distances < 5
near_points = points[near_mask]
print(f"五米内{len(near_points)}个点")

theta = np.radians(30)
c,s = np.cos(theta),np.sin(theta)
R = np.array([
    [c,-s,0],
    [s,c,0],
    [0,0,1]
])
rotated = (R @ points.T).T
print(f"旋转后的第一个点：{points[0]}")
print(f"               {rotated[0]}")