name = "Kust - bot"
wheel_radius = 0.15
motor_count = 4
sensors = ["camera","lidar","imu"]

print(f"机器人:{name}")
print(f"传感器清单:{sensors}")
print(f"第一个传感器:{sensors[0]}")
print(f"传感器个数: {len(sensors)}")