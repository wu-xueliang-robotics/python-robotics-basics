for i in range(5):
    print(f"this is NO.{i} test")
wheel_radius = 0.15
circle = 2 * 3.14 * wheel_radius
for speed in range(0,11,2):
    rps = speed/circle
    print(f"speed{speed:2d}m/s to 每秒{rps:.2f}圈")