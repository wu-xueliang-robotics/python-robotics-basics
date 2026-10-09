sensor = {"name": "lidar","range":10.0,"rate":10,"topic":"/scan"}

print(sensor["name"])
sensor["rate"] = 20
sensor["frame"] = "base_link"
print(sensor)

for k,v in sensor.items():
    print(f"{k} = {v}")

sensors = [
    {"name":"camera","topic":"/image_raw","rate":30},
    {"name":"lidar","topic":"/scan","rate":10},
    {"name":"imu","topic":"/imu","rate":100}
]

for s in sensors:
    print(s["name"],"->",s["topic"])

print(sensors[0]["name"])
