speed = int(input("please input speed:"))

if speed > 5:
    print("speed is too fast,please drive slowly")
elif speed == 0:
    print("the robot is static")
elif speed < 0:
    print("speed can not be minus")
else:
    print("speed is safety")